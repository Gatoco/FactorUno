// Etiquetas de las columnas 8-37 segun hoja 3.TIpos de datos / 3.2 Homologacion
export const LABELS = {
  8: 'Con crédito IDPC (gen. 01.01.2017)',
  9: 'Con crédito IDPC (acum. 31.12.2016)',
  10: 'Con derecho crédito pago IDPC voluntario',
  11: 'Sin derecho a crédito',
  12: 'RAP y Dif. Inicial (ex Art. 14 TER A)',
  13: 'Otras rentas percibidas sin prioridad',
  14: 'Exceso Distribuciones Desproporcionadas (N°9 Art.14 A)',
  15: 'ISFUT Ley N°20.780',
  16: 'Rentas hasta 31.12.1983 / ISFUT Ley N°21.210',
  17: 'Rentas exentas IGC (Art.11 L.18.401) afectas a IA',
  18: 'Rentas exentas IGC y/o IA',
  19: 'Ingresos No Constitutivos de Renta',
  20: 'No sujetos restitución hasta 31.12.2019 sin derecho',
  21: 'No sujetos restitución hasta 31.12.2019 con derecho',
  22: 'No sujetos restitución desde 01.01.2020 sin derecho',
  23: 'No sujetos restitución desde 01.01.2020 con derecho',
  24: 'Sujetos a restitución sin derecho',
  25: 'Sujetos a restitución con derecho',
  26: 'Sujetos a restitución sin derecho (2)',
  27: 'Sujetos a restitución con derecho (2)',
  28: 'Crédito por IPE',
  29: 'Asociados a Rentas Afectas, sin derecho',
  30: 'Asociados a Rentas Afectas, con derecho',
  31: 'Asociados a Rentas Exentas (Art.11 L.18.401), sin derecho',
  32: 'Asociados a Rentas Exentas (Art.11 L.18.401), con derecho',
  33: 'Crédito por IPE (acumulados 31.12.2016)',
  34: 'Crédito impuesto tasa adicional ex Art.21 LIR, sin derecho',
  35: 'Crédito impuesto tasa adicional ex Art.21 LIR, con derecho',
  36: 'Tasa efectiva crédito FUT (TEF)',
  37: 'Tasa efectiva crédito FUT (TEX)',
}

export const MONTOS_COLS = Object.keys(LABELS).map(Number)
export const BASE_COLS = MONTOS_COLS.filter((c) => c <= 19) // base del calculo 8..19

export function formatFecha(iso) {
  if (!iso) return ''
  return iso.slice(0, 10)
}

export function sumaBase(factores) {
  return BASE_COLS.reduce((acc, c) => acc + (factores[c] || 0), 0)
}

// Agrupación de columnas por concepto (hoja 3.2 Homologacion del HDU)
export const GRUPOS = [
  { desde: 8, hasta: 11, concepto: 'Afectos a impuestos globales y/o adicional (IDPC)' },
  { desde: 12, hasta: 16, concepto: 'Rentas con tributación cumplida (RAP, ISFUT)' },
  { desde: 17, hasta: 18, concepto: 'Rentas exentas de IGC' },
  { desde: 19, hasta: 19, concepto: 'Ingresos no constitutivos de renta' },
  { desde: 20, hasta: 23, concepto: 'No sujetos a restitución' },
  { desde: 24, hasta: 27, concepto: 'Sujetos a restitución' },
  { desde: 28, hasta: 28, concepto: 'Crédito por IPE' },
  { desde: 29, hasta: 32, concepto: 'Acumulados hasta 31.12.2016' },
  { desde: 33, hasta: 33, concepto: 'Crédito por IPE (acumulados hasta 2016)' },
  { desde: 34, hasta: 35, concepto: 'Crédito impuesto tasa adicional (Art. 21 LIR)' },
  { desde: 36, hasta: 37, concepto: 'Tasa efectiva del crédito FUT (TEF/TEX)' },
]

export function grupoDe(col) {
  const g = GRUPOS.find((x) => col >= x.desde && col <= x.hasta)
  if (!g) return ''
  const rango = g.desde === g.hasta ? `C${g.desde}` : `C${g.desde}–${g.hasta}`
  return `${rango}: ${g.concepto}`
}

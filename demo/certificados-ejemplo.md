# Certificados de ejemplo para ingresar a mano

Cómo se usa: **Ingresar** → completar *Datos básicos* → pestaña **Montos** (solo las columnas que trae el certificado) → **Guardar**.
Las demás columnas y los factores se calculan solos con **Calcular factores** (desde **Ver**).

Reglas fijas: fecha `AAAA-MM-DD` · Mercado ACN / CFI / FM · Sociedad A = abierta, C = cerrada · Origen corredor o entidad · la suma de la base (columnas 8–19) no puede pasar de 1.

> Si el lote de la demo ya está cargado, los ejemplos 1 a 4 existen: usalos solo cambiando el **N° de dividendo** (si no, la app responde «duplicado»).

---

## Ejemplo 1 — AGUAS ANDINAS S.A.

| Campo | Valor |
|---|---|
| Mercado | CFI |
| Instrumento | AGUAS ANDINAS S.A. |
| Ejercicio | 2024 |
| Fecha pago | 2024-08-12 |
| Secuencia evento | 1 |
| N° de dividendo | 1450 |
| Tipo sociedad | Abierta (A) |
| Valor histórico | 300000 |
| Origen | corredor |
| ISFUT | no |

| Columna | Concepto | Monto |
|---|---|---|
| 8 | Con crédito IDPC (gen. 01.01.2017) | 150000 |
| 12 | RAP y Dif. Inicial (ex Art. 14 TER A) | 50000 |

Base 8–19 = 200000 → Factores: **col 8 = 0.75** · **col 12 = 0.25**

---

## Ejemplo 2 — ENEL AMERICAS S.A.

| Campo | Valor |
|---|---|
| Mercado | ACN |
| Instrumento | ENEL AMERICAS S.A. |
| Ejercicio | 2024 |
| Fecha pago | 2024-05-09 |
| Secuencia evento | 2 |
| N° de dividendo | 880 |
| Tipo sociedad | Abierta (A) |
| Valor histórico | 640000 |
| Origen | corredor |
| ISFUT | no |

| Columna | Concepto | Monto |
|---|---|---|
| 8 | Con crédito IDPC (gen. 01.01.2017) | 200000 |
| 12 | RAP y Dif. Inicial (ex Art. 14 TER A) | 120000 |

Base 8–19 = 320000 → Factores: **col 8 = 0.625** · **col 12 = 0.375**

---

## Ejemplo 3 — CENCOSUD S.A.

| Campo | Valor |
|---|---|
| Mercado | ACN |
| Instrumento | CENCOSUD S.A. |
| Ejercicio | 2024 |
| Fecha pago | 2024-05-06 |
| Secuencia evento | 4 |
| N° de dividendo | 1201 |
| Tipo sociedad | Abierta (A) |
| Valor histórico | 1250000 |
| Origen | corredor |
| ISFUT | no |

| Columna | Concepto | Monto |
|---|---|---|
| 8 | Con crédito IDPC (gen. 01.01.2017) | 400000 |
| 9 | Con crédito IDPC (acum. 31.12.2016) | 250000 |
| 12 | RAP y Dif. Inicial (ex Art. 14 TER A) | 100000 |

Base 8–19 = 750000 → Factores: **col 8 = 0.53333333** · **col 9 = 0.33333333** · **col 12 = 0.13333333**

---

## Ejemplo 4 — FONDO MUTUO LARRAIN VIAL

| Campo | Valor |
|---|---|
| Mercado | FM |
| Instrumento | FONDO MUTUO LARRAIN VIAL |
| Ejercicio | 2024 |
| Fecha pago | 2024-06-14 |
| Secuencia evento | 1 |
| N° de dividendo | 300 |
| Tipo sociedad | Cerrada (C) |
| Valor histórico | 2100000 |
| Origen | corredor |
| ISFUT | no |

| Columna | Concepto | Monto |
|---|---|---|
| 8 | Con crédito IDPC (gen. 01.01.2017) | 700000 |
| 9 | Con crédito IDPC (acum. 31.12.2016) | 300000 |
| 17 | Rentas exentas IGC (Art.11 L.18.401) afectas a IA | 50000 |

Base 8–19 = 1050000 → Factores: **col 8 = 0.66666667** · **col 9 = 0.28571429** · **col 17 = 0.04761905**

---

## Ejemplo 5 — FALABELLA S.A. (ejercicio nuevo)

| Campo | Valor |
|---|---|
| Mercado | ACN |
| Instrumento | FALABELLA S.A. |
| Ejercicio | 2025 |
| Fecha pago | 2025-04-15 |
| Secuencia evento | 1 |
| N° de dividendo | 2100 |
| Tipo sociedad | Abierta (A) |
| Valor histórico | 900000 |
| Origen | entidad |
| ISFUT | no |

| Columna | Concepto | Monto |
|---|---|---|
| 8 | Con crédito IDPC (gen. 01.01.2017) | 300000 |
| 9 | Con crédito IDPC (acum. 31.12.2016) | 100000 |

Base 8–19 = 400000 → Factores: **col 8 = 0.75** · **col 9 = 0.25**

---

## Ejemplo 6 — SQM S.A.

| Campo | Valor |
|---|---|
| Mercado | ACN |
| Instrumento | SQM S.A. |
| Ejercicio | 2024 |
| Fecha pago | 2024-11-05 |
| Secuencia evento | 3 |
| N° de dividendo | 1750 |
| Tipo sociedad | Cerrada (C) |
| Valor histórico | 1500000 |
| Origen | corredor |
| ISFUT | no |

| Columna | Concepto | Monto |
|---|---|---|
| 8 | Con crédito IDPC (gen. 01.01.2017) | 500000 |
| 12 | RAP y Dif. Inicial (ex Art. 14 TER A) | 300000 |

Base 8–19 = 800000 → Factores: **col 8 = 0.625** · **col 12 = 0.375**

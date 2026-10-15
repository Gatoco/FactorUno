# LEEME — cómo generar el podcast en NotebookLM

Este archivo NO se sube al notebook: es la guía para armarlo.

## Qué hay en esta carpeta

| Archivo | Para qué sirve |
|---|---|
| `01 - El proyecto en simple.md` | Fuente: qué es FactorUno, para quién y por qué existe |
| `02 - Conceptos en simple.md` | Fuente: los conceptos tributarios y técnicos explicados fácil |
| `03 - Como usar la app paso a paso.md` | Fuente: recorrido completo de la aplicación |
| `LEEME - instrucciones para el podcast.md` | Este archivo (no subir) |

## Paso a paso (5 minutos)

1. Entrar a https://notebooklm.google.com con la cuenta de Google.
2. **Crear notebook**.
3. **Añadir fuentes** → subir los tres archivos numerados (`01`, `02` y `03`). No subir este LEEME.
4. Esperar a que procese las fuentes y abrir **Audio Overview** → **Personalizar**.
5. Idioma: Español. Pegar el prompt de abajo tal cual y **Generar**.

## Prompt para pegar en "Personalizar" (copiar todo el bloque)

> Genera un podcast en español, como una conversación entre dos personas, dirigido a una sola persona: el autor de este proyecto, que necesita entenderlo de punta a punta para explicarlo en un video de entrega universitaria y no es experto en tributaria.
>
> Reglas:
> - Explica los conceptos complejos con palabras simples y ejemplos concretos usando los datos de las fuentes (CENCOSUD, ENEL AMERICAS, AGUAS ANDINAS; montos 200.000 y 120.000; factor 0.625; suma 1.075; etc.).
> - Cada vez que aparezca una sigla o término técnico (DJ 1948, IDPC, SII, S3, DynamoDB, EC2, API), explícalo en una frase antes de seguir.
> - No supongas conocimiento previo de programación ni de contabilidad.
>
> Temas que DEBE tocar, en este orden aproximado:
> 1. Qué es FactorUno: la aplicación que registra y calcula la calificación tributaria de los dividendos para la empresa nuam (la bolsa), y qué problema resuelve.
> 2. El caso de la demo: el cierre de dividendos del ejercicio 2024 y qué es un certificado DJ 1948.
> 3. El corazón tributario: los montos vienen en columnas numeradas del SII, se agrupan por concepto (homologación), se suman las columnas 8 a 19 y de ahí sale el factor de cada columna (monto dividido por la suma). Con un ejemplo completo de un certificado.
> 4. Cómo se usa la app, paso a paso: entrar con usuario y contraseña, la grilla y los filtros, ingresar un certificado a mano, ver el detalle, calcular los factores, editarlos y el aviso de "supera 1", cargar un lote por CSV con vista previa, la auditoría y la exportación con URL firmada.
> 5. Dónde vive todo, en palabras simples: la página publicada en la nube de AWS con dirección fija, la base de datos, el espejo de la auditoría en DynamoDB y los respaldos en S3.
> 6. Cierra con 5 frases clave que el autor puede decir en el video para explicar el proyecto de forma sencilla.
>
> Tono: cercano y claro, sin pausas publicitarias, sin promesas exageradas. Que se entienda todo a la primera escucha.

## Si algo sale mal

- **Sale en inglés**: volver a generar revisando que el idioma esté en Español.
- **Se salta temas**: regenerar (cada generación es distinta) o revisar que los 3 archivos estén como fuentes.
- **Sale muy técnico**: regenerar pegando de nuevo el prompt completo.

## Después del podcast

- El guion para el video (qué decir y hacer en cada toma) está en `../guion-demo.md`.
- Este podcast es material de estudio personal: no se entrega.

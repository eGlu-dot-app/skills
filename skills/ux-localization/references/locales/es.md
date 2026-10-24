# es-ES and es-419: Spanish (Spain, Latin America)

All terms and examples are `proposed` and need native review.

## Contents

1. Scope and register
2. Language characteristics and UX implications
3. Typography and punctuation
4. Common mistakes, both markets (ES-01 to ES-14)
5. Mistakes specific to es-ES (ESES-01 to ESES-04) and es-419 (ES419-01 to ES419-04)
6. Worked examples

## 1. Scope and register

- es-ES: Spain.
- es-419: one shared text variant for Latin America. It is a language choice, not a single market: numbers, currency and some vocabulary still differ by country (es-MX, es-AR, es-CO, es-CL). Country variants and voseo (vos, used for example in Argentina) are out of scope; neutral es-419 uses tú or usted.
- Proposed default for both: **tú**. Use **usted** for formal or regulated contexts (banking, health, government) when the brand chooses it. Never mix within a product.
- Addressing several people: es-ES vosotros, es-419 ustedes. Most UI addresses one user, so this rarely appears; check it in team or group messages.
- Buttons and menu items: **infinitive** (Guardar, Cancelar, Eliminar, Iniciar sesión).
- Instructions: imperative. tú: es-ES "Introduce", es-419 "Ingresa". usted: "Introduzca" / "Ingrese".

## 2. Language characteristics and UX implications

- **Grammatical gender and agreement.** Adjectives and participles agree: "Cambios guardados", "Carpeta eliminada", "Archivo eliminado". Variables need `select` or a rephrase (ES-11).
- **Gendered welcomes.** "Bienvenido" assumes a male user. Neutral rewrites: "Te damos la bienvenida", "¡Hola, {firstName}!". Forms with @, x or -e are not standard; using them is a brand decision.
- **"su" is ambiguous** with usted (your, his, her, their). Prefer the article when the owner is clear: "El archivo se guardó" rather than "Su archivo se guardó".
- **Recent past differs by market (tendency, not a strict rule).** es-ES often uses the present perfect for just-completed events ("No se han podido guardar los cambios"); es-419 often uses the simple past ("No se pudieron guardar los cambios"). Pick per locale and keep it.
- **Passive.** Spanish prefers the "se" form or an adjectival state ("Se guardaron los cambios", "Cambios guardados") over "fueron guardados".
- **Gerund.** Progress statuses are fine ("Guardando…", "Cargando…"). Avoid gerunds as titles copied from English "-ing" headings ("Creando un proyecto" for "Creating a project" as a help title; write "Crear un proyecto" or "Cómo crear un proyecto").
- **Plural.** 0 takes the plural ("0 archivos"). CLDR also has `many` for exact millions, which take "de": "1.000.000 de archivos" (`formats.md`).
- **Capitalization.** Sentence case. Days, months and languages are lowercase. After a colon, continue in lowercase in normal text.
- **Text length.** Spanish UI strings are often longer than English. Test real widths.
- **"y" and "o" change** before certain sounds: "e" before an /i/ sound ("Diseño e ilustración"), "u" before an /o/ sound ("siete u ocho").

## 3. Typography and punctuation

- Opening ¿ and ¡ are required where the question or exclamation starts, even mid-sentence: "Si no lo encuentras, ¿quieres buscar en otra carpeta?"
- Quotation marks: « » are traditional in Spain; “ ” are common in both markets and in UI. Product setting.
- Numbers and currency: format by the user's region, not by es-ES or es-419 alone. CLDR es-ES output is 1234 and 12.345,67. [S18] RAE and ASALE guidance writes 4-digit numbers without a separator and recommends a space for larger groups. [S17] Follow the formatter unless the product style guide says otherwise.
- Times: es-ES 14:30; es-419 formatters often give 2:30 p.m.
- No final period on buttons, menu items, titles or standalone labels.

## 4. Common mistakes, both markets

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| ES-01 | Punctuation | Eliminar este archivo? / Listo! | ¿Eliminar este archivo? / ¡Listo! | Opening marks are required. |
| ES-02 | Casing | Crear Un Nuevo Proyecto | Crear un proyecto | No English title case. |
| ES-03 | Register | tú in onboarding, usted in errors | One address form | Brand decision; keep it. |
| ES-04 | Inclusiveness | Bienvenido, {firstName} | Te damos la bienvenida, {firstName} / ¡Hola, {firstName}! | Do not assume gender. |
| ES-05 | Translationese | Tus cambios fueron guardados exitosamente. | Cambios guardados. | Cut stacked passive and "exitosamente". |
| ES-06 | Translationese | Creando un proyecto (help title) | Crear un proyecto / Cómo crear un proyecto | Gerund headings copied from English -ing. |
| ES-07 | False friend | Este formato no es soportado. | No se admite este formato. / Formato no compatible. | "soportar" means to endure. |
| ES-08 | False friend | librería (software library), eventualmente (eventually), actualmente (actually) | biblioteca, con el tiempo or más adelante, en realidad | librería means bookshop; eventualmente means possibly or by chance (DLE); actualmente means currently. "asistir" is not a general false friend: "asistir a" + event means attend, while "asistir" + person means help ("ayudar" is more natural in UI). [S27] |
| ES-09 | Style | Realizar una búsqueda / Realizar el pago | Buscar / Pagar | "realizar" + noun copies "perform a". |
| ES-10 | Style | Por favor, guardar / Guardar por favor | Guardar | No "por favor" on buttons. |
| ES-11 | Variables | {item} eliminado. | El archivo se eliminó. / La carpeta se eliminó. | Gender per object; use `select` or full strings. |
| ES-12 | Meaning | Aplicar for applying settings vs applying for something: one key for both | Separate keys | "Aplicar" is fine for settings. For applying for a job or program, see ESES-04 and the es-419 note below. |
| ES-13 | Plural | 1.000.000 archivos | 1.000.000 de archivos | `many` category needs "de". |
| ES-14 | Consistency | ordenador and computadora, correo and email in the same locale | One term per locale | Regional vocabulary must not mix. |

## 5. Market-specific mistakes

### es-ES

| ID | Avoid | Prefer | Rule |
|---|---|---|---|
| ESES-01 | Remover de la lista | Quitar de la lista | In es-ES, "remover" for UI "remove" reads as an anglicism; its everyday senses are stir and move. |
| ESES-02 | ustedes forms when addressing a group in a Spain-only product with an informal voice | vosotros forms, if the brand addresses groups informally | es-ES plural address. |
| ESES-03 | Simple past in just-completed toasts (No se pudieron guardar) where the rest of es-ES copy uses the present perfect | No se han podido guardar los cambios. | Consistency with the market tendency. |
| ESES-04 | Aplicar a una beca / un puesto | Solicitar / Presentar la candidatura | The DLE marks "aplicar" in this sense as an Americanism. [S27] |

### es-419

| ID | Avoid | Prefer | Rule |
|---|---|---|---|
| ES419-01 | Spain-only vocabulary: ordenador, móvil, vale, coger, fichero, pinchar (to click) | computadora, celular, de acuerdo or OK, tomar, archivo, hacer clic | "coger" is vulgar in several Latin American countries. |
| ES419-02 | vosotros forms (podéis, guardad) | ustedes forms (pueden, guarden) | |
| ES419-03 | One country's number format hard-coded for all of Latin America | Locale formatter by country | es-MX 12,345.67 vs es-AR 12.345,67. [S18] |
| ES419-04 | Voseo (vos podés) in neutral es-419 | tú (puedes) | Voseo belongs to country variants. |

es-419 note: "aplicar a" for applying for a job, grant or program is accepted in Latin America (DLE, Am.); "postularse" is also common. [S27]

Regional term table: `pairs.md`, section es-ES and es-419.

## 6. Worked examples

| Meaning | EN | es-ES (tú) | es-419 (tú) |
|---|---|---|---|
| In progress | Saving changes. | Guardando los cambios. | Guardando los cambios. |
| Done | Changes saved. | Cambios guardados. | Cambios guardados. |
| Failed | Couldn't save changes. | No se han podido guardar los cambios. | No se pudieron guardar los cambios. |
| No permission | You don't have permission to edit this file. | No tienes permiso para editar este archivo. | No tienes permiso para editar este archivo. |
| Not created yet | No projects yet. | Aún no hay proyectos. | Aún no hay proyectos. |
| Missing input | Enter a project name. | Introduce un nombre para el proyecto. | Ingresa un nombre para el proyecto. |
| No results | No results found. | No se han encontrado resultados. | No se encontraron resultados. |
| Confirmation | Delete this file? | ¿Eliminar este archivo? | ¿Eliminar este archivo? |

| Scenario | Title | Body | Primary | Secondary |
|---|---|---|---|---|
| Trash, restorable | ¿Mover el archivo a la papelera? | Puedes restaurarlo desde la papelera. | Mover a la papelera | Cancelar |
| Permanent | ¿Eliminar el archivo de forma permanente? | Los archivos eliminados no se pueden recuperar. | Eliminar de forma permanente | Cancelar |

ICU plural example:

```
{count, plural,
  one {# archivo seleccionado}
  many {# de archivos seleccionados}
  other {# archivos seleccionados}
}
```

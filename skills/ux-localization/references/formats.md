# Formats: numbers, dates, times, currency, lists, plurals

Generated on 2026-10-24 with Node.js `Intl` (ICU 78.3, CLDR 48). [S18] Rerun before relying on exact characters; locale data changes between CLDR releases.

Main rule: format at runtime with the platform's locale formatter (`Intl`, ICU, `NumberFormatter`, `DateFormatter`). Do not hard-code separators or date order into strings. Translators should place a placeholder (`{amount}`, `{date}`), not a formatted value.

Changing the display language does not change the time zone, the currency, or the amount. Keep those as separate settings.

## Numbers and percent

| Locale | 1234 | 12345.67 | 50% | Notes |
|---|---|---|---|---|
| en-US | 1,234 | 12,345.67 | 50% | |
| en-GB | 1,234 | 12,345.67 | 50% | |
| fr-FR | 1 234 | 12 345,67 | 50 % | Group separator is U+202F (narrow no-break space); space before % is U+00A0 |
| de-DE | 1.234 | 12.345,67 | 50 % | Space before % is a no-break space |
| es-ES | 1234 | 12.345,67 | 50 % | No group separator for 4-digit numbers (CLDR minimum grouping). The Diccionario panhispánico de dudas also writes 4-digit numbers without a separator. [S17] |
| es-419 | 1,234 | 12,345.67 | 50% | CLDR es-419 follows Mexico-style separators |
| ko-KR | 1,234 | 12,345.67 | 50% | |
| ja-JP | 1,234 | 12,345.67 | 50% | |
| zh-Hans-CN | 1,234 | 12,345.67 | 50% | |
| zh-Hant-TW | 1,234 | 12,345.67 | 50% | |

**es-419 is a language variant, not one number format.** In CLDR, es-AR, es-CO and es-CL format 12345.67 as `12.345,67`, while es-MX and es-US use `12,345.67`. Format numbers by the user's region (es-AR, es-MX), even when the text is shared es-419. [S18]

Compact numbers group differently. 12,345 in compact notation: en-US `12K`, de-DE `12.345` (no abbreviation for thousands in the short form), ko-KR `1.2만`, ja-JP `1.2万`, zh-Hans-CN `1.2万`. Korean, Japanese and Chinese group by 10,000. Never translate "12K" by hand; format the number. [S18]

## Currency (1234.50 in the local currency)

| Locale | Output | Notes |
|---|---|---|
| en-US, USD | $1,234.50 | |
| en-GB, GBP | £1,234.50 | |
| fr-FR, EUR | 1 234,50 € | Symbol after the number, no-break space |
| de-DE, EUR | 1.234,50 € | |
| es-ES, EUR | 1234,50 € | |
| es-MX, MXN | $1,234.50 | `$` is also used for USD; ambiguous in cross-border products |
| es-419, USD | USD 1,234.50 | |
| ko-KR, KRW | ₩1,235 | KRW has no minor unit: the formatter rounds |
| ja-JP, JPY | ￥1,235 | JPY has no minor unit: the formatter rounds |
| zh-Hans-CN, CNY | ¥1,234.50 | |
| zh-Hant-TW, TWD | $1,234.50 | Default symbol is a bare `$`. Use `currencyDisplay: "code"` (TWD 1,234.50) or show NT$ when another dollar currency could be meant |

- Never convert or round amounts during translation. Rounding of KRW and JPY above is the formatter's behavior for a currency without decimals; prices must be authored in that currency.
- When the symbol alone is ambiguous, show the ISO code (USD, MXN, TWD, KRW, JPY, CNY, EUR, GBP) according to a product rule.
- Tax inclusion, billing cycle, and what is charged after a free trial come from the actual policy. State them as separate facts.

## Dates and times (2026-10-24, 14:30 UTC)

| Locale | Short date | Long date | Short time |
|---|---|---|---|
| en-US | 10/24/26 | October 24, 2026 | 2:30 PM |
| en-GB | 24/10/2026 | 24 October 2026 | 14:30 |
| fr-FR | 24/10/2026 | 24 octobre 2026 | 14:30 |
| de-DE | 24.10.26 | 24. Oktober 2026 | 14:30 |
| es-ES | 24/10/26 | 24 de octubre de 2026 | 14:30 |
| es-419 | 24/10/26 | 24 de octubre de 2026 | 2:30 p.m. |
| ko-KR | 26. 10. 24. | 2026년 10월 24일 | 오후 2:30 |
| ja-JP | 2026/10/24 | 2026年10月24日 | 14:30 |
| zh-Hans-CN | 2026/10/24 | 2026年10月24日 | 14:30 |
| zh-Hant-TW | 2026/10/24 | 2026年10月24日 | 下午2:30 |

- `03/04` means March 4 in en-US and 3 April in en-GB, fr, de, es. Use a locale formatter or a long, unambiguous form.
- Month and weekday names are lowercase in French and Spanish ("24 octobre", "sábado"), capitalized in German and English.
- Keep the real time zone for renewal times and deadlines; state it when users could be in several zones.
- Relative expressions ("tomorrow", "next month") need a known current time and user time zone. Format them with a relative time formatter when possible (yesterday: hier, gestern, ayer, 어제, 昨日, 昨天).

## Lists ("A, B, C")

| Locale | Output |
|---|---|
| en-US | A, B, and C |
| en-GB | A, B and C |
| fr-FR | A, B et C |
| de-DE | A, B und C |
| es-ES, es-419 | A, B y C |
| ko-KR | A, B 및 C |
| ja-JP | A、B、C |
| zh-Hans-CN, zh-Hant-TW | A、B和C |

The serial (Oxford) comma differs between the en-US and en-GB CLDR data. In UI copy written by hand it is a product style setting; follow the product's style guide in both. Use a list formatter for dynamic lists instead of joining with commas.

Spanish: "y" becomes "e" before a word starting with an /i/ sound ("Diseño e ilustración"), and "o" becomes "u" before an /o/ sound. ICU's list formatter handles this for dynamic lists (checked: "Diseño e ilustración", "siete u ocho", "Agua y hielo"); hand-written strings must do it themselves.

## Plural categories (cardinal)

| Locale | Categories | 0 | 1 | 1.5 | 2 | 1000000 |
|---|---|---|---|---|---|---|
| en-US, en-GB | one, other | other | one | other | other | other |
| fr-FR | one, many, other | one | one | one | other | many |
| de-DE | one, other | other | one | other | other | other |
| es-ES, es-419 | one, many, other | other | one | other | other | many |
| ko-KR | other | other | other | other | other | other |
| ja-JP | other | other | other | other | other | other |
| zh-Hans-CN, zh-Hant-TW | other | other | other | other | other | other |

- French uses `one` for 0 and for values below 2 ("0 fichier", "1,5 fichier"). Do not write "0 fichiers".
- `many` in French and Spanish covers exact large round numbers, which take "de": "1 000 000 de fichiers" (fr-FR), "1.000.000 de archivos" (es-ES). Always provide the `many` branch for French and Spanish; it is selected only for exact large round numbers, but leaving it out makes those cases wrong. [S6] [S18]
- ICU message example for fr-FR:

```
{count, plural,
  one {# fichier}
  many {# de fichiers}
  other {# fichiers}
}
```

- `other` is always required. Missing locale categories fall back to `other`, which is grammatically wrong in French and Spanish for the cases above.

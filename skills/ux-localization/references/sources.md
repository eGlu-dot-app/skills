# Sources and change log

## What the sources support

Sources back statements about scripts, typography, formats, accessibility and legal labels. They are not the source of the glossary terms or the example translations: those are editorial proposals written for this skill, not extracted from any product's translations or from another style guide. No open-source translation catalog was imported. Before importing outside terms, record source, revision and license (see `universal-rules.md` section 13).

W3C Notes and Drafts are cited as such, not as final standards. Rows marked "review pass" were checked by a separate review agent during this build; the author did not open those pages directly.

| ID | Source | Supports | Checked |
|---|---|---|---|
| S1 | W3C, Approaches to full justification. https://www.w3.org/International/articles/typography/justification | Word spacing differs across Korean, Japanese, Chinese | 2026-10-23 |
| S2 | W3C, Requirements for Japanese Text Layout (Working Group Note). https://www.w3.org/TR/jlreq/ | Japanese line breaking and punctuation | 2026-10-23 |
| S3 | W3C, Requirements for Chinese Text Layout (Group Note Draft). https://www.w3.org/TR/clreq/ | Chinese punctuation, line breaking, regional practice | 2026-10-23 |
| S4 | Unicode, Chinese and Japanese FAQ. https://unicode.org/faq/han_cjk.html | Regional glyph differences for the same code point; language tagging | 2026-10-23 |
| S5 | W3C, Requirements for Hangul Text Layout and Typography (Group Note Draft). https://www.w3.org/TR/klreq/ | Korean text layout | 2026-10-23 |
| S6 | Unicode CLDR, Language Plural Rules. https://unicode.org/cldr/charts/49/supplemental/language_plural_rules.html | Plural categories per language | 2026-10-24 |
| S7 | W3C WAI, Understanding SC 2.5.3 Label in Name. https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html | Accessible name contains the visible label | 2026-10-24 |
| S8 | W3C WAI, Understanding SC 3.3.1 Error Identification. https://www.w3.org/WAI/WCAG22/Understanding/error-identification | Errors identified in text, not color alone | 2026-10-24 |
| S9 | W3C, UI Events (Working Draft). https://www.w3.org/TR/uievents/ | Composition events for IME input | 2026-10-24 |
| S10 | W3C Internationalization, Language tags in HTML and XML. https://www.w3.org/International/articles/language-tags/index.var | Use region and script subtags only when needed; en-GB, es-419, zh-Hans, zh-Hant examples | 2026-10-24 |
| S11 | Office québécois de la langue française, Espacement avant et après les signes de ponctuation et les symboles. https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles | Quebec usage: no space before ; ! ?; no-break spaces inside « » | 2026-10-24 |
| S12 | Gérald Purnelle, Règles et usages de typographie française (Université de Liège syllabus). https://orbi.uliege.be/bitstream/2268/298446/1/R%C3%A8glesTypographiquesSyllabus-Purnelle.pdf | European French: narrow no-break space before ? ! ;, no-break space before :, no-break spaces inside « » | 2026-10-24 |
| S13 | Académie française, Questions de langue: accentuation des majuscules. https://dictionnaire-academie.fr/article/QDL005 | Accents on capital letters are part of correct spelling | 2026-10-24 |
| S14 | Bürgerliches Gesetzbuch § 312k. https://www.gesetze-im-internet.de/bgb/__312k.html | Cancellation button labels "Verträge hier kündigen" and "jetzt kündigen", each "or an equivalent unambiguous wording" | 2026-10-24 |
| S15 | Bürgerliches Gesetzbuch § 312j. https://www.gesetze-im-internet.de/bgb/__312j.html | Order button "zahlungspflichtig bestellen" or an equivalent unambiguous wording | 2026-10-24 |
| S16 | Seban Avocats, La résiliation des contrats conclus par voie électronique en trois clics. https://www.seban-associes.avocat.fr/la-resiliation-des-contrats-conclus-par-voie-electronique-en-trois-clics/ | Secondary summary of the 2023 French decree; example label "résilier votre contrat" | 2026-10-24 |
| S17 | Universidad de Piura, Castellano actual: Uso de punto en los números. https://www.udep.edu.pe/castellanoactual/uso-de-punto-en-los-numeros/ | Summary of RAE guidance: 4-digit numbers without a separator; comma or point as decimal marker | 2026-10-24 |
| S18 | Node.js Intl output, ICU 78.3 with CLDR 48, generated 2026-10-24 | All values in `formats.md`; plural categories in the checker. Note: S6 links the CLDR 49 chart, while this ICU build carries CLDR 48 data; the checker follows the ICU output | 2026-10-24 |
| S19 | Directive 2011/83/EU, Article 8 (legislation.gov.uk copy). https://www.legislation.gov.uk/eudr/2011/83/article/8 | Order button labeled only "order with obligation to pay" or a corresponding unambiguous formulation | 2026-10-24 |
| S21 | Directive 2011/83/EU, official French and Spanish texts on EUR-Lex. https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32011L0083 and https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32011L0083 | Art. 8(2) wording: « commande avec obligation de paiement », «pedido con obligación de pago» | 2026-10-24 (review pass) |
| S22 | Institut national de la consommation, summary of CJEU C-249/21 (Fuhrmann-2, 7 April 2022). https://www.inc-conso.fr/content/la-cjue-se-prononce-sur-la-reglementation-de-la-vente-distance-sur-internet | Only the button wording counts; alternatives must leave no doubt about the obligation to pay | 2026-10-24 (review pass) |
| S23 | Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013, reg. 14. https://www.legislation.gov.uk/uksi/2013/3134/regulation/14 | UK order-button wording "order with obligation to pay" or a corresponding unambiguous formulation | 2026-10-24 (review pass) |
| S24 | Ministry of Education (Taiwan), Revised Mandarin Chinese Dictionary, entry 了解. https://dict.revised.moe.edu.tw/dictView.jsp?ID=63145 | 了解 is the headword; 瞭解 is listed as a variant | 2026-10-24 (review pass) |
| S25 | W3C WAI, Understanding SC 2.4.4 Link Purpose (In Context). https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html | Link purpose may come from the surrounding context at level AA | 2026-10-24 (review pass) |
| S26 | Institut national de la consommation, résiliation en quelques clics, https://www.inc-conso.fr/content/vous-pouvez-resilier-votre-contrat-dabonnement-en-quelques-clics ; Juritravail on art. D. 215-1, https://www.juritravail.com/Actualite/resiliation-des-contrats-par-voie-electronique-nouvelle-fonctionnalite/Id/376543 | Termination function presented under « résilier votre contrat » or an equivalent unambiguous wording (secondary sources; article text not read) | 2026-10-24 (review pass) |
| S27 | Real Academia Española, Diccionario de la lengua española: aplicar, asistir, remover, eventualmente, revertir. https://dle.rae.es/aplicar (and the same path for each word) | "aplicar" for applying for something is marked as an Americanism; senses of asistir, remover, eventualmente; revertir listed as intransitive | 2026-10-24 (review pass) |
| S28 | Chromium (Chrome UI strings), generated_resources and components_strings .grd/.grdp with .xtb translations, main branch f320236d579b, fetched 2026-10-24. https://github.com/chromium/chromium (BSD-3-Clause) | Current Chrome terms per locale; message IDs computed from the English source | 2026-10-24 |
| S29 | Android Open Source Project mirror: packages/apps/Settings, frameworks/base core and SystemUI strings.xml, main branch (settings 7c598253ff60, frameworks/base 1cdfff555f4a; last mirror update March 2025). https://github.com/aosp-mirror (Apache-2.0) | Android system terms per locale (es-US resources used for es-419) | 2026-10-24 |
| S30 | Mozilla Firefox: firefox-l10n b5ea1c1e2960 and firefox en-US source 4190c69a7dd5, fetched 2026-10-24. https://github.com/mozilla-l10n/firefox-l10n and https://github.com/mozilla-firefox/firefox (MPL-2.0) | Current Firefox terms per locale (es-MX used for es-419) | 2026-10-24 |
| S31 | Apple, Mac용 Safari 사용 설명서. https://support.apple.com/ko-kr/guide/safari/ibrw8fa63b51/mac | Safari Korean guide uses 북마크 for bookmarks and 즐겨찾기 for a separate Favorites feature | 2026-10-24 |
| S32 | Microsoft Support, Import favorites in Microsoft Edge. https://support.microsoft.com/en-us/help/4028355/microsoft-edge-import-favorites | Edge names the feature Favorites in English | 2026-10-24 |

Not used as evidence: vendor style guides (Microsoft, Apple, Google) were not opened, so no style rule here is attributed to them. Shipped product strings (S28 to S30) are used only as evidence of which term a product shows; the glossary does not copy their catalogs. `platform-evidence.csv` quotes short UI terms with counts for traceability. Statements marked "[not verified]" or "low confidence" in the reference files need checking before they become product rules.

## Known gaps

- No native-speaker review yet for any locale.
- Platform labels (OS settings, trash, notifications) not verified against current OS builds.
- National transpositions of the EU order-button rule (France, Spain) not checked; the directive's official language versions are used as the baseline.
- French art. D. 215-1 text not read on Légifrance; the termination label comes from two secondary summaries.
- Taiwan favorites term and French upload term are low confidence.
- Out of scope: fr-CA, fr-BE, fr-CH, de-AT, de-CH, es-US and country variants of es-419, zh-HK, zh-MO, zh-SG, en-AU and others.

## Change log

- 0.1, 2026-10-23: CJK reference: 24 terms, 29 error types, language characteristics, sentence examples.
- 0.2, 2026-10-24: CJK reference: 32 more terms, 22 more error types, state patterns, AI actions, numbers and variables, IME and accessibility checks, skill design proposals.
- 1.1, 2026-10-24: Korean default register changed to 합니다체 (requests -해 주십시오); KO-27 and a checker register check added. Glossary grew from 85 to 198 concepts. Every concept was checked against Chrome, Android and Firefox translations; terms that differed from platform consensus were replaced (for example ko 미리보기, 로드 중, 선택사항; de Weitere Informationen, Filter; es-ES Hecho; ja 詳細, 期限切れ). Added `evidence` column, `platform-evidence.csv`, the term-selection rule, and ALL-19.
- 1.0, 2026-10-24: Packaged as the `ux-localization` skill. A test run and a separate fact-check pass corrected the German § 312k scope and wording alternative, EU and UK order-button wording, French legal termination label, several Spanish false-friend claims, the Taiwan 了解/瞭解 claim, and WCAG link-purpose wording, and added a `variants` column, three concepts, a toast undo pattern, source-issue handling and checker improvements. Added en-US, en-GB, fr-FR, de-DE, es-ES, es-419. Glossary moved to CSV with 82 concepts across 10 locales. Added direction-specific mistakes (`pairs.md`), formats generated from ICU, legal labels for German and EU order and cancellation buttons, `avoid-terms.csv`, and `lint_strings.py`. CJK common mistakes CJK-01 to CJK-10 renamed ALL-01 to ALL-10 because they apply to every locale.

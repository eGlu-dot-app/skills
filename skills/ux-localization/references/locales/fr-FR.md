# fr-FR: French (France)

All terms and examples are `proposed` and need native review.

## Contents

1. Scope and register
2. Language characteristics and UX implications
3. Typography and punctuation
4. Common mistakes (FR-01 to FR-18)
5. Worked examples

## 1. Scope and register

- Market: France. fr-CA (Quebec), fr-BE and fr-CH differ in vocabulary and punctuation spacing; do not apply this file to them without review. Example: Quebec usage prefers no space before ; ! ? [S11], while European French typography uses one [S12].
- Proposed default: **vous**. Some consumer brands use **tu**; that is a brand decision. Never mix the two in one product.
- Buttons, menu items and commands: **infinitive** (Enregistrer, Annuler, Supprimer, Se connecter).
- Instructions addressed to the user: imperative with vous (Saisissez un nom de projet.) or the infinitive in some product styles. Choose one per text type and keep it.
- "Veuillez + infinitive" is formal and heavy for short UI text; use it only where the brand tone is formal.

## 2. Language characteristics and UX implications

- **Grammatical gender and agreement.** Adjectives and past participles agree in gender and number: "Modifications enregistrées", "Fichier enregistré", "Projets supprimés". A bare status label (Enregistré) agrees with the noun it describes; reusing one label for objects of different gender produces errors.
- **Elision.** le/la → l', de → d', que → qu' before a vowel or mute h. Variables break this: "le fichier de {name}" becomes wrong for "Anna" (d'Anna). Rephrase so no article or preposition governs the variable ("Propriétaire : {name}"), or handle the cases in the message.
- **Agreement with variables.** "{name} a été ajouté" needs ajouté / ajoutée / ajoutés. Use ICU `select` on gender only if the product knows it; otherwise rephrase ("{name} fait maintenant partie de l'espace de travail").
- **Plural of zero.** CLDR and most grammars use the singular for 0 and 1 ("0 fichier"); the plural after a numeric 0 is also attested, so treat it as a consistency point. CLDR also has a `many` category for exact millions ("1 000 000 de fichiers"). See `formats.md`.
- **Capitalization.** Sentence case for titles, buttons and menus: only the first word and proper nouns take a capital. Days, months and language names are lowercase.
- **Accents on capitals are kept** (É, À, Ê). The Académie française considers them part of correct spelling. [S13] Keep them in all-caps styles too.
- **Text length.** French UI strings are often longer than English. Test in the real component.
- **Possessives.** "Votre" is natural more often than "your" is in Korean or Japanese, but it can still be dropped when obvious ("Mot de passe" as a field label, not "Votre mot de passe").
- **Inclusive writing** (for example the point médian: connecté·e) is debated in France. Treat it as a brand policy. A neutral rewrite often avoids the issue: "Connexion réussie" instead of "Vous êtes connecté".
- **Anglicisms.** Some are standard in UI (cliquer, e-mail, cookie). For email, France's official terminology recommends "courriel", while "e-mail" is widespread; pick one and use "adresse e-mail" or "adresse courriel" consistently.

## 3. Typography and punctuation

European French typography [S12]:

| Mark | Space before | Character |
|---|---|---|
| ; ! ? | narrow no-break space | U+202F |
| : | no-break space | U+00A0 |
| « | regular space before, no-break space after | U+00A0 after |
| » | no-break space before | U+00A0 before |

- In UI strings the space must be **non-breaking**, so that the mark never wraps to the start of a line. Whether to use U+202F or U+00A0 before ; ! ? is a product rule; some fonts and platforms render U+202F poorly, so test it.
- Do not insert spaces inside URLs, times (14:30), code, or ratios.
- Quotation marks: « … » with no-break spaces inside. Nested quotes may use “ ”.
- Apostrophe: typographic ’ or ASCII ' is a product setting. Keep one. Android XML needs an ASCII apostrophe escaped (\'). In ICU or Java MessageFormat an apostrophe can start a quoted literal; write '' or use ’ there.
- Numbers: 1 234,56 with U+202F as the group separator; 50 % and 12,50 € with U+00A0. Use the formatter (`formats.md`).
- Ellipsis: … (one character).
- No final period on buttons, menu items, titles or standalone labels.

## 4. Common mistakes

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| FR-01 | Casing | Créer Un Nouveau Projet | Créer un projet | No English title case. |
| FR-02 | Punctuation | Supprimer ce fichier? / Attention: | Supprimer ce fichier ? / Attention : | No-break space before ? ! ; : (European French). |
| FR-03 | Register | Enregistrez as a button next to Annuler | Enregistrer | Buttons use the infinitive; do not mix forms within one element type. |
| FR-04 | Register | vous in settings, tu in onboarding | One address form | Brand decision; keep it everywhere. |
| FR-05 | Plural | 0 fichiers mixed with 1 fichier rules | 0 fichier | CLDR and most grammars use the singular for 0; keep it consistent with the plural rule. |
| FR-06 | Variables | Le fichier de {name} | Fichier de {name}, or rephrase | Elision (d'Anna) and articles break with variables. |
| FR-07 | Variables | {name} a été ajouté | {name} fait maintenant partie de l'espace de travail | Gender agreement unknown; rephrase or use `select`. |
| FR-08 | False friend | Ce format n'est pas supporté. | Ce format n'est pas pris en charge. | "supporter" means to tolerate. |
| FR-09 | False friend | librairie (software library), éventuellement (eventually), actuellement (actually) | bibliothèque, à terme or finalement, en fait | Each French word means something else: bookshop, possibly, currently. Also check "contrôler", which often means "to check" rather than "to control"; use vérifier or gérer by meaning. |
| FR-10 | Collision | Annuler for Cancel and Undo on the same screen | Annuler la suppression (Undo), Annuler (Cancel) | See glossary-notes `cancel-undo-restore`. |
| FR-11 | Spelling | ECHEC DE L'ENVOI | ÉCHEC DE L'ENVOI | Keep accents on capitals. [S13] |
| FR-12 | Punctuation | "Brouillon" | « Brouillon » | French quotation marks with no-break spaces. |
| FR-13 | Translationese | Vos modifications ont été enregistrées avec succès. | Modifications enregistrées. | Cut "avec succès" and stacked passive in success toasts. |
| FR-14 | Register | Cher utilisateur, | Bonjour {firstName}, or no salutation | English-style generic salutations sound stiff and gendered. |
| FR-15 | Collision | Importer for both Upload and Import | Importer un fichier / Importer des contacts, or a separate term for one | See glossary-notes `upload-import`. |
| FR-16 | Term, legal | Annuler l'abonnement on the online termination function | Résilier votre contrat (or an unambiguous equivalent approved by legal); Résilier l'abonnement elsewhere | "Résilier" is the contract term, and the termination function has a reported statutory label (glossary-notes `billing`). |
| FR-17 | Consistency | mail, e-mail, email, courriel in one product | One form | Choose once. |
| FR-18 | Grammar | Bienvenu ! (to all users) | Bienvenue ! | "Bienvenue" is the invariable noun form and works for everyone. |

## 5. Worked examples

U+202F is shown as a normal space below; use a non-breaking space in real strings.

| Meaning | EN | fr-FR |
|---|---|---|
| In progress | Saving changes. | Enregistrement des modifications en cours. |
| Done | Changes saved. | Modifications enregistrées. |
| Failed | Couldn't save changes. | Impossible d'enregistrer les modifications. |
| No permission | You don't have permission to edit this file. | Vous n'avez pas l'autorisation de modifier ce fichier. |
| Not created yet | No projects yet. | Aucun projet pour le moment. |
| Missing input | Enter a project name. | Saisissez un nom de projet. |
| No results | No results found. | Aucun résultat trouvé. |
| Confirmation | Delete this file? | Supprimer ce fichier ? |

| Scenario | Title | Body | Primary | Secondary |
|---|---|---|---|---|
| Trash, restorable | Placer le fichier dans la corbeille ? | Vous pourrez le restaurer depuis la corbeille. | Placer dans la corbeille | Annuler |
| Permanent | Supprimer définitivement le fichier ? | Les fichiers supprimés ne peuvent pas être récupérés. | Supprimer définitivement | Annuler |

ICU plural example:

```
{count, plural,
  one {# fichier sélectionné}
  many {# de fichiers sélectionnés}
  other {# fichiers sélectionnés}
}
```

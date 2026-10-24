# de-DE: German (Germany)

All terms and examples are `proposed` and need native review.

## Contents

1. Scope and register
2. Language characteristics and UX implications
3. Typography and punctuation
4. Legal labels
5. Common mistakes (DE-01 to DE-16)
6. Worked examples

## 1. Scope and register

- Market: Germany. de-AT (for example "Jänner" for January) and de-CH (no ß, « » quotes, apostrophe as the number group separator) differ; do not apply this file to them without review.
- Proposed default: **Sie**. Many consumer brands use **du**; that is a brand decision. Never mix the two in one product.
- Sie, Ihr, Ihnen (formal) are always capitalized. du, dein, dich are lowercase in UI text.
- Buttons and menu items: **infinitive** (Speichern, Abbrechen, Löschen, Hochladen).
- Instructions: imperative. Sie form: "Geben Sie einen Projektnamen ein." du form: "Gib einen Projektnamen ein."

## 2. Language characteristics and UX implications

- **All nouns are capitalized**, including nominalized verbs (das Speichern). Other words follow sentence case. There is no title case.
- **Compounds are one word or hyphenated, never spaced.** Projektname, Speicherplatz, E-Mail-Adresse, Figma-Datei, Upload-Limit. A space inside a compound is a spelling error (DE-03).
- **Long words.** Compounds produce long unbreakable words. Allow hyphenation with `lang="de"` and `hyphens: auto`, or add soft hyphens in fixed-width components; otherwise choose a shorter term.
- **Verb position and separable verbs.** In declarative main clauses the finite verb is second ("Sie laden die Datei hoch"). In imperatives and yes/no questions, the most common UI forms, it comes first ("Laden Sie die Datei hoch"). In both, the separable prefix goes to the end. In subordinate clauses the verb goes last. Strings concatenated from English-order fragments break this bracket (DE-04).
- **Gender and case.** Articles and adjectives change with gender and case: der Ordner, die Datei, das Projekt; "den Ordner", "dem Projekt". Messages with a variable object need one string per object type, or ICU `select` (DE-05).
- **Passive for system states is natural.** "Wird gespeichert", "Änderungen gespeichert", "Datei wurde gelöscht". Avoid heavy nominal style ("Durchführung der Speicherung").
- **"Bitte"** is fine in instructions where politeness helps; it does not belong on buttons.
- **Ordinary possessives take no apostrophe**: "Annas Projekt". The official rules allow an apostrophe only in limited name constructions. With a variable, rephrase: "Projekt von {name}" (DE-10).
- **Gender-inclusive forms** (Nutzer:innen, Nutzende, Mitglieder) are a brand decision. Neutral nouns (Mitglieder, Personen, Team) avoid the issue in many strings.
- **Text length.** German UI strings are often noticeably longer than English. Test in real widths.

## 3. Typography and punctuation

- Quotation marks: „…“ (low-high) in Germany. (Switzerland uses « ».)
- Numbers: 1.234,56; percent and currency with a space: 50 %, 12,50 €. Use the formatter (`formats.md`).
- Dates: 24.10.2026 or 24. Oktober 2026. Times: 14:30 or 14:30 Uhr.
- No final period on buttons, menu items, titles or standalone labels.
- Ellipsis style on loading states is a product setting.

## 4. Legal labels

Each statute names a wording and also allows "an equivalent unambiguous wording". The statutory wording is the safe default; a different or shorter label is a legal decision, not a translation choice. Confirm with legal for each product.

| Situation | Label | Source |
|---|---|---|
| Cancellation button for consumer contracts concluded through a website that create a paid continuing obligation (subscriptions and similar; financial services excluded) | Verträge hier kündigen, or an equivalent unambiguous wording | BGB § 312k [S14] |
| Confirmation button on the cancellation page | jetzt kündigen, or an equivalent unambiguous wording | BGB § 312k [S14] |
| Final order button that creates a payment obligation | zahlungspflichtig bestellen, or an equivalent unambiguous wording | BGB § 312j(3) [S15] |

If a length limit cannot fit the statutory wording, report it under Needs product check with the statutory label, the proposed short label (for example "Abo kündigen"), and the question for legal. Do not silently shorten.

Labels without a payment reference ("Weiter", "Bestellung abschließen") on the final order step are high risk: the CJEU held that only the words on the button count, and that alternatives must leave no doubt about the obligation to pay (C-249/21). [S22]

## 5. Common mistakes

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| DE-01 | Register | Sie in settings, du in onboarding | One address form | Brand decision; keep it everywhere. |
| DE-02 | Spelling | sie haben keine Berechtigung / Ihre and ihre mixed | Sie haben keine Berechtigung | Formal Sie and Ihr are capitalized. |
| DE-03 | Spelling | Projekt Name, Email Adresse, E-Mail Adresse | Projektname, E-Mail-Adresse | Compounds are closed or hyphenated, never spaced. |
| DE-04 | Grammar | "Laden Sie" + "{file}" + "hoch" assembled from fragments | One complete string: "Laden Sie {file} hoch." | Separable verbs and verb position need full strings. |
| DE-05 | Variables | {object} wurde gelöscht. | Die Datei wurde gelöscht. / Der Ordner wurde gelöscht. | Gender and case differ per object. |
| DE-06 | Meaning | Abbrechen for Cancel subscription; Kündigen for Cancel upload | Abbrechen (operation), Kündigen (contract), Stornieren (order, booking) | English Cancel splits into three verbs. |
| DE-07 | Style | Bitte speichern / Bitte klicken Sie hier | Speichern / Name the destination | No "Bitte" on buttons; no "hier" links. |
| DE-08 | Translationese | Die Speicherung Ihrer Änderungen wurde erfolgreich durchgeführt. | Änderungen gespeichert. | Cut nominal style and "erfolgreich". |
| DE-09 | Casing | Neues Projekt Erstellen | Neues Projekt erstellen | Only nouns take capitals. |
| DE-10 | Spelling | Anna's Projekt / {name}'s Projekt | Annas Projekt / Projekt von {name} | No apostrophe in ordinary possessives. |
| DE-11 | False friend | actual → aktuell; eventually → eventuell | tatsächlich; schließlich or irgendwann | aktuell means current, eventuell means possibly. Also check "kontrollieren": it often means check or monitor; for control in the sense of steer or manage, prefer steuern or verwalten. |
| DE-12 | Punctuation | "Entwurf" | „Entwurf“ | German quotation marks. |
| DE-13 | Layout | A 30-character compound that overflows a button | Hyphenation, a shorter term, or a different layout | Test real widths. |
| DE-14 | Legal | "Abo beenden" or "Abonnement verwalten" for the § 312k button | Verträge hier kündigen (or an unambiguous equivalent approved by legal) | "beenden" and "verwalten" do not clearly say the contract is terminated. |
| DE-15 | Spelling | Email, eMail, E-mail | E-Mail | Standard spelling. |
| DE-16 | Meaning | Freigeben and Teilen used for the same action | Teilen (social or link share), Freigeben (grant access) | Pick by what the action does. |

## 6. Worked examples

| Meaning | EN | de-DE (Sie) | de-DE (du) |
|---|---|---|---|
| In progress | Saving changes. | Änderungen werden gespeichert. | same |
| Done | Changes saved. | Änderungen gespeichert. | same |
| Failed | Couldn't save changes. | Änderungen konnten nicht gespeichert werden. | same |
| No permission | You don't have permission to edit this file. | Sie haben keine Berechtigung, diese Datei zu bearbeiten. | Du hast keine Berechtigung, diese Datei zu bearbeiten. |
| Not created yet | No projects yet. | Noch keine Projekte vorhanden. | same |
| Missing input | Enter a project name. | Geben Sie einen Projektnamen ein. | Gib einen Projektnamen ein. |
| No results | No results found. | Keine Ergebnisse gefunden. | same |
| Confirmation | Delete this file? | Diese Datei löschen? | same |

| Scenario | Title | Body (Sie) | Primary | Secondary |
|---|---|---|---|---|
| Trash, restorable | Datei in den Papierkorb verschieben? | Sie können sie aus dem Papierkorb wiederherstellen. | In den Papierkorb verschieben | Abbrechen |
| Permanent | Datei endgültig löschen? | Gelöschte Dateien können nicht wiederhergestellt werden. | Endgültig löschen | Abbrechen |

ICU plural example:

```
{count, plural,
  one {# Datei ausgewählt}
  other {# Dateien ausgewählt}
}
```

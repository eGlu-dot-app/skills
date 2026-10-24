# Glossary notes

Context limits, allowed variants and collisions for the concepts in `glossary.csv`. Each heading matches a value in the `notes` column. All entries are `proposed`.

## How terms are chosen

Prefer the term that people already see in the major products of the market over a literal translation of the English word. Users learn UI vocabulary from their browser and operating system; a literal translation that differs from it reads as a different feature.

- Every concept was checked on 2026-10-24 against the shipped translations of Chrome (Chromium, current main), Android (AOSP mirror, last updated March 2025) and Firefox (current main). Raw counts per locale are in `platform-evidence.csv`. [S28] [S29] [S30]
- The `evidence` column says how many locales match a platform term, and lists the differences.
- Decision rule: when Google (Chrome, Android) and Mozilla (Firefox) agree, use their term. When they differ, use Google's term, unless it collides with another concept in this glossary or reflects a narrower feature name; then keep the other term and record why in `variants` or here.
- A platform term does not override meaning. Where Google uses one word for two concepts this skill keeps apart (Korean 삭제 for both Delete and Remove), the glossary keeps the split and records the platform term.
- Microsoft and Apple translations were not extracted in bulk. Single checks are cited where used.
- Concepts marked "no platform match" (SaaS, billing and AI terms) are editorial proposals; check them against the product's own UI and competitors before shipping.

A cell in the glossary is the preferred term for the concept as defined in the `definition` column. Inside a sentence, adjust articles, particles, case, gender, agreement and word order as the target grammar requires. If the product already has an approved term, the product term wins.

## Contents

How terms are chosen · auth · account · settings · workspace · en-gb-spelling · file-folder · trash · favorites · roles · notifications · save-apply · cancel-undo-restore · delete-remove · copy-duplicate · share · publish · upload-import · status · navigation · learn-more · fields · billing · ai · browser · system-ui · common-actions · messaging

## auth

- Pick one sign-in pair per product and keep it: Sign in / Sign out, or Log in / Log out. Do not mix "Log in" with "Sign out".
- en: "Sign up" and "Log in" are verbs (two words). "Signup" and "login" are nouns or adjectives ("login page").
- ja: ログイン and サインイン are both valid. Choose one per product (JA-04).
- zh-Hans-CN: 登录, not 登陆 (ZHCN-01). zh-Hant-TW: 登入; 登錄 means "register or record" in other contexts (ZHTW-03).
- Cross-CJK trap: zh 登录 means sign in, but ja 登録 and ko 등록 mean registration. See `pairs.md`, section CJK shared characters.
- fr: "Se connecter" and "Se déconnecter" are standard. "Créer un compte" is a common alternative to "S'inscrire" for sign up.

## account

- The login account, not a bank account.
- zh-Hans-CN: 账户 is also possible depending on product; do not treat 账号 as the only correct form. Do not mix with financial meanings.
- es: "Cuenta" covers both login and bank account; add context ("cuenta bancaria") only for the financial meaning.

## settings

- The in-product settings screen.
- When the text points to operating system settings, use the platform's own name. Apple platforms use different names from Android or Windows in some languages; for example, Apple uses "Réglages" in French and "Ajustes" in Spanish (Spain), where Android or Windows often use "Paramètres" and "Configuración" or "Ajustes". [Not verified against current OS builds; check the live OS before shipping.]

## workspace

- Confirm whether "Workspace" is the same concept as Team or Project in this product. A product's own named feature takes priority.
- de: many SaaS products keep "Workspace" in German. Choose one and keep it.

## en-gb-spelling

- en-GB here uses -ise spellings (Organisation, customise), which are common in UK consumer products. Oxford spelling (-ize with British vocabulary) is also standard British English. This is a product setting, not a grammar rule. Decide once.

## file-folder

- zh-Hant-TW: 檔案 for file, 資料夾 for folder. Converting 文件夹 character by character to 文件夾 is a localization error for Taiwan (ZHTW-02).
- es-ES: "fichero" also exists in Spain; "archivo" is understood in all markets and is proposed for both.
- ja: フォルダ and フォルダー are both used. Choose per product style; neither is wrong.

## trash

- Place where deleted items wait and can be restored. If items are deleted permanently, do not call the place Trash or Bin.
- en-GB: "Bin" is the British word. If the text names the operating system's trash, use the platform's own label.
- zh: platform names differ (Windows and macOS use different words in both Chinese markets). For an in-product trash, 回收站 (CN) and 垃圾桶 (TW) are proposed. [Platform labels not verified against current OS builds.]
- ja: ゴミ箱 and ごみ箱 both occur; choose one.

## favorites

- en-GB: "Favourites".
- zh-Hant-TW: 我的最愛 is proposed for a favorites list; 收藏 is also common for saved items. Low confidence; native review needed.

## roles

- Owner and Admin are product roles. Do not infer billing or ownership-transfer rights from the name.
- Editor and Viewer label people. For a permission state, write "Can edit" or "Can view" as separate strings.
- Grammatical gender (fr, de, es): Administrateur, Éditeur, Lecteur, Eigentümer, Administrador and Propietario are masculine forms; French "Propriétaire" has one form for both genders (only the article shows gender). For a label next to a person's name, decide a product policy: generic masculine, paired forms, or a neutral rewrite (for example "Accès : propriétaire" or a permission phrase). Do not invent forms that the market does not use. In German, also decide whether to use forms such as "Administrator:in"; this is a brand decision.
- ko: 멤버 is proposed; 구성원 is also natural. Pick one.
- Invite: invitation sends a request; it does not grant access until accepted. Do not translate as "add".

## notifications

- de: Apple platforms use "Mitteilungen" for system notifications; "Benachrichtigungen" is proposed for in-product notifications. [Platform label not verified against current OS builds.]

## save-apply

- Save stores content. Apply makes chosen settings take effect.
- In products that save automatically, do not add a Save action that the product does not have.
- de: "Übernehmen" is the usual dialog button for applying settings. "Anwenden" fits applying a filter, template or effect.

## cancel-undo-restore

Three different results. Never share one key between them.

| Concept | Meaning | Collision to watch |
|---|---|---|
| Cancel | Stop an operation in progress, or close without completing | fr "Annuler" is also Undo |
| Undo | Reverse a completed action | ja キャンセル is Cancel, not Undo (JA-05) |
| Restore | Bring an object or an earlier state back | zh-TW 還原 can absorb Undo, Restore and Reset (ZHTW-06) |

- fr: "Annuler" is standard for both Cancel and Undo. When both can appear on the same screen (for example an Undo toast over a dialog with Cancel), name the object: "Annuler la suppression", "Annuler l'envoi".
- de: English "Cancel" splits into three verbs. "Abbrechen" stops an operation. "Kündigen" ends a contract or subscription. "Stornieren" cancels an order, booking or payment. Status words follow the same split: Abgebrochen, Gekündigt, Storniert.
- en: "canceled" (US) vs "cancelled" (UK).
- es: "Cancelar" covers operation, order and subscription; "Anular" is also used for orders or payments in some products.

## delete-remove

- Delete removes the object. Remove from list removes only the link; the object stays.
- Languages do not map these one to one. ja often uses 削除 for both, so name the target and scope (リストから削除).
- de: "Löschen" deletes; "Entfernen" removes from a list or container.
- es: "Eliminar" deletes; "Quitar" removes from a list. In es-ES, "remover" for UI "remove" reads as an anglicism (its everyday senses are "stir" and "move"); in parts of Latin America "remover" is used for remove, but "quitar" is understood everywhere.
- fr: "Supprimer" deletes; "Retirer" removes from a list.

## copy-duplicate

- Copy goes to the clipboard. Duplicate creates a new object.
- zh-Hant-TW: 複製 can mean both, so Duplicate is proposed as 建立副本. Manage "Copy link" and "Duplicate project" as separate keys.
- ja: 複製 for Duplicate and コピー for Copy keeps the two apart.

## share

- Means giving access or a link. Check which: link sharing, co-ownership, or permission grant.
- zh: 共享 (CN) or 共用 (TW) can fit collaboration features better than 分享.
- de: "Teilen" is the general share action (social, link). For granting file access, many products use "Freigeben". Pick by the action.

## publish

- Moving content to the published state. Check the audience. If it is not visible to everyone outside the workspace, reconsider ja 公開 and similar words that imply public visibility.
- zh-Hant-TW: 發佈 and 發布 both occur; choose one.

## upload-import

- Upload sends a local file. Import converts data from another format or service.
- fr: "Importer" is widely used for upload, which collides with Import. If both appear in one product, keep "Importer" for one and choose another for the other ("Envoyer un fichier", "Ajouter des fichiers"), or always name the object ("Importer un fichier", "Importer des contacts"). "Téléverser" is mainly Quebec usage and uncommon in fr-FR UI. Low confidence on which label French users expect for upload in your product; check the product's existing French UI.

## status

- Saving and Saved: confirm local or server save. Saved does not mean synced to every device.
- Failed and Expired: say what failed or expired, in the same string or right next to it.
- Refresh means reloading the view. Token refresh, data refresh and app update are separate concepts.
- Loading and in-progress statuses: whether to add an ellipsis is a product style setting.
- fr, es: past participles agree with the noun they describe ("Modifications enregistrées", "Cambios guardados"). A bare status label (Enregistré, Guardado) agrees with the implied noun; check the noun before reusing one label for several objects.
- es: "Caducado" is proposed for Expired in both markets (Chrome es and es-419); "Vencido" (cards, documents) and "Expirado" (Firefox) are allowed variants.
- es: "Error" is proposed for the Failed status label; in sentences use "No se pudo…" (es-419) or "No se ha podido…" (es-ES).

## navigation

- Continue and Back move between steps. Done finishes a task. Close dismisses a container without implying anything was completed.
- es-419: "Volver" is common for Back; "Atrás" works in both markets.
- ko: 뒤로 for navigation back; 이전 for the previous step in a numbered flow.

## learn-more

- Prefer a link that names the topic when space allows ("Learn more about billing"). A bare "Learn more" fails WCAG 2.4.4 (AA) unless its sentence, paragraph, list item or table cell identifies the topic, and it always fails 2.4.9 (AAA). [S25]
- zh-Hant-TW: 了解 and 瞭解 both occur in Taiwan (the Ministry of Education dictionary lists 了解 as the headword, with 瞭解 as a variant); choose one per product. [S24] zh-Hans-CN uses 了解.

## fields

- Required and Optional are input field states. Do not use 选填/選填 for paid add-ons or optional features.
- de: "Pflichtfeld" is a common alternative to "Erforderlich" as a field marker.
- fr: "Facultatif" and "Optionnel" both occur; "Facultatif" is proposed.
- en-US uses "ZIP code"; en-GB uses "Postcode". For a multi-country form, "Postal code" is a neutral alternative.
- de: write "E-Mail" with a capital E and a hyphen, and "E-Mail-Adresse" with hyphens.

## billing

- Plan is the paid tier, not a work plan. Do not reuse its translation for "plan" in a project.
- Free trial: say only what is confirmed. Whether a card is required, whether and when charging starts, and the trial length are separate facts from the actual policy.
- Cancel subscription is not a refund and not a payment cancellation. Confirm when access ends, whether renewal stops, and whether money is returned.
- de: ending a subscription is "kündigen". For consumer contracts concluded through a website that create a paid continuing obligation (subscriptions and similar), German law requires a cancellation button labeled only "Verträge hier kündigen" or an equivalent unambiguous wording, and a confirmation button labeled only "jetzt kündigen" or an equivalent unambiguous wording (BGB § 312k; financial services excluded). [S14] The statutory wording is the safe default. A shorter label (for example "Abo kündigen") must still be unambiguous, and legal decides; vague labels such as "Abo beenden" or "Abonnement verwalten" are risky because they do not say the contract is terminated.
- de: the final order button must be labeled only with "zahlungspflichtig bestellen" or an equivalent unambiguous wording (BGB § 312j(3)). [S15]
- EU: the order button must be labeled only with "order with obligation to pay" or a corresponding unambiguous formulation (Directive 2011/83/EU, Art. 8(2)). [S19] The official French and Spanish texts of the directive read "commande avec obligation de paiement" and "pedido con obligación de pago"; the fr-FR and es-ES cells of `action.place_order` use these as the baseline. [S21] National transpositions were not checked. The CJEU held that only the words on the button count, and that an alternative wording must leave no doubt that ordering creates an obligation to pay (C-249/21, Fuhrmann-2, 2022). [S22] Labels without a payment reference ("Weiter", "Place order", "Bestellung abschließen") are high risk; confirm with legal.
- UK: the same requirement and wording are in the Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013, reg. 14(4). [S23] The en-GB cell is "Pay now", a label that names the payment; the statutory wording is the safest option. en-US has no equivalent federal button rule in this reference; the en-US cell stays "Place order".
- es-419: the EU rule does not apply in Latin American markets. The es-419 cell is a natural label ("Realizar pedido"); check local consumer law.
- fr: "Résilier" is the term for ending a contract. Since the 2023 decree, the online termination function in France must be presented under « résilier votre contrat » or an equivalent unambiguous wording, according to two summaries of Code de la consommation art. D. 215-1. [S16] [S26] Treat it like the German labels: the statutory wording is the safe default, and "Annuler l'abonnement" on that function is a legal risk. [Article text not read on Légifrance in this pass; confirm with legal.]
- ko: 구독 취소 is proposed; 구독 해지 is also common for ending a subscription. Pick one.
- ja: 解約 for ending a contract; キャンセル is less specific.
- Billing events differ: charge incurred, invoice issued, payment completed, refund issued. JA-11 lists the Japanese trap (課金 vs 請求).

## ai

- Regenerate: confirm whether it replaces the current result or adds a new candidate. zh-TW 重新產生 should be checked against the product's existing AI terms.
- Stop generating stops further output. It does not undo changes already applied.
- Discard changes throws away changes that are not applied or not saved. For applied changes, use Revert or Undo.
- Apply changes moves a previewed suggestion into the real content. Keep preview and real change distinct.
- Suggestions and estimates must not read as confirmed facts or completed work.
- fr: "Annuler les modifications" (Revert) shares "Annuler" with Cancel and Undo. If they can co-occur, use "Revenir à la version précédente" for Revert. Do not use "Rétablir", which is the Redo term.
- es: "Revertir cambios" is common in tech UI, but the DLE lists "revertir" as intransitive; "Restablecer la versión anterior" avoids the question.
- fr: "Abandonner les modifications" is proposed for Discard; "Ignorer les modifications" also occurs. Low confidence on market preference.

## browser

- **Bookmarks.** Chrome, Firefox and Apple Safari use 북마크 in Korean (Safari's Korean guide uses 북마크 for bookmarks and 즐겨찾기 for a separate Favorites feature). [S28] [S30] [S31] Microsoft Edge calls the feature "Favorites" in English [S32], and its Korean UI uses 즐겨찾기 [Korean Edge UI not checked directly in this pass]. So translate "Bookmarks" as 북마크 and "Favorites" as 즐겨찾기. 책갈피 is a literal translation of the English word and is not used by any of these browsers' current Korean UI.
- **Bookmarks in fr-FR and es-419.** Chrome uses "Favoris" (fr-FR) and "Favoritos" (es-419); Firefox uses "Marque-pages" and "Marcadores". These collide with Favorites in this glossary. If one product has both bookmarks and favorites, use Marque-pages / Marcadores for bookmarks.
- **Tab.** A browser tab is Onglet (fr), Pestaña (es), 标签页 (zh-CN), 分頁 (zh-TW). Do not leave "Tab" untranslated in French or Spanish, and do not use 标签 alone (it means label or tag).
- **History.** Chrome's Korean term is 방문 기록 (Firefox: 기록); German Chrome uses Verlauf (Firefox: Chronik).
- **Find vs Search.** Chrome keeps Find (찾기, 查找, 尋找) apart from Search (검색, 搜索, 搜尋). Keep the same split.
- **Delete browsing data.** Chrome renamed "Clear browsing data" to "Delete browsing data"; the Korean label is 인터넷 사용 기록 삭제, not a literal 탐색 데이터 삭제.
- **Zoom (es).** Platform pairs differ: es-ES Chrome Ampliar / Alejar, es-419 Acercar / Alejar, Firefox Aumentar / Reducir. Keep one pair per product.

## system-ui

- **Dark theme.** Google uses 어두운 테마 (ko), Dunkles Design (de), ダークモード (ja), 深色主题 / 深色主題 (zh). "Dark mode" as a label is Android's quick setting (어두운 모드, Mode sombre, Modo oscuro). Light theme cells for de and zh mirror the Google dark-theme terms; Firefox uses Helles Theme, 明亮主题 and 亮色佈景主題.
- **Help (zh-Hant-TW).** Taiwan UI uses 說明 for Help; 幫助 is a literal choice that Chrome, Android and Firefox do not use for the Help menu.
- **Do Not Disturb.** Market terms are not literal: サイレント モード (ja), 零打擾 (zh-TW), No interrumpir (es-419), 방해 금지 모드 (ko).
- **Accessibility.** Android uses Bedienungshilfen (de), ユーザー補助 (ja), 無障礙 (zh-TW) for the settings section; Firefox uses Barrierefreiheit, アクセシビリティ and 輔助功能. Use the Android terms for settings labels; the Firefox terms read as the general concept.
- **Appearance.** Chrome uses 디자인 (ko), デザイン (ja), Diseño (es-419) for the Appearance settings section.
- **Japanese spacing in katakana compounds.** Google writes a half-width space between katakana words (キーボード ショートカット, パスワード マネージャー, サイレント モード); Firefox does not (キーボードショートカット). Choose one rule per product.
- **Korean spacing.** Google writes 허용 안함 and 사용 안함; standard spacing is 허용 안 함 and 사용 안 함. The glossary uses standard spacing.

## common-actions

- **OK and Got it.** Spanish uses Aceptar for OK; Chinese uses 确定 / 確定; Korean uses 확인 for both OK and Got it. For "Got it", Google uses OK in French and German; Firefox uses J'ai compris and Verstanden.
- **Add.** es-ES Añadir, es-419 Agregar, zh-Hant-TW 新增: regional choices, not synonyms.
- **Next vs Continue.** zh-Hant-TW Chrome uses 繼續 for Next; this glossary keeps 下一步 for Next and 繼續 for Continue. In German both are Weiter; write the object if both appear.
- **Remove.** Chrome and Android use 삭제 (ko) and Supprimer (fr) for Remove. This glossary keeps 제거 and Retirer for remove-from-a-place so that Delete and Remove stay distinct; if a product never shows both, the platform term is acceptable.
- **Turn on / off (ko).** Android and Chrome use 사용 설정 / 사용 중지 and the status words 사용 / 사용 안 함; Firefox uses 켜기 / 끄기. Choose one pair per product.
- **On / Off (ja).** Android writes ON / OFF; Chrome and Firefox write オン / オフ. The glossary uses オン / オフ to match オンにする / オフにする.
- **Pin.** Google strings also contain PIN (code); never reuse the PIN translation for pinning.
- **Update (ja).** 更新 is used for both Update and Refresh in Chrome and Firefox. When both actions appear, write the object (アプリを更新, ページを再読み込み).

## messaging

- **Comments.** For comments on shared content, Korean products use 댓글 and Taiwan Chrome uses 留言. Firefox's 주석 / 批注 / 註解 are annotation terms for PDFs, not discussion comments.
- **Archive (ko).** 보관처리 is the Google term; 보관 alone also occurs.
- **Unread (es).** Agreement follows the noun: No leídos (mensajes), No leídas (notificaciones).
- **Something went wrong.** Platform translations are full sentences in each language's natural form (문제가 발생했습니다, 問題が発生しました, Un problème est survenu); do not translate word for word.

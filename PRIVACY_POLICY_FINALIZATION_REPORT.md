# Privacy policy finalization — milestone 11.1

Prepared October 27, 2026. Complete publication content is implemented locally in
both repositories. Operator/operating practices are owner-confirmed. **This task did
not commit, push or deploy.** The live policy URLs still served the earlier drafts
when checked. Finalized publication is therefore pending; legal certification and
App Store approval are not claimed.

## 1. Items resolved and evidence

| Previously unresolved | Decision / evidence |
| --- | --- |
| Operator | Stas Stern, an individual developer based in Israel, supplied in the milestone brief; no invented organization/address/DPO |
| Contact/provider | staroldur@gmail.com, Gmail through Google, explicitly confirmed |
| Mailbox access | Owner confirms only Stas Stern has developer-side access; Google/provider processing is explained separately |
| Email content and purpose | Voluntary sender address, subject, body and chosen attachments; questions, technical investigation, follow-up and privacy requests; no automatic sending or medical attachments |
| Retention | Owner confirms only as reasonably necessary for the inquiry, related follow-up and applicable obligations; no automatic fixed deletion period |
| Requests | Owner confirms access/correction/deletion handling with reasonable verification; same email, applicable-law handling, no arbitrary additional deadline |
| Territories | International English-speaking and Israeli Hebrew-speaking audience; actual Store countries still being configured; no worldwide guarantee, exclusive Israeli-law clause or automatic GDPR assertion |
| Hosting | HTTPS English/Hebrew policy and English support pages return 200; GitHub Pages present-tense disclosure, including IP security logging |
| Dates | Source prepared for October 27, 2026 publication, identical ISO date and localized visible dates; actual final deployment not performed |

The app contact method was inspected in about_actions.dart and native open handling:
mailto with version subject, no body/attachment parameters; explicit mail-app send.
Protected storage, Vision OCR, local notifications, EventKit, StoreKit current
entitlements/restore and portability deletion/replacement boundaries were inspected
against existing architecture, security and StoreKit reports. No production behavior
was changed or new device test result inferred from this source review.

## 2. Final policy destinations and effective date

- English: https://staroldur.github.io/medical-timeline-site/privacy.html
- Hebrew: https://staroldur.github.io/medical-timeline-site/privacy-he.html
- English support: https://staroldur.github.io/medical-timeline-site/support.html
- Hebrew support: https://staroldur.github.io/medical-timeline-site/support-he.html

Both policies contain `<time datetime="2026-10-27">` and visible October 27, 2026 /
27 באוקטובר 2026. **This date is valid only if this finalized revision is first
published on that date.** If publication is later, change the ISO and visible dates
in both pages AND the application copies to that actual date before publishing.
The previous draft's publication is not the effective date of the final policy.
Do not mark final publication complete until new deployed content is verified.

## 3. Substantive English/Hebrew changes

All existing local medical/profile/minor/photo/document/OCR disclosures, security
limits, App Lock/passcode fallback, forgotten-password and device-loss warnings,
destructive full restore, independent encrypted profile copy, readable PDF/ZIP risks,
notifications, Calendar sync boundaries and Apple non-consumable purchase behavior
are retained. Manual and automatic scanning are explicit. No advice, diagnosis,
automatic cloud sync, universal OCR accuracy or perfect-security claim was added.

Separate complete sections now explain:

- Local retention/deletion versus voluntary email correspondence.
- Exactly what emails can contain and their limited support/privacy purposes; even
  unsolicited medical information can be received, though users are told not to send it.
- Confirmed developer-side mailbox access, Google and other email provider roles,
  possible processing outside the user's country/Israel, provider backups and deletion limits.
- Email access/correction/deletion requests, reasonable verification without asking
  for medical records or identity copies in an initial request, applicable-law handling.
- The developer's inability to remotely retrieve/delete on-device medical records,
  and separate handling of external backups, source files, recipients and Calendar copies.
- iOS permission control and Apple's separate purchase/account records.
- Live GitHub Pages hosting, IP security logging, and no site-added tracking/scripts/
  cookies/forms/accounts/remote fonts. Google/GitHub/Apple policy links are ordinary
  outbound links and introduce no automatic third-party resource loading.

Operator, effective date and clickable contact are separate semantic paragraphs at
the top of each page. Hebrew isolates complete Latin names, the full email address
and provider names with bdi. Each page prominently links to the complete other language.
The existing candidate Markdown paths are now complete final publication counterparts,
with no unresolved editorial preface; their filenames are retained for existing links.
All 28 substantive paragraphs in each language match the corresponding web page.

## 4. Draft/indexing/navigation corrections

Removed draft titles/descriptions/notices, unresolved handling paragraphs and
noindex/nofollow from both policy pages. Home/support links now say policy rather
than draft, without rewriting those pages. robots.txt permits all pages and sitemap.xml
includes both policies. Canonical/hreflang destinations remain the actual Pages base.
The HTML validator's grouping warnings were fixed by using div for unheaded groups;
no layout redesign or new CSS/JavaScript was introduced.

## 5. Authoritative review and limits

Checked October 27, 2026:

- [Apple App Review Guidelines 5.1.1](https://developer.apple.com/app-store/review/guidelines/#data-collection-and-storage): accessible in-app/Connect policy, processing uses, retention/deletion and user control. This is a disclosure review, not Apple approval.
- [Israeli PPA notice guidance, updated after Amendment 13](https://www.gov.il/BlobFolder/legalinfo/duty_to_notify/he/notify13.pdf) and [updated access guidance](https://www.gov.il/BlobFolder/legalinfo/right_of_access/he/av_recordings.pdf): notice transparency and access/correction require attention for actual off-device support processing. Official indexed text was available; direct full-document retrieval returned HTTP 403. No exhaustive full-statute review is claimed.
- [Library of Congress account of Amendment 13](https://www.loc.gov/item/global-legal-monitor/2025-11-17/israel-amendment-to-privacy-protection-law-goes-into-effect/): confirms the amendment took effect August 14, 2025. Older pre-amendment assumptions were not treated as current law.
- [Google Privacy Policy](https://policies.google.com/privacy): email content and provider processing/retention are separate from local app medical storage.
- [GitHub Pages data collection](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) and [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement): visitor IP logging and separate host handling.

No claim is made that every international privacy regime applies merely because the
app may be downloadable abroad, nor that Israeli law excludes other applicable rights.
Actual country settings and mailbox processing determine any further statutory notice,
address, security, international-transfer or other legal obligations. These cannot be
settled from app source alone; no exemption, DPO/registration conclusion, contract
adequacy or compliance certification is invented. This is a targeted factual policy
revision; any jurisdiction-specific obligation identified at launch must be addressed.

## 6. Validation actually performed

| Check | Outcome |
| --- | --- |
| python3 validate.py | Passed; checks final text, required disclosures, dates, indexing/sitemap, local links/assets, balanced HTML and metadata |
| Validator regression suite | 6 passed, with EN/HE mutation subcases for draft/noindex, dates, missing retention, robots exclusion and missing sitemap policy |
| Cross-repository text comparison | 28 substantive paragraphs per language match exactly after removing HTML markup |
| W3C Nu HTML validator | All six pages passed with no messages after semantic grouping fixes |
| Browser responsive matrix | All six pages at 320, 375, 390, 430, 768, 1024 and 1440px: 42 checks, no horizontal overflow, images loaded |
| Hebrew/English headers | Visually checked at 390px; operator/date/contact are separate and readable, mail address isolated |
| Keyboard / console | Tab reaches visible skip-link focus outline; no warnings/errors reported in inspected browser session |
| Tracking/resources | Source audit: no scripts/forms/iframes, remote src, CSS imports or remote CSS assets; all website assets local; no packet-capture audit claimed |
| Print | Existing plain print CSS inspected for policy text and full-width document; physical print/PDF pagination not executed |
| git diff --check | Passed in both repositories |
| Live HTTPS before deployment | English/Hebrew policies and English support returned 200; policies still contained previous draft banners |
| Final deployed revision | Unrun: no commit/push/deployment in this milestone |

The app changes are Markdown-only; under AGENTS.md no Flutter analysis/tests/builds
are required for this task. No app runtime, Simulator or physical-device checks were
run or claimed. No Xcode/Android setup is needed for these content changes. Validation
does not prove legal compliance, actual final publication or App Store acceptance.

## 7. Minimal owner/release checklist

- [x] Confirm operator/contact/base in Israel; no guessed postal or corporate details.
- [x] Confirm developer-side mailbox access, reasonable-necessity retention/deletion,
  and email privacy-request handling with reasonable verification. Owner confirmed
  all on October 27, 2026; maintain these practices after release.
- [ ] Finalize actual App Store country settings; address any resulting legal notice,
  address, transfer or operational requirements for the actual setup. Do not publish
  a guessed address or invent applicability/exemption conclusions.
- [ ] On authorized deployment, set the real effective date if later than October 27,
  publish both finalized policies and verify content over HTTPS. No new blanket legal
  approval gate or paid legal certificate is imposed by this report.

## 8. App Store Connect and in-app configuration

After final publication is content-verified, use the English policy URL above as
baseline Privacy Policy URL, Hebrew policy URL for Hebrew-localized metadata where
available, and localized Support URLs above. Confirm the pages are accessible without
sign-in. No App Store Connect value was changed here.

In the application repository, set the existing release helper's public policy input:

```sh
POLICY_URL='https://staroldur.github.io/medical-timeline-site/privacy.html'
python3 tool/release_config.py prepare --policy-url "$POLICY_URL" --build 1 --previous-build 0
```

Use that build history ONLY if still owner-confirmed; otherwise choose a valid next
build and actual highest uploaded build. This helper checks URL syntax, not final
publication or legal sufficiency. Follow RELEASE_BUILD_V1.md for the normal
lib/main.dart signed Release/archive flow, verify final policy constants and About's
actual policy action, then complete privacy/export compliance and owner submission.
Keep the single English destination with its prominent full Hebrew link. No URL
routing subsystem, app feature, medical storage/schema/crypto/StoreKit change, iPad
support, new language, dependency or tracking was added.

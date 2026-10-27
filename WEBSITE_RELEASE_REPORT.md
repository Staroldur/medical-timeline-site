# Website release preparation — October 27, 2026

**Historical initial-site snapshot.** Privacy draft/indexing/deployment status below
is superseded by PRIVACY_POLICY_FINALIZATION_REPORT.md (milestone 11.1). Prior
validation evidence is retained; it is not a claim of final-policy publication.

Implemented in a real clone of `Staroldur/medical-timeline-site`, on main.
The owner subsequently requested committing and pushing the website for testing.
No Pages configuration, app upload or submission was performed; website deployment
is not verified. Planned public base:
`https://staroldur.github.io/medical-timeline-site/`. Live status is **unverified**.

## Design and architecture

Six buildless HTML pages, shared styles.css and local assets; .nojekyll, robots.txt,
sitemap.xml and optional standard-library validate.py. No package/build pipeline.
Warm ivory canvas, deep evergreen, muted gold, system serif English headings and
local Heebo Hebrew/body text. Generous editorial spacing, original Yggdrasil focal
art, subtle non-mirrored rings, three connected feature sections, privacy section,
free-versus-Full Unlock and support. No fake app screenshots or stock medical imagery.
English is the default; switches preserve home/support/privacy context.

Reference inspected: `Staroldur/letters-app` index.html, privacy.html, styles.css,
README.md and assets. Reused its simple root-file Pages architecture and licensed
local font approach, without game text/art/child policy. Images originate only from
Medical Timeline appIcon.png, resized to WebP 640×640 and 128×128 (about 100 KiB and
8 KiB on disk); font about 116 KiB, with full OFL notice. No images were redrawn.
The homepage transfers roughly 240 KiB of uncompressed local files; support/policy
omit the large illustration. This is a file-size estimate, not a measured speed score.

## Content and privacy review

index.html/he.html include official names/subtitles, timeline/appointments, manual
and automatic scans, imports/search limits, preparations/reminders, local privacy,
manual encrypted backups and accurate one-time purchase benefits. Free one-profile
scope, existing-data access and free full backup/restore are explicit. No fixed price,
subscription, automatic booking, clinical service, cloud sync or Family Sharing claim.
No confirmed numeric Store ID exists locally: noninteractive Coming soon; README
explains replacement only after a verified real public listing.

support.html/support-he.html cover setup, Full Unlock, Restore Purchases versus
medical restoration, local storage, saving an external encrypted backup, destructive
full restore, lost passwords/device/uninstall, permissions, provider files, reminders,
Calendar and technical bug reports. No records/names/passwords requested in email;
no response-time promise or clinical support. Contact: staroldur@gmail.com.

privacy.html/privacy-he.html carry **all substantive candidate policy sections**,
not summaries: local family/health/photos/documents/OCR, protection/limits, App Lock,
manual encrypted backup/password loss/full replacement, encrypted profile copies,
readable exports/recipients, notifications, Calendar, Apple StoreKit, retention,
local deletion/support and updates. Added a complete bilingual website/provider
section: GitHub hosting requests are separate from app medical storage. This is
consistent with [GitHub's Pages IP logging disclosure](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
and its linked privacy statement. Neither Apple nor GitHub/email processing is denied.

App candidates, APP_PRIVACY_INVENTORY_V1.md, ARCHITECTURE.md, SECURITY_REVIEW.md and
MILESTONE_10_STOREKIT_REPORT.md supplied the implementation boundaries. Earlier
milestone caveats are historical, not declarations of new runtime passes.

Operator **Stas Stern** and mailbox are owner-confirmed. Policies remain visibly
marked draft, not effective; noindex and robots disallow are editorial safeguards,
not access control. Effective date, territories, any required address, support access/
retention/international handling and applicable rights/request process remain owner/
legal review items. Draft handling paragraphs explicitly identify these gaps; no
legal facts are invented. **Publication is held until both language versions are
finalized.** README gives the precise draft-marker/indexing removal steps.

## Validation actually performed

| Check | Result |
| --- | --- |
| Browser matrix | All 6 pages × 320, 375, 390, 430, 768, 1024, 1440 CSS-pixel viewport widths, 900px height; 42 settled checks passed |
| Overflow / images | document scroll width never exceeded client width; all images loaded in those checks |
| Visual review | EN desktop hero; HE 390px home and policy; EN full-page and HE viewport/scroll review of content and navigation |
| Keyboard | Tab reaches skip link with visible solid focus outline; normal anchors use focus-visible styling |
| Semantics | One h1 per page, landmarks, labelled navigation, descriptive hero alt, empty decorative icon alt, skip link |
| RTL | Hebrew document dir=rtl, directional spacing/borders, isolated mixed Latin in policy/support; original art not mirrored |
| Contrast | Body muted/ivory 5.67:1; gold changed to #806326 after initial small-text gold failed 4.5:1; green-section body 8.16:1 |
| Local source checker | Passed: balanced tags, duplicate IDs, all local links/fragments/assets, direction, titles/descriptions, canonicals/alternates, sitemap paths, no script/iframe/form or remote asset src |
| External requests | Source inspection: assets/fonts/CSS local, no scripts or CSS imports; only explicit email/GitHub privacy outbound links. No packet-level capture claimed |
| Console | Browser reported no warnings/errors during inspected home/policy navigation; no JavaScript ships |
| Reduced motion | No animations; explicit reduced-motion CSS safety rule |
| Print | Dedicated plain print CSS for complete policy; actual print-dialog/PDF pagination not run |
| Diff whitespace | git diff --check passed; source safety reviewed |
| W3C HTML/CSS validation | Full official validator not installed/run; source checks and real browser rendering are not a conformance certificate |
| Live HTTPS / public links | Unrun; no deployment authorized/performed |

Browser uses a scrollbar gutter, so client width is 15px smaller than requested
viewport width; checked actual innerWidth matches every requested size. Layout
checks concern actual rendered pages, not assertions from CSS breakpoints alone.
Not an exhaustive WCAG audit or native screen-reader/real Safari certification.

## Handoff

Follow README in order: finalize legal facts in both languages; review/commit/push;
Pages main/root; verify six HTTPS destinations anonymously; configure Connect Support
and Privacy URLs; configure app PRIVACY_POLICY_URL using the English policy with its
prominent full Hebrew link; rebuild/verify signed normal Release; owner submits.
No new app localization router, medical feature, analytics or cloud backend.
Physical iPhones were intentionally not used; browser mobile widths are desktop
responsive checks, not physical-device evidence. Native app checks are recorded in
the application repository’s IPHONE_ONLY_RELEASE_REPORT.md.

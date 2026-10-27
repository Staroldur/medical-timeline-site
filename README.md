# Medical Timeline companion website

Static English/Hebrew website for `Staroldur/medical-timeline-site`.
No build step, package installation, JavaScript, cookies, analytics, contact forms,
accounts or backend. Serve the repository root directly with GitHub Pages.

**Prepared for repository testing; GitHub Pages deployment is not verified. Privacy pages are complete publication drafts, not
legally approved or effective policies. Do not enable Pages until the review below
is complete.** A noindex tag is not an access control; public Git content is public.

## Pages

| English | Hebrew | Purpose |
| --- | --- | --- |
| index.html | he.html | Product, real functionality, free/Full Unlock distinction |
| support.html | support-he.html | Setup, purchases, backups, permissions, safe bug reporting |
| privacy.html | privacy-he.html | Complete policy candidates with hosting disclosure |

Each language switch opens the equivalent page. English is the default destination.
Styles and assets are shared; Hebrew has RTL chrome and isolated Latin text.
The original Tree of Life artwork is never mirrored.

## Local preview and checks

```sh
python3 -m http.server 8766 --bind 127.0.0.1
python3 validate.py
```

Open `http://127.0.0.1:8766/`. `validate.py` uses only Python's standard library;
it checks source structure, links/fragments, assets and metadata, not browser layout,
legal sufficiency or full W3C conformance. The site also works without Python once
hosted. No tool-generated runtime files are required.

## Review before publication

Owner confirmed **Stas Stern** and **staroldur@gmail.com** on October 27, 2026.
The policy preserves all substantive sections of the current application candidates,
cross-checked against architecture, security review, privacy inventory and StoreKit
report. The GitHub Pages section is specific to this website. Nothing was copied
from Dino's gameplay, children’s rules or privacy claims.

Still required, with external review where appropriate:

- Effective date and intended distribution territories.
- Any required legal/address details and authority to record/share family/child data.
- Support mailbox access, provider arrangements, retention/deletion and international handling.
  The confirmed address uses gmail.com; no retention or access practice is inferred.
- Applicable privacy rights, identity verification and actual request handling.
- Actual hosting settings and GitHub's separate processing. GitHub logs visitor IP
  addresses for security; do not say nobody processes website visitor information.
- Final App Privacy questionnaire and encryption/export-compliance decisions belong
  to the app release owner; these pages do not establish those answers.

Apply the same approved decisions to **both** privacy pages and the application's
policy candidates. Set the effective date, replace the draft handling paragraphs with
confirmed wording, remove the draft notice/title wording and privacy noindex tags.
Remove privacy Disallow entries from robots.txt and add both privacy URLs to sitemap.xml.
Update homepage/support links that say “policy draft”. Do not publish unfinished text.
No date, jurisdiction, retention period or certification has been guessed.

## Publish with GitHub Pages

1. Finish and approve the legal/operator review above. Review the diff for public
   safety: only public HTML/CSS, approved art, font/license and documentation belong here.
2. The owner requested committing and pushing the website to **main** for testing.
   No deployment workflow or external host is required. Repository availability does
   not by itself establish a successful GitHub Pages deployment.
3. In GitHub repository Settings → Pages, select **Deploy from a branch**, branch
   **main**, folder **/ (root)**. Save and wait for the actual Pages deployment result.
4. Confirm the deployed HTTPS base is actually
   `https://staroldur.github.io/medical-timeline-site/`. This remains a **planned URL**
   until verified. Enforce HTTPS when available. If base/path changes, update all
   canonical/alternate links, sitemap.xml, robots.txt and validate.py’s BASE value.
5. Open every page below without signing in, check both languages on mobile, inspect
   navigation/links, compare approved policy content, check HTTPS and response status.
6. Enter the verified `support.html` URL in App Store Connect's English Support URL;
   use `support-he.html` for Hebrew localized metadata. Enter the verified privacy URL
   in the corresponding policy fields; English links prominently to full Hebrew.
7. In the **application** checkout configure `PRIVACY_POLICY_URL` with the real published
   `privacy.html` URL via `tool/release_config.py prepare`. Keep the existing single
   destination; a second locale routing system is unnecessary. See RELEASE_BUILD_V1.md.
8. Rebuild and verify the final signed **1.0.0** Release candidate with `lib/main.dart`,
   final policy defines, correct next build number and iPhone-only device family.
   Verify the actual About policy action before the owner uploads/submits manually.

Planned verification checklist (none is claimed live):

- https://staroldur.github.io/medical-timeline-site/index.html
- https://staroldur.github.io/medical-timeline-site/he.html
- https://staroldur.github.io/medical-timeline-site/support.html
- https://staroldur.github.io/medical-timeline-site/support-he.html
- https://staroldur.github.io/medical-timeline-site/privacy.html
- https://staroldur.github.io/medical-timeline-site/privacy-he.html

## App Store download link

No confirmed numeric Medical Timeline App Store ID was found in the release records.
Both landing pages therefore use a noninteractive “Coming soon” label. After actual
app publication, verify the official Medical Timeline listing and its numeric ID;
replace each `.coming` span with a real `.button` anchor to
`https://apps.apple.com/app/id<CONFIRMED_NUMERIC_ID>`. Verify the listing belongs to
Medical Timeline: Family Care / מה קבעתי. Do not substitute Dino or another app.
Keep price out of static copy. No Family Sharing or health-record synchronization
availability is promised. App rating/sharing flags are separate app build settings.

## Assets and licensing

- `assets/yggdrasil.webp`: resized to 640×640 from approved original **appIcon.png**
  in `Staroldur/medical-timeline`; no redraw, replacement or generated art.
- `assets/icon.webp`: same original, 128×128; used as navigation icon and favicon.
- `assets/Heebo.ttf`: unchanged local variable font reused from the reference
  `Staroldur/letters-app`, originally the Heebo project. Redistribution under the
  included **assets/Heebo-OFL.txt** (SIL Open Font License 1.1); copyright retained.
- English editorial headings use system Georgia; no external font CDN or download.

The artwork is approved product branding, not a medical document or new license grant.
No private app configuration, records, backups, screenshots, signing assets, patient
fixtures or source repository tree were copied. No real medical information appears.

## External provider references

- [GitHub Pages and its IP logging](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [GitHub General Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)
- [GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

See WEBSITE_RELEASE_REPORT.md for observed validation and intentional limits.

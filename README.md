# Medical Timeline companion website

Static English/Hebrew website for `Staroldur/medical-timeline-site`, hosted on GitHub
Pages. No build step, packages, JavaScript, cookies, analytics, forms, accounts or
backend. Images and the licensed font are local.

## Privacy policy status — milestone 11.1

Complete publication content is prepared in both languages, with matching copies in
the application repository's PRIVACY_POLICY_CANDIDATE_EN.md and
PRIVACY_POLICY_CANDIDATE_HE.md (filenames retained for existing references).
The owner confirmed Stas Stern, an individual developer based in Israel,
staroldur@gmail.com, sole developer-side mailbox access, purpose-limited retention,
and handling access/correction/deletion requests with reasonable verification.
Actual App Store countries are still being configured; the policy does not promise
worldwide availability or impose one jurisdiction's law on every user.

The source effective date is **October 27, 2026**, for publication on that date.
If the finalized content is first published later, update BOTH policy `<time>` values,
visible dates and the matching application copies to the actual publication date.
Do not backdate or treat the previous draft's deployment as final publication.

The public English/Hebrew policy and English support URLs returned HTTPS 200 on
October 27, 2026, but still served the **previous drafts** during this milestone.
This milestone's final content is local and uncommitted; no deployment has occurred.
Do not use a local validation pass as proof that the finalized policy is already live.
See PRIVACY_POLICY_FINALIZATION_REPORT.md for decisions, sources and release checks.

## Pages

| English | Hebrew | Purpose |
| --- | --- | --- |
| index.html | he.html | Existing product pages |
| support.html | support-he.html | Setup, purchases, backups and safe bug reports |
| privacy.html | privacy-he.html | Complete privacy policies |

Language switches preserve page context. English is the default. Hebrew has RTL
layout, isolated Latin names/email/providers and readable separate operator/date/
contact fields. Approved original Tree of Life artwork is never mirrored.

## Preview and validate

```sh
python3 -m http.server 8766 --bind 127.0.0.1
python3 validate.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -p test_validate.py
```

Open `http://127.0.0.1:8766/`. Python is for optional local preview/checks only.
The host serves root HTML/CSS directly. The source validator rejects draft text,
noindex/nofollow, missing effective dates/disclosures, differing policy dates,
robots policy exclusions, sitemap omissions, broken local links and remote assets.
It cannot certify legal compliance or the actual publication date.

## Publish the finalized policy

1. Review the confirmed operating practices in the finalization report and ensure
   they are maintained. Recheck whether the actual launch countries/mailbox setup
   require further statutory notice, address, transfer or other operational steps.
   No invented address, DPO, organization, certification or legal exemption appears.
2. Set both effective dates to the ACTUAL publication date if it is no longer
   October 27, 2026. Synchronize application policy copies. Run the checks above.
3. When explicitly authorized, commit/push the reviewed changes to **main**. This
   milestone does not authorize commit/push. Exclude `.DS_Store` and private data.
4. Existing Pages should use Deploy from a branch → main → / (root). Review its
   actual deployment result; enforce HTTPS. No external deployment service needed.
5. Verify every URL below anonymously over HTTPS. For both policies, verify the new
   effective date, support-retention/request text, no draft notice/noindex, correct
   language switch and mobile rendering. Confirm robots.txt allows the policies
   and sitemap.xml contains both. A 200 response with old draft content is insufficient.
6. Set App Store Connect Privacy Policy URL to the finalized English URL, with the
   Hebrew URL in Hebrew-localized policy metadata where available. Use support.html
   as English Support URL and support-he.html for Hebrew. No account access was changed.
7. In the APPLICATION repository follow RELEASE_BUILD_V1.md: set PRIVACY_POLICY_URL
   through the existing release-config helper to the verified finalized English
   URL. Its prominent link opens the full Hebrew policy. No new routing layer.
8. Verify the final signed normal lib/main.dart Release archive, actual next build
   number, iPhone-only family [1] and installed About policy action before App Review.
   Website checks do not validate the app's signing, privacy label or export compliance.

Public destinations (existing hosted pages; finalized revision still needs deployment):

- https://staroldur.github.io/medical-timeline-site/index.html
- https://staroldur.github.io/medical-timeline-site/he.html
- https://staroldur.github.io/medical-timeline-site/support.html
- https://staroldur.github.io/medical-timeline-site/support-he.html
- https://staroldur.github.io/medical-timeline-site/privacy.html
- https://staroldur.github.io/medical-timeline-site/privacy-he.html

If the base changes, update canonical/alternate links, sitemap.xml, robots.txt and
validate.py's BASE. Policies are indexable; indexing is not a compliance guarantee.

## App Store link

No confirmed numeric Medical Timeline Store ID was found in the release sources.
Coming soon remains noninteractive. After verifying the real published Medical
Timeline listing, replace `.coming` spans in both homepages with `.button` links to
`https://apps.apple.com/app/id<CONFIRMED_NUMERIC_ID>`. Never substitute another app.
No static price, subscription, health-record sync or Family Sharing promise.

## Asset provenance

- assets/yggdrasil.webp: approved application appIcon.png, resized to 640×640.
- assets/icon.webp: same original, resized to 128×128.
- assets/Heebo.ttf: unchanged local font from Staroldur/letters-app, originally the
  Heebo project. Full SIL OFL 1.1 copyright/license in assets/Heebo-OFL.txt.
- System Georgia for English headings; no font CDN, stock image or redrawn branding.

No medical documents, private backups, patient fixtures, signing assets or private
application configuration are part of this public repository.

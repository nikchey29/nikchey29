# Chaithanya Vemuri — Portfolio V4

An editorial static portfolio for junior Data / ML Engineering roles. Ten content routes, three technical case studies, locally hosted portrait and fonts, interactive architecture illustrations, and role-focused CVs. The existing V3 design informed the new composition; all project metrics were checked against source artifacts on 22 October 2026.

## Build and checks

Python 3.10+ is sufficient to build the site. There is no frontend dependency installation or framework runtime.

```sh
npm run build
python3 -m pip install -r requirements-dev.txt
npm run check
```

`npm run build` runs `scripts/build.py` and writes `dist/`. Checks inspect every internal route, fragment, render asset, metadata contract, PDF text/link/page contract, key evidence values and the main text palette contrast. They also run Node's JavaScript syntax check.

To regenerate CVs after a factual edit:

```sh
python3 scripts/resumes.py
npm run build
npm run check
```

Original font files used by the PDF renderer are in `source-assets/fonts/`. The public website serves smaller subsetted WOFF files. The three SIL Open Font License files are included in `assets/font-licenses/`.

## Publishing

This source is prepared for the existing public site, `https://chaithanyavemuri.netlify.app/`. Its canonical URLs, sitemap, social metadata and CV hyperlinks use that origin.

- **Git-connected Netlify:** set the base directory to this portfolio folder. The root `netlify.toml` runs the build and publishes `dist/`.
- **Manual Netlify deployment:** deploy only the contents of `dist/`, or the prepared deploy ZIP. The built folder has its own static Netlify configuration and needs no build command.
- **Another origin:** change `ORIGIN` in `scripts/build.py` and `P` in `scripts/resumes.py`, regenerate CVs, build, check and republish.

Authenticated owner access to the existing Netlify site is required to replace its deployment and inspect its actual repository connection. The current public homepage was read and matched the retained V3 package. No connected GitHub repository was established as its deployment source. This V4 source branch is a new recoverable source location, not evidence that Netlify already tracks it.

## Content and claim boundaries

- REES46: 411,709,736 Bronze / 410,325,314 Silver events. Monthly Gold plus 64 session buckets. Ranking benchmark: 1,499,021 training interactions / 5,000 test users, separate from the full data corpus.
- FulfillAI: synthetic orders and a controlled API platform lab. Complete V2 remains on `platform-engineering-v2`; API delivery evidence does not prove that the full data stack ran in GKE.
- OTTO: aggregate hourly cart / order activity, 672 observations, eight methods, three development folds and separate 96-hour holdout. The baseline was selected by mean CV WAPE; Ridge had lower carts error on the final holdout.
- Education is shown as in progress. November 2026 completion was not independently confirmed. No language levels, certificates, legal work declarations, employment dates or paid engineering responsibilities were invented.
- Contact email is the existing public portfolio email, also supplied by the owner. No deliverability test or email transmission was performed.
- Portrait is the photograph from the authenticated `nikchey29` GitHub profile, downloaded from its returned avatar URL. Its source is 460 × 460 pixels; a higher-resolution replacement would improve large-screen sharpness.

## UI / accessibility

Native cross-document view transitions, scroll reveals, lightweight diagram motion and small portrait parallax. `prefers-reduced-motion` disables animations/transitions/parallax and restores reveal visibility. Mobile navigation supports Escape with focus recovery; buttons have explicit state, diagrams have accessible descriptions, tables have captions and headers, and images retain a clear text fallback on failure.

No trackers, analytics SDKs, fake dashboards, generated likenesses, testimonials or live-production metrics are included.

## Verification limits

Browser layout checks used fixed-size same-origin frames at 320, 768, 1024 and 1440 CSS pixels, plus visual review at 390 pixels and the normal desktop viewport. These are responsive layout checks, not physical-device testing. Lighthouse and OS-level reduced-motion emulation were not available. Reduced-motion rules were reviewed statically. Native browser download-event capture timed out; all PDF files and download targets passed local checks.

The QA harness in `scripts/qa.html` is test-only and is excluded from `dist/` and the deployment ZIP. Build output and deployment archives contain no account credentials.

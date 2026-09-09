# IDUS — Enterprise-Grade AI Platform (Marketing Site)

Single-page static marketing site for the [IDUS](https://serene-idus-a35dd0.netlify.app) AI platform, plus a privacy policy page. No build step — plain HTML with inline CSS and a small amount of dependency-free JavaScript.

## Features

- **Performance (Core Web Vitals)**: no frameworks, no blocking JS, no unused CSS/JS (enforced in CI), Google Fonts + GA `preconnect`, `display=swap` fonts, inline SVG favicon (no 404 round-trip), explicit edge `Cache-Control` rules in `netlify.toml`
- **Accessibility (WCAG 2.1 AA)**: skip link, `<header>`/`<nav>`/`<main>` landmarks, logical heading order, visible `:focus-visible` outlines, `aria-hidden` decorative icons, `prefers-reduced-motion` support, AA-verified color contrast (all text pairs ≥ 4.5:1)
- **Security & privacy**: security headers (CSP, `nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy`, `Permissions-Policy`); Google Analytics loads **only after consent** via an accessible cookie-consent banner; [privacy policy](privacy.html) with auto-updating copyright year
- **SEO / AEO**: meta description, canonical, Open Graph + Twitter Card with a 1200×630 `og:image`, JSON-LD structured data (Organization, WebSite, Product with offers), `sitemap.xml` + `robots.txt`
- **CI/CD**: GitHub Actions lint pipeline (`html-validate`, TOML/XML validation, URL-consistency and unused-CSS checks) — see [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

## Repository layout

```
├── index.html          # The main site (markup, styles, consent + analytics scripts)
├── privacy.html        # Privacy policy
├── assets/
│   └── og-idus-1200x630.png  # Social sharing card (OG / Twitter)
├── scripts/
│   ├── check_urls.py   # canonical / sitemap / robots / og:image consistency
│   └── check_css.py    # fail on unused CSS classes
├── netlify.toml        # Build config, security headers, cache rules, redirect
├── robots.txt          # Search-crawler policy
├── sitemap.xml         # Site map
├── .nojekyll           # Tells GitHub Pages not to process Jekyll
└── ANALYTICS_SETUP.md  # Step-by-step Google Analytics activation guide
```

## Local development

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

Run the same checks CI runs, locally:

```bash
npx html-validate@11 index.html privacy.html
python3 scripts/check_urls.py
python3 scripts/check_css.py
```

## Deploy

### GitHub Pages

1. In the repository, go to **Settings → Pages**.
2. Set **Source** to *Deploy from a branch*, branch `master`, folder `/ (root)`.
3. The site goes live at `https://abhinav-a11y-ops.github.io/idus/` (`.nojekyll` is already present).

Note: GitHub Pages cannot set the security headers or `Cache-Control` rules defined in `netlify.toml` — use Netlify if those matter to you.

### Netlify

The repository is Netlify-ready out of the box (`netlify.toml`): publish dir `.`, no build command, security headers and cache rules included. Connect the repo in Netlify and every push deploys.

## Cookies & analytics

The page ships **without** the analytics tag loading. On first visit a consent banner appears:

- **Allow analytics** → GA4 tag loads, `_ga` cookies set, choice remembered in `localStorage` (`idus-analytics-consent`)
- **Essentials only** → no tag, no cookies, choice remembered

The policy is documented in [privacy.html](privacy.html).

### Activating Google Analytics

The analytics script near the end of `index.html` uses the single placeholder constant `MEASUREMENT_ID = 'G-XXXXXXXXXX'`. Follow [ANALYTICS_SETUP.md](ANALYTICS_SETUP.md) to create your GA4 property and replace that one value.

## Canonical URL

`index.html`, `privacy.html`, `robots.txt` and `sitemap.xml` reference `https://abhinav-a11y-ops.github.io/idus/`. If the final production domain changes, update the canonical, Open Graph, JSON-LD, robots and sitemap references together (CI's `scripts/check_urls.py` will fail until they agree).

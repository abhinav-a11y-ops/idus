# IDUS — Enterprise-Grade AI Platform (Marketing Site)

Single-page static marketing site for the [IDUS](https://serene-idus-a35dd0.netlify.app) AI platform. No build step — the whole site is `index.html`.

## Features

- Single self-contained HTML file (inline CSS, no framework dependencies)
- WCAG-conscious markup: skip link, landmark regions, logical heading order, visible keyboard focus, `aria-hidden` decorative emoji, `prefers-reduced-motion` support, AA-contrast text colors
- SEO: meta description, canonical URL, Open Graph / Twitter Card tags, JSON-LD structured data, `sitemap.xml` and `robots.txt`, inline SVG favicon
- Performance: Google Fonts `preconnect` + `display=swap`, no unused third-party CSS
- Security headers (CSP, nosniff, frame options, referrer policy, permissions policy) configured for Netlify in [`netlify.toml`](netlify.toml)

## Repository layout

```
├── index.html          # The entire site (markup, styles, analytics tag)
├── netlify.toml        # Build config, security headers, SPA-style redirect
├── robots.txt          # Search-crawler policy
├── sitemap.xml         # Site map (single page)
├── .nojekyll           # Tells GitHub Pages not to process Jekyll
└── ANALYTICS_SETUP.md  # Step-by-step Google Analytics activation guide
```

## Deploy

### GitHub Pages

1. In the repository, go to **Settings → Pages**.
2. Set **Source** to *Deploy from a branch*, branch `master`, folder `/ (root)`.
3. The site goes live at `https://abhinav-a11y-ops.github.io/idus/` (`.nojekyll` is already present).

Note: GitHub Pages cannot set the security headers defined in `netlify.toml`.

### Netlify

The repository is Netlify-ready out of the box (`netlify.toml`): publish dir `.` with no build command. Connect the repo in Netlify and every push deploys.

## Google Analytics

The analytics tag in `index.html` ships with the placeholder ID `G-XXXXXXXXXX`. Follow [ANALYTICS_SETUP.md](ANALYTICS_SETUP.md) to create your GA4 property and swap in your real Measurement ID.

## Local preview

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

## Canonical URL

`index.html`, `robots.txt` and `sitemap.xml` reference `https://abhinav-a11y-ops.github.io/idus/`. If the final production domain changes, update the canonical, Open Graph, JSON-LD, robots and sitemap references together.

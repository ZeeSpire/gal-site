# galdc-site

Static HTML/CSS website for **GAL Dobrogea Centrala** (`galdc.ro`).

Migrated from the Next.js `gal-frontend` project to plain HTML/CSS with optional
minimal vanilla JS. No build step is required to host or run this site.

## Layout

- `index.html` — chooser/landing page (LEADER 2023-2027 vs LEADER 2014-2020).
- `acasa/`, `arhiva/`, `contact/`, `details-of-organisations/`,
  `implementarea-sdl-prin-leader/`, `teritoriul-microregiunii/`,
  `finantare-proiecte/*/`, `media/*/` — content pages.
- `404.html`, `robots.txt`, `sitemap.xml` — root-level helpers.
- `assets/css/site.css`, `assets/js/site.js` — shared styling and tiny
  mobile-menu interactivity.
- `helper/`, `interventii/`, `media/`, `teritoriul-microregiunii/`,
  `strategia-de-dezvoltare-locala/` — copied public assets. Their original
  production URLs (e.g. `/media/...`, `/interventii/...`) are preserved.
- `favicon.ico` — copied verbatim from the Next.js source.
- `CNAME` — GitHub Pages custom-domain pin to `galdc.ro`.
- `_tools/build.py` — one-time generator used during migration. Not required
  for hosting; safe to delete after the site is published.

## Local preview

Open `index.html` directly in a browser via `file://`. The navigation, CSS,
and images all work without a server.

For a GitHub Pages-style preview with clean directory URLs:

```bash
python3 -m http.server --directory /Users/gabrielvoicu/Projects/others/galdc-site 4173
```

then visit `http://localhost:4173/`.

## Deployment

GitHub Pages serves the repository root on `main`. No build step. Editing any
HTML file and pushing is enough to publish.
# gal-site

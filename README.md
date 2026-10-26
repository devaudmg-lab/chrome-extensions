# Chrome Extensions

Free Chrome extensions, ready to download and install. None of them collect data or need an account.

## Download

| Extension | Version | What it does | Download |
|---|---|---|---|
| **API Interceptor Pro** | 1.3.0 | Monitor, inspect and mock fetch/XHR API calls; HAR export, copy as cURL. | [api-interceptor.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/api-interceptor.zip) |
| **Blur Remover & DOM Modifier** | 1.2.0 | Remove blur overlays and modals, unlock scrolling, Reader View, dark mode, custom CSS. | [blur-remover.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/blur-remover.zip) |
| **ClearPath Zen Pro** | 1.2.0 | Hide distractions, reading ruler, tints, typography controls, bionic reading. | [clear-path.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/clear-path.zip) |
| **Meta Competitor Intelligence** | 1.1.0 | Turn the Meta Ad Library into a private, searchable competitor database. | [competitor-analysis.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/competitor-analysis.zip) |
| **ContextSearch - AI & Multi-Source Developer Search** | 0.2.0 | Context-aware AI explanations and multi-source developer search (Stack Overflow, GitHub, MDN, npm). | [context-search.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/context-search.zip) |
| **CookieClean** | 1.1.0 | Cookie manager and auto-cleaner: clean on tab close, whitelists, one-key purge. | [cookie-clean.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/cookie-clean.zip) |
| **DevShield — Ad, Tracker & Pop-up Blocker** | 3.1.0 | Ad, tracker, pop-up and redirect-hijack blocker. No telemetry. | [devshield.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/devshield.zip) |
| **Universal Form Autofiller** | 1.2.0 | Fill forms with realistic mock data or Gemini-generated data; profiles and URL rules. | [formfiller.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/formfiller.zip) |
| **Musicox** | 1.1.0 | Background music player for YouTube links and audio URLs. | [musicox.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/musicox.zip) |
| **ScrollShot Pro** | 1.1.0 | Region-locked scrolling screenshots, stitched seamlessly; PNG/JPG/WebP. | [scrollshot.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/scrollshot.zip) |
| **SEO Lens** | 1.1.0 | Real-time on-page SEO audit in the side panel; CSV/Markdown export. | [seo-lens.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/seo-lens.zip) |
| **SEO Rank Finder** | 1.1.0 | Find your site's Google ranking position for a list of keywords. | [seo-rank-finder.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/seo-rank-finder.zip) |
| **SiteScope - Content Auditor** | 1.2.0 | Crawl a whole domain from your browser for content and compliance audits. | [sitescope.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/sitescope.zip) |
| **WebDrawPro** | 1.2.0 | Draw, annotate and measure on any web page; save as a screenshot. | [web-draw-pro.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/web-draw-pro.zip) |
| **Pro Auto Scroller** | 1.3.0 | Smooth, adjustable auto-scrolling; Space to start/pause. | [auto-scroller.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/auto-scroller.zip) |
| **Smooth Keyboard & Mouse Zoom** | 1.2.0 | Smooth zoom toward the mouse with Alt + Scroll and Alt +/-/0. | [zoomer.zip](https://github.com/devaudmg-lab/chrome-extensions/raw/main/zips/zoomer.zip) |

## How to install

1. Download the `.zip` for the extension you want and **unzip it** into a folder you'll keep (Chrome loads it from there, so don't delete it).
2. Open `chrome://extensions` in Chrome (also works in Edge, Brave, Opera and other Chromium browsers).
3. Turn on **Developer mode** (top-right toggle).
4. Click **Load unpacked** and select the unzipped folder (the one that contains `manifest.json`).
5. Pin it from the puzzle-piece menu in the toolbar.

**Updating:** download the new zip, replace the files in the same folder, then click the reload icon on the extension's card in `chrome://extensions`. Your settings are kept.

## For the maintainer

- `extensions.json` lists every published extension: its source folder, the folder that holds `manifest.json` (`.` or `dist`), and which files ship.
- `python tools/package.py` rebuilds every zip into `zips/` and regenerates `zips/index.json` (id, name, version, path) for the website to read. `python tools/package.py zoomer` rebuilds just one.
- The packager fails if the manifest references a file that isn't being shipped.
- Zip names are stable (`zips/<id>.zip`) so download links never change; the version lives in the manifest and `index.json`.
- For extensions with a build step (`devshield`, `seo-lens`), run `npm run build` in the source folder first (or add a `"build"` command to its entry).
- To add a new extension: add an entry to `extensions.json`, run the packager, and commit.

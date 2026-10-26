# SEO Lens

**Tagline:** A complete on-page SEO audit in Chrome's side panel, updated as you browse.

## What it does

SEO Lens audits the page you are looking at and gives it a 0-100 SEO score with a prioritised list of fixes. It checks titles, descriptions, headings, links, images, structured data, social tags, speed and accessibility, and it re-scans automatically when you switch tabs. Everything runs locally in your browser.

## Key features

- **Health score and "Road to 100%" checklist**: each fix shows how many points it is worth and what to change.
- **Content, Tech, Links and Media tabs**: title and description length, heading outline, keyword density, timing, page weight, nofollow and generic anchors, unsafe `_blank` links, a status check on the first 15 links, and images without alt text.
- **Structured data checks**: JSON-LD is shown as a tree and checked for the fields Google needs for rich results (Product, Offer, Article, Organization, BreadcrumbList, FAQPage, Recipe, Event and more).
- **Social previews**: see the page as a Google result and as Facebook, X and LinkedIn cards, plus a list of missing Open Graph and X tags.
- **Score history**: every audit is saved on your device, so you can watch each page improve over time.
- **Printable report**: a clean report you can print or save as a PDF for clients.
- **Scroll and highlight**: click "Show" to jump to a heading, link, image or control on the page.
- **Export**: JSON, CSV or a Markdown summary.
- **Optional AI content-gap ideas** using your own Google Gemini API key.
- Dark and light themes.

## How to use

1. Download and unzip the ZIP, open `chrome://extensions`, turn on **Developer mode** and click **Load unpacked**. Select the unzipped folder.
2. Pin SEO Lens and click its icon (or press `Alt+Shift+S`) to open the side panel.
3. Open any website. The panel scans it automatically.
4. Start with **Summary** for the biggest wins, then open the other tabs for details.
5. Fix things on your site, rescan with `R`, and check **History** to see the score go up.
6. Press `P` to open a printable report and save it as a PDF.

## Keyboard shortcuts

| Key | Action |
| --- | --- |
| `Alt+Shift+S` | Open SEO Lens (change it at `chrome://extensions/shortcuts`) |
| `R` | Rescan the current page |
| `1`-`9`, `0` | Jump to a tab |
| `P` | Open the printable report |
| `D` | Toggle dark / light theme |
| `?` | Show all shortcuts |

## Permissions explained

- **Side panel**: shows SEO Lens next to the page you are auditing.
- **Scripting**: reads the current page's HTML so it can be audited, only when the panel is open.
- **Storage**: keeps your audit history, settings and optional Gemini key on your own computer.
- **Access to all sites**: lets you audit any website, including localhost, and lets the link checker read real status codes.

Nothing is sent to the developer. The only network requests are the link status check (when you click it) and the optional Gemini audit (when you click it, using your own key).

## FAQ

**Does SEO Lens send my pages anywhere?**
No. Audits run inside your browser. Only the optional Gemini feature sends the page's title, description, keywords and headings to Google, and only when you click it.

**Why can't it audit some pages?**
Chrome does not let extensions read its own pages (such as `chrome://` pages and the Chrome Web Store) or the built-in PDF viewer. Open a normal website and it works.

**Is the schema check the same as Google's Rich Results Test?**
It is a quick check of the most important required and recommended properties for common types. For a final answer before you publish, confirm with Google's Rich Results Test.

# SEO Lens

**Tagline:** A complete on-page SEO audit in Chrome's side panel, updated as you browse.

## What it does

SEO Lens audits the page you are looking at and gives it a 0-100 SEO score with a prioritised list of fixes. It checks titles, descriptions, headings, links, images, structured data, social tags, speed and accessibility, shows what a search engine crawler gets for the URL, finds broken links, and shows what the site is built with. It re-scans automatically when you switch tabs or a single-page app changes the URL. Everything runs locally in your browser.

## Key features

- **Health score and "Road to 100%" checklist**: each fix shows how many points it is worth and what to change.
- **Tech stack** (new): see the CMS, ecommerce platform, frameworks, analytics and ad tags, consent banner, payments, CDN, hosting and web server behind any page, with versions, a confidence level and the evidence for each. 300+ technologies are recognised entirely on your device, with no lookups to any other service.
- **Crawler view** (new): the page's HTTP status and redirects, the `X-Robots-Tag` header, whether `robots.txt` blocks Googlebot (and which rule), and the sitemaps it lists, fetched the way a crawler would, without cookies.
- **Broken link checker** (new): checks every link on the page (up to 500) at once, shows 404s, unreachable links and redirects with their target, and lets you copy the broken ones. Filter by internal, external, nofollow, issues, broken or redirects, or search.
- **Titles that fit** (new): title and description width in pixels next to Google's truncation limits, not just character counts.
- **hreflang checks** (new): every language alternate, with invalid or duplicate codes, a missing self-reference and a missing `x-default` flagged.
- **Content, Performance, Links and Media tabs**: heading outline, keyword density, canonical and robots tags, timing, page weight, nofollow and generic anchors, unsafe `_blank` links and images without alt text.
- **Structured data checks**: JSON-LD is shown as a tree and checked for the fields Google needs for rich results (Product, Offer, Article, Organization, BreadcrumbList, FAQPage, Recipe, Event and more).
- **Social previews**: see the page as a Google result and as Facebook, X and LinkedIn cards, plus a list of missing Open Graph and X tags.
- **Score history**: every audit is saved on your device, so you can watch each page improve over time.
- **Printable report**: a clean report you can print or save as a PDF for clients, including crawler checks and broken links.
- **Scroll and highlight**: click "Show" to jump to a heading, link, image or control on the page.
- **Export**: JSON, CSV (safe to open in Excel or Sheets) or a Markdown summary.
- **Optional AI content-gap ideas** using your own Google Gemini API key.
- Dark and light themes, following your system setting on first run.

## How to use

1. Download and unzip the ZIP, open `chrome://extensions`, turn on **Developer mode** and click **Load unpacked**. Select the unzipped folder.
2. Pin SEO Lens and click its icon (or press `Alt+Shift+S`) to open the side panel.
3. Open any website. The panel scans it automatically.
4. Start with **Summary**: the Crawler view card tells you at once if the page can be indexed, and the checklist lists the biggest wins.
5. Open **Links** and click **Check links** to find broken links and redirects.
6. Fix things on your site, rescan with `R`, and check **History** to see the score go up.
7. Press `P` to open a printable report and save it as a PDF.

## Keyboard shortcuts

| Key | Action |
| --- | --- |
| `Alt+Shift+S` | Open SEO Lens (change it at `chrome://extensions/shortcuts`) |
| `R` | Rescan the current page |
| `1`-`9`, `0` | Jump to a tab |
| `T` | Open the Tech stack tab |
| `P` | Open the printable report |
| `D` | Toggle dark / light theme |
| `?` | Show all shortcuts |

## Permissions explained

- **Side panel**: shows SEO Lens next to the page you are auditing.
- **Scripting**: reads the current page's HTML so it can be audited, only when the panel is open.
- **Storage**: keeps your audit history, settings and optional Gemini key on your own computer. Web pages can't read it.
- **Access to all sites**: lets you audit any website, including localhost, and lets the link checker and crawler view read real status codes and headers.

Nothing is sent to the developer. Tech stack detection uses a signature list built into the extension; it reads cookie names, never their values. The only network requests are: the crawler view, which requests the audited page and its site's `robots.txt` without cookies (you can switch it to on-demand); the link checker (when you click it); and the optional Gemini audit (when you click it, using your own key).

## FAQ

**Does SEO Lens send my pages anywhere?**
No. Audits run inside your browser. Only the optional Gemini feature sends the page's title, description, keywords and headings to Google, and only when you click it.

**Why can't it audit some pages?**
Chrome does not let extensions read its own pages (such as `chrome://` pages and the Chrome Web Store) or the built-in PDF viewer. Open a normal website and it works.

**Why does the crawler view show a different status than my browser?**
It requests the page without your cookies, like Googlebot. A page that needs a login returns a redirect or a 401/403 to crawlers, so that's what you'll see. That is usually exactly what you want to know.

**How accurate is the pixel width?**
It measures your text in the fonts Google uses (about 600px for titles and 920px for descriptions on desktop). Google can still rewrite or shorten snippets, so treat it as a close guide.

**Why are some links shown as "unreachable"?**
The server didn't answer within 10 seconds, refused the connection, or the domain doesn't exist. Some sites also block automated requests; open the link to confirm.

**How does the tech stack detector work? Is it as complete as Wappalyzer?**
It compares the page's scripts, stylesheets, meta tags, markup, page variables, cookie names and server headers with a built-in list of 300+ technologies. Nothing is looked up online. Each result shows the evidence and a confidence level. Technologies that leave no trace in the page or its headers can't be seen, so treat it as a strong hint rather than a full inventory.

**Can I audit local files?**
Yes. Open `chrome://extensions`, click **Details** on SEO Lens and turn on **Allow access to file URLs**.

**Is the schema check the same as Google's Rich Results Test?**
It is a quick check of the most important required and recommended properties for common types. For a final answer before you publish, confirm with Google's Rich Results Test.

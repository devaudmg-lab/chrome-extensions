# SiteScope - Content Auditor

**Find every mention of any word, phrase or pattern across a whole website, right from your browser.**

## What it does

SiteScope crawls a website from inside your own browser and lists every page where your terms appear: in visible text, titles, meta descriptions, image alt text, aria-labels, placeholders and other HTML attributes. Because it runs in your browser session, it also works on staging sites, intranets and pages behind a login. Results stay on your computer.

## Key features

- Search up to 20 terms in a single crawl, with per-term match and page counts
- Exact, regular expression and fuzzy (typo-tolerant) matching
- Whole-site or single-page scans, up to 1,000 pages
- Reads sitemaps and robots.txt, skips files and URLs you exclude
- Gentle, Normal or Fast crawl speed
- Highlight in Context: open a page with every match marked and step through them
- Recheck one page after a fix, or re-run the whole audit with one click
- Export a shareable HTML report, CSV, JSON or PDF
- Optional JavaScript rendering for single-page apps
- No account, no server: audit history is stored locally in your browser

## How to use

1. Open any page of the site you want to audit.
2. Click the SiteScope icon (or press Alt+Shift+S).
3. Type your terms, one per line, and choose the search mode, scope, page limit and speed.
4. Click Start Audit (or press Ctrl+Enter) and watch the progress.
5. Click Dashboard to review results, filter by term, view match context, or highlight matches on the page.
6. Export a report, recheck pages you have fixed, or re-run the audit later.

## Keyboard shortcuts

- **Alt+Shift+S**: open the SiteScope popup (change it at chrome://extensions/shortcuts)
- **Ctrl+Enter** (Cmd+Enter on Mac): start the audit from the popup
- **/**: focus the URL filter in the dashboard; **Esc** clears it
- **Enter / Shift+Enter** (or F3 / Shift+F3): next / previous highlighted match on a page
- **Esc**: remove highlights from the page

## Permissions explained

- **Read and change data on websites**: needed to download the pages of the site you choose to audit. SiteScope only requests pages from the site you start the audit on.
- **Storage**: keeps crawl progress and your settings so nothing is lost if the browser pauses the extension.
- **Scripting**: adds the highlighter to a page when you click Highlight in Context, and reads rendered pages when JS rendering is on.
- **Offscreen**: uses a hidden extension page to read HTML quickly without opening visible tabs.

## FAQ

**Does SiteScope send my data anywhere?**
No. There is no server. Audit history lives in your browser, and the only requests made are to the website you are auditing.

**Can it audit pages behind a login or on a staging site?**
Yes. It crawls using your own browser session, so if you can open the pages, SiteScope can usually audit them.

**Will it overload the website?**
It respects robots.txt by default, backs off automatically when a server asks it to slow down, and lets you choose a Gentle speed that fetches one page at a time.

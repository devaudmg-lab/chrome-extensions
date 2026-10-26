# SEO Rank Finder

**Tagline:** See where your site ranks on Google for every keyword, and follow it over time.

## What it does

SEO Rank Finder checks Google for your keywords and tells you the exact position and page where your website appears, for example "#14, page 2". It saves every check, so you can see each keyword move up or down, and it can re-check your keywords daily or weekly and notify you when something changes. It runs in your own browser, with no account and no server.

## Key features

- **Bulk keyword checks**: paste many keywords, one per line or separated by commas.
- **Competitor comparison**: track a second domain in the same scan.
- **Rank history and charts**: every keyword gets a trend line, the change since last time and a full history chart.
- **Daily or weekly re-checks**: automatic checks with a notification when a position changes.
- **36 Google regions** plus "Auto" for your own location.
- **Search depth**: top 10, 30, 50 or 100 results.
- **Strict or broad mode**: organic results only, or include sublinks; featured snippets and People Also Ask are labelled.
- **Use the current site**: one click fills in the site you are on.
- **Stop and resume**: stop a long scan any time, and resume after solving a Google CAPTCHA.
- **CSV export** of the latest results and of your full history.

## How to use

1. Download and unzip the ZIP, open `chrome://extensions`, turn on **Developer mode** and click **Load unpacked**. Select the unzipped folder.
2. Pin SEO Rank Finder and click its icon (or press `Alt+Shift+K`) to open the side panel.
3. Enter your website (or click "Use yoursite.com"), choose a region and depth, and type your keywords.
4. Click **Find Position** or press `Ctrl+Enter`. The results show your position, the ranking page and the change since your last check.
5. Open the **Tracked** tab to see every keyword's history. Click a keyword for its chart.
6. Optional: set **Automatic re-checks** to Daily or Weekly to get notified when positions change.

## Keyboard shortcuts

| Key | Action |
| --- | --- |
| `Alt+Shift+K` | Open SEO Rank Finder (change it at `chrome://extensions/shortcuts`) |
| `Ctrl+Enter` / `Cmd+Enter` | Start the scan |
| `Esc` | Stop a running scan |

## Permissions explained

- **Side panel**: shows the tool next to the page you are on.
- **Scripting**: reads the result links from the Google results page it opens.
- **Storage**: keeps your settings and ranking history on your own computer.
- **Active tab**: reads the address of the current tab, only to offer it as your target site.
- **Alarms**: runs the daily or weekly re-check, only if you turn it on.
- **Notifications**: tells you when a re-check finds a ranking change.
- **google.com**: the only website the extension can access.

Nothing is sent to the developer or to any server other than Google.

## FAQ

**Why are my positions different from what a colleague sees?**
Google personalises results by location, language and login. SEO Rank Finder uses your own Google session, so pick the right region and compare checks made the same way.

**What happens if Google shows a CAPTCHA?**
The scan pauses and opens the Google tab so you can solve it. Then click **Resume Scanning**. Shallower scans (top 10 or 30) and fewer keywords at a time make CAPTCHAs less likely.

**Do automatic re-checks run when Chrome is closed?**
No. They run while Chrome is open, in a background tab that closes itself when done. Up to 25 keywords are re-checked per run.

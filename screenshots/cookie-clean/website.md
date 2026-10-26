# CookieClean

**Delete tracking cookies automatically and stay signed in to the sites you trust.**

## What it does

CookieClean removes a site's cookies when you close its last tab, so trackers can't follow you from one visit to the next. Sites you trust go on a whitelist and keep you logged in. The panel shows every cookie on the current site, the third-party trackers loaded by the page, and how much has been cleaned over time. Everything runs locally; nothing is collected or sent.

## Key features

- One-click purge of the current site's cookies, or delete single cookies, with **Undo**
- **Restore anything cleaned by mistake**: every cleanup, manual or automatic, can be put back until you close the browser
- **Wait before cleaning** (15 seconds by default): reopen a site in time and nothing is deleted
- Auto-clean when you close a site's last tab, and optionally when you navigate away
- **Trusted sites**, kept *Always* or *Until restart*, covering their subdomains and the shared cookies they use
- Sites open in any tab or window are never cleaned automatically
- **Third-party view**: see which ad and analytics domains on this page store cookies, and delete them
- Handles partitioned (CHIPS) cookies everywhere
- **Deep clean** (optional): also remove the site's localStorage, IndexedDB, cache and service workers
- **Scheduled cleaning** every hour, 6 hours or day, plus clean on browser startup (after open tabs are restored)
- Cookie Explorer with a high-risk filter for trackers and long-lived or insecure cookies
- Privacy score for the current site and a Cookie Age Limiter
- Stats: today, last 7 days, total, and a 14-day chart
- Optional "Clear cookies?" prompt instead of silent cleaning

## How to use

1. Install the extension and pin CookieClean from the puzzle-piece menu.
2. Browse as usual. When you close the last tab of a site, its cookies are deleted after a short wait.
3. On sites where you want to stay signed in, open CookieClean and click **Trust Site**. On the Whitelist tab you can switch a site to **Until restart** to stay signed in only for this browser session.
4. Cleaned something by mistake? Open **Settings › Recently Cleaned** (or the Restore strip on the Active Site tab) and click **Restore**.
5. Open **Third-party** on the Active Site tab to see and remove tracker cookies from the page you are on.
6. In **Settings**, choose the wait time and turn on Deep clean or Scheduled cleaning if you want more thorough or regular cleaning.

## Keyboard shortcuts

| Keys | Action |
| --- | --- |
| <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd> | Purge the current site's cookies without opening the panel (trusted sites are skipped) |
| <kbd>1</kbd>-<kbd>4</kbd> | Switch tabs in the panel |
| <kbd>/</kbd> | Search domains in the Explorer |
| <kbd>Ctrl</kbd>+<kbd>Z</kbd> | In the panel: undo the last manual or shortcut purge |

## Permissions explained

- **Cookies and access to all sites**: Chrome only lets an extension read and delete cookies for sites it has access to.
- **Storage**: keeps your settings, trusted sites and stats on your computer. Copies of recently cleaned cookies (for Restore) stay in memory only and vanish when the browser closes.
- **Notifications**: for the optional "Clear cookies?" prompt.
- **Alarms**: runs the Cookie Age Limiter, scheduled cleaning and cleanups after the wait time.
- **Browsing data**: used only by Deep clean, to remove the storage of the site being cleaned.
- **Scripting**: used only when you open the panel, to list which domains the current page loaded for the Third-party view. It doesn't change the page, and pages can't trigger any deletion.

## FAQ

**Will this log me out of everything?**
Only sites you leave and haven't trusted. Click **Trust Site** (or add domains on the Whitelist tab) for the accounts you want to keep, and their cookies are never cleaned automatically.

**I deleted cookies by mistake. Can I get them back?**
Yes. Every cleanup, including automatic ones when you close a tab, is listed under **Settings › Recently Cleaned** until you close the browser. Click **Restore**. Right after a manual purge you can also click **Undo** or press <kbd>Ctrl</kbd>+<kbd>Z</kbd>.

**I closed a tab by accident. Are my cookies gone?**
Not if you reopen it within the wait time (15 seconds by default, up to 5 minutes). And even after that, you can restore them.

**Will cleaning one site sign me out of another?**
No. Cookies used by a trusted site, or by a site open in another tab or window, are always kept. If `mail.example.com` is trusted, closing `news.example.com` keeps the shared `.example.com` cookies.

**Does CookieClean collect my data?**
No. It works completely offline, with no account, server or analytics.

# CookieClean

**Delete tracking cookies automatically and stay signed in to the sites you trust.**

## What it does

CookieClean removes a site's cookies when you close its last tab, so trackers can't follow you from one visit to the next. Sites you trust go on a whitelist and keep you logged in. The panel shows every cookie on the current site, the third-party trackers loaded by the page, and how much has been cleaned over time. Everything runs locally; nothing is collected or sent.

## Key features

- One-click purge of the current site's cookies, or delete single cookies, with **Undo**
- Auto-clean when you close a site's last tab, and optionally when you navigate away
- **Third-party view**: see which ad and analytics domains on this page store cookies, and delete them
- **Deep clean** (optional): also remove the site's localStorage, IndexedDB, cache and service workers
- **Scheduled cleaning** every hour, 6 hours or day, plus clean on browser startup
- Whitelist ("Safe Havens") that protects a domain and its subdomains, with import and export
- Cookie Explorer with a high-risk filter for trackers and long-lived or insecure cookies
- Privacy score for the current site and a Cookie Age Limiter
- Stats: today, last 7 days, total, and a 14-day chart
- Optional "Clear cookies?" prompt instead of silent cleaning

## How to use

1. Install the extension and pin CookieClean from the puzzle-piece menu.
2. Browse as usual. When you close the last tab of a site, its cookies are deleted.
3. On sites where you want to stay signed in, open CookieClean and click **Trust Site**.
4. Open **Third-party** on the Active Site tab to see and remove tracker cookies from the page you are on.
5. In **Settings**, turn on Deep clean or Scheduled cleaning if you want more thorough or regular cleaning.

## Keyboard shortcuts

| Keys | Action |
| --- | --- |
| <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd> | Purge the current site's cookies without opening the panel |
| <kbd>1</kbd>-<kbd>4</kbd> | Switch tabs in the panel |
| <kbd>/</kbd> | Search domains in the Explorer |
| <kbd>Ctrl</kbd>+<kbd>Z</kbd> | Undo the last purge (while the panel is open) |

## Permissions explained

- **Cookies and access to all sites**: Chrome only lets an extension read and delete cookies for sites it has access to.
- **Storage**: keeps your settings, whitelist and stats on your computer.
- **Notifications**: for the optional "Clear cookies?" prompt.
- **Alarms**: runs the Cookie Age Limiter and scheduled cleaning.
- **Browsing data**: used only by Deep clean, to remove the storage of the site being cleaned.
- **Scripting**: used only when you open the panel, to list which domains the current page loaded for the Third-party view. It doesn't change the page.

## FAQ

**Will this log me out of everything?**
Only sites you leave and haven't trusted. Click **Trust Site** (or add domains on the Whitelist tab) for the accounts you want to keep, and their cookies are never cleaned automatically.

**I deleted cookies by mistake. Can I get them back?**
Yes, while the panel is still open: click **Undo** in the message at the bottom or press <kbd>Ctrl</kbd>+<kbd>Z</kbd>.

**Does CookieClean collect my data?**
No. It works completely offline, with no account, server or analytics.

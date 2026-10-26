# DevShield

**Blocks ads, trackers and pop-ups on every site, privately, with nothing leaving your browser.**

## What it does

DevShield is an ad and tracker blocker for Chrome that also stops pop-unders, sneaky redirects and click hijacks. It uses well-known filter lists (EasyList, EasyPrivacy, uBlock Origin filters and more), and Chrome itself applies them. Blocking stays fast, and DevShield never sends your browsing anywhere.

## Key features

- Blocks ads, trackers and malware sites with EasyList, EasyPrivacy, uBlock Origin filters, Peter Lowe's list, URLhaus and regional lists
- Hides leftover ad boxes, sponsored widgets and "recommended" link farms
- Stops pop-ups, pop-unders, click hijacks and timed redirects, while links you really click still work
- Blocked history in the popup, with an **Open** button for anything you actually wanted
- YouTube: removes ads from videos, skips any that slip through, and can hide Shorts and Premium upsells
- Privacy: strips tracking tags (utm_*, fbclid, gclid…) from links and sends Global Privacy Control
- Per-site control: turn protection off for a site, allow one blocked host, or hide any element with the picker
- Pause everywhere for 15 minutes or an hour, and it turns itself back on
- Your own filters, plus one-click import from uBlock Origin or AdGuard

## How to use

1. Download the ZIP, extract it to a folder you'll keep, open `chrome://extensions`, turn on **Developer mode** and click **Load unpacked** (choose the folder that contains `manifest.json`).
2. Pin DevShield from the puzzle-piece menu. Protection is on straight away.
3. Click the shield to see what was blocked on the current page and your all-time totals.
4. If a site doesn't work right, flip the site switch in the popup (or press `Alt+Shift+D`) to trust it.
5. If a pop-up you wanted was blocked, click **Open** in the notice or in the popup's Activity list.
6. Coming from uBlock Origin or AdGuard? Open **Settings → My filters → Import…** and choose your exported filters or backup file.

## Keyboard shortcuts

| Keys | Action |
|---|---|
| `Alt+Shift+D` | Turn protection on or off for the current site |
| `S` (in the popup) | Turn protection on or off for this site |
| `B` (in the popup) | Block an element on the page |
| `O` (in the popup) | Open settings |

You can also give shortcuts to "on/off everywhere" and "Block element" at `chrome://extensions/shortcuts`.

## Permissions, in plain words

| Permission | Why DevShield needs it |
|---|---|
| Read and change data on all sites | To block ads and hide ad boxes on any site you visit. |
| Block content (declarativeNetRequest) | Lets Chrome itself block ad and tracker requests using the built-in lists. |
| Scripting | Adds the ad-hiding styles, pop-up guard and element picker to pages. |
| Web requests (observe only) | Counts what was blocked so the popup can show it. Nothing is changed or sent. |
| Web navigation | Resets the counters on each page and closes pop-under tabs that sites open. |
| Storage | Keeps your settings, counters and history on your computer. |
| Alarms | Ends a timed pause and updates lists you subscribed to. |
| Context menus | The right-click "Block element…" and "Trust this site" entries. |

DevShield has no accounts, no analytics and no telemetry. The only downloads it makes are extra filter lists that you add yourself.

## FAQ

**A site is broken or says "please disable your ad blocker". What do I do?**
Click the DevShield icon and turn off the switch next to the site name, or press `Alt+Shift+D`. The page reloads with DevShield off for that site only. Flip it back on whenever you like.

**I clicked something and nothing opened. Did DevShield block it?**
Possibly. If a page tried to open a pop-up without your click, DevShield blocks it and shows a small notice. Click **Open** in that notice, or in the Activity list in the popup, to open it anyway.

**Can I keep my uBlock Origin or AdGuard rules?**
Yes. Export "My filters" (or a full backup) from uBlock Origin or AdGuard, then in DevShield go to **Settings → My filters → Import…**. Your filters are added, duplicates are skipped, and any trusted sites in a backup are added to your trusted sites.

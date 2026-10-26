# Blur Remover & DOM Modifier

**Tagline:** Clear blurred pop-ups, frozen scrolling and clutter, and read the page you came for.

## What it does

Blur Remover clears blurred backdrops, newsletter and cookie pop-ups and locked scrolling, so the page underneath is usable again. Point at anything that gets in your way and it builds a rule for that site, or open the page in a clean Reader View. It also adds a proper dark mode and your own CSS tweaks, per site or everywhere.

## Key features

- Magic auto-unblur: finds real blur overlays from the page's computed styles and clears them, leaving normal design alone.
- Presets for scroll unlock, overlay eraser, cookie banner and newsletter pop-up removal, unblurred text and re-enabled copy and right-click.
- Element picker with suggested stable selectors, live match counts, one-off "zap" and Ctrl+Z undo.
- Reader View with table of contents, read-aloud, highlights and notes, Markdown/HTML export, print to PDF and readable fonts.
- Dark mode per site: a fast filter mode or a dynamic mode that keeps brand colours, with brightness, contrast and schedule.
- Pause on any site, permanently or for 30 minutes (it switches back on by itself).
- Export a site's rules as a small rule pack file to share or import on another computer.
- Rule packs, statistics, backup and restore, and an optional count badge on the toolbar icon.

## How to use

1. Download the ZIP, unzip it to a folder you'll keep, open `chrome://extensions`, turn on Developer mode and click **Load unpacked**.
2. Pin Blur Remover from the puzzle-piece menu.
3. Visit a page with a blurred pop-up or frozen scrolling. Magic auto-unblur works straight away; press **Alt+U** for a stronger instant unblur.
4. Still something in the way? Press **Alt+P**, click the element and save a rule. It's fixed every time you come back.
5. Press **Alt+R** to read the article in Reader View.
6. Open the popup to switch presets, dark mode or rules, or to pause the site for 30 minutes.

## Keyboard shortcuts

| Shortcut | Action |
| --- | --- |
| Alt+U | Instant unblur for this tab |
| Alt+P | Element picker |
| Alt+R | Reader View |
| Alt+Shift+D | Dark mode on or off for this site |
| Ctrl+Z | Undo the last zapped element or picked rule |
| (your choice) | Pause or resume on this site, set it at `chrome://extensions/shortcuts` |

## Permissions, in plain words

- **Read and change data on all websites**: needed to remove blurs and pop-ups and apply your rules on whatever site you visit.
- **Storage**: keeps your settings, rules, statistics and Reader View highlights on your computer (core settings sync through your Chrome account).
- **Scripting**: loads the element picker and Reader View into a page only when you use them.
- **Context menus**: the right-click items (pick or zap an element, Reader View, dark mode, pause the site).
- **Alarms**: updates rule packs once a day and switches a site back on when a 30-minute pause ends.

No accounts, no analytics, no server of ours. Nothing you read is sent anywhere.

## FAQ

**Will it break sites?**
Magic auto-unblur only touches elements that are really blurred overlays. If a site looks wrong, pause Blur Remover there from the popup, for good or for 30 minutes.

**Can I share my fixes for a site?**
Yes. In the popup, open Rules and click "Export this site's rules". The file can be imported in Options > Backup on another computer; only the rules are added.

**Does it get around paid subscriptions?**
No. It removes visual clutter that sits on top of content already loaded in your browser, such as blurred pop-ups and locked scrolling. It doesn't unlock content a site hasn't sent you.

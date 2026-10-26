# Pro Auto Scroller

**Hands-free, smooth auto scrolling for anything you read in Chrome.**

## What it does
Pro Auto Scroller scrolls the page for you at a steady, adjustable pace, so you can read long articles, follow a recipe with flour on your hands, or play along with chords and lyrics. A small floating bar lets you pause, change speed and see how much reading time is left. Each site remembers the speed you like.

## Key features
- Smooth scrolling from a slow crawl to fast skimming, the same on any screen refresh rate
- Floating speed bar with play/pause, slower/faster, progress and time-left estimate
- Press `+` / `-` to change speed while you read, `Esc` to stop
- Remembers a separate speed for every site
- Spacebar play/pause (ignored while you type)
- Works in web apps that scroll an inner panel (chat apps, docs viewers)
- Stops at the end of the page, but waits for infinite feeds to load more
- Light and dark mode popup; nothing is collected or sent anywhere

## How to use
1. Download the ZIP, unzip it, open `chrome://extensions`, turn on **Developer mode** and click **Load unpacked**. Pick the unzipped folder.
2. Open any article and press **Space** (or open the popup and drag the speed slider).
3. Use the floating bar or `+` / `-` to find a comfortable speed. It's saved for that site.
4. Press **Space** to pause and resume, or **Esc** to stop.

## Keyboard shortcuts
| Keys | Action |
|---|---|
| `Space` (on the page) | Start / pause |
| `+` / `-` (while scrolling) | Faster / slower |
| `Esc` (while scrolling) | Stop |
| `Alt+Shift+S` | Toggle scrolling from anywhere |
| `Alt+Shift+Up` / `Alt+Shift+Down` | Faster / slower |

You can change the `Alt+Shift` shortcuts at `chrome://extensions/shortcuts`.

## Permissions explained
- **Runs on http and https pages**: needed so Space and the shortcuts work on whatever you're reading. It only scrolls the page; it doesn't read or send page content.
- **activeTab and scripting**: lets the popup switch the scroller on in a tab that was already open before you installed it.
- **storage**: saves your settings and per-site speeds on your own computer.

## FAQ
**Does Space still work normally on pages?**
On normal pages Space starts and pauses scrolling instead of jumping a screen down. It's ignored in text boxes, and you can turn it off in the popup.

**Why doesn't it work on some pages?**
Chrome blocks all extensions on `chrome://` pages, the Chrome Web Store and a few other built-in pages. The popup tells you when that's the case.

**Will `+` and `-` interfere with websites that use those keys?**
No. They only change speed while the scroller is running on that page. When it's stopped, the keys go to the website as usual.

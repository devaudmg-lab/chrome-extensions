# Pro Auto Scroller

**Hands-free, smooth auto scrolling for anything you read in Chrome.**

## What it does
Pro Auto Scroller scrolls the page for you at a steady, adjustable pace, so you can read long articles, follow a recipe with flour on your hands, or play along with chords and lyrics. A small floating bar lets you pause, change speed and see how much reading time is left. Each site remembers the speed you like.

## Key features
- Smooth scrolling from a slow crawl to fast skimming, the same on any screen refresh rate
- Floating speed bar with play/pause, slower/faster, progress and time-left estimate
- Press `+` / `-` to change speed while you read, `Esc` to stop
- Remembers a separate speed for every site
- Space pauses and resumes once the scroller runs, and leaves Space alone otherwise (page down, videos, games keep working). Opt in to let Space start it anywhere
- Finish the page in N minutes: it picks the exact speed for you
- Auto-start on the sites you choose (lyrics, chords, recipes)
- Works in web apps that scroll an inner panel (chat apps, docs viewers) and on smooth-scroll sites
- Stops at the end of the page, but waits for infinite feeds to load more
- Light and dark mode popup; nothing is collected or sent anywhere

## How to use
1. Download the ZIP, unzip it, open `chrome://extensions`, turn on **Developer mode** and click **Load unpacked**. Pick the unzipped folder.
2. Open any article and press **Alt+Shift+S** (or open the popup and drag the speed slider, or type minutes into **Finish page in**).
3. Use the floating bar or `+` / `-` to find a comfortable speed. It's saved for that site.
4. Press **Space** to pause and resume, or **Esc** to stop.

## Keyboard shortcuts
| Keys | Action |
|---|---|
| `Space` (while the scroller runs) | Pause / resume |
| `+` / `-` (while scrolling) | Faster / slower |
| `Esc` (while scrolling) | Stop |
| `Alt+Shift+S` | Start / pause from anywhere |
| `Alt+Shift+Up` / `Alt+Shift+Down` | Faster / slower |

You can change the `Alt+Shift` shortcuts at `chrome://extensions/shortcuts`.

## Permissions explained
- **Runs on http and https pages**: needed so Space and the shortcuts work on whatever you're reading. It only scrolls the page; it doesn't read or send page content.
- **activeTab and scripting**: lets the popup switch the scroller on in a tab that was already open before you installed it.
- **storage**: saves your settings, per-site speeds and auto-start sites on your own computer.

## FAQ
**Does Space still work normally on pages?**
Yes. Until you start the scroller on a page, Space does what it always does: page down, play a video, jump in a game. Once it runs, Space pauses and resumes it, unless the page itself uses Space or a button or video has focus. If you'd rather have Space start scrolling everywhere, turn on **Space also starts scrolling on any page** in the popup.

**How does "Finish page in" work?**
It measures how much of the page is left and sets the speed that gets you to the end in that many minutes. If that would need more than the 10x maximum, it tells you.

**Can it start by itself?**
Only on sites you choose. Tick **Auto-start on (site)** in the popup and pages of that site start scrolling a moment after they load.

**Why doesn't it work on some pages?**
Chrome blocks all extensions on `chrome://` pages, the Chrome Web Store and a few other built-in pages. The popup tells you when that's the case.

**Will `+` and `-` interfere with websites that use those keys?**
No. They only change speed while the scroller is running on that page. When it's stopped, the keys go to the website as usual.

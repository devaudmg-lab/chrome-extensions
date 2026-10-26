# ScrollShot Pro

**Scrolling screenshots of exactly the part of the page you want.**

## What it does
ScrollShot Pro captures more than fits on your screen. Draw a box around a table, click a chat thread or code panel, or grab the whole page, and ScrollShot scrolls for you and stitches everything into one clean image. Before you share it, you can crop it, blur private details, point things out with arrows and labels, and highlight what matters.

## Key features
- Region capture that scrolls: select any area, even taller than the screen
- Click any scroll area (chat threads, code viewers, sidebars) to capture all of it
- Full page in one click, without repeated sticky headers or sidebars, and with lazy-loaded images filled in
- Very long pages are kept whole (scaled to fit Chrome's image size limit instead of cut off)
- Visible-area capture when you just want what's on screen
- Built-in editor: crop, blur (pixelate), red box, arrow, yellow highlight and text labels, with undo
- Copy to clipboard or download as PNG, JPG, WebP or a multi-page PDF with tidy automatic file names
- Capture history: your last 25 captures stay on your computer, ready to download again
- Optional 3, 5 or 10 second delay to capture menus and hover states
- Everything runs locally; nothing is uploaded

## How to use
1. Download the ZIP, unzip it, open `chrome://extensions`, turn on **Developer mode** and click **Load unpacked**. Pick the unzipped folder, then pin ScrollShot Pro.
2. Click the ScrollShot icon and choose **Region Scroll Capture**, **Full Page** or **Visible Area**.
3. For a region, drag a box or click a highlighted scroll area, then press **Enter**.
4. In the preview, crop, blur, highlight or add arrows and text if you like.
5. Pick a format (PNG, JPG, WebP or PDF) and click **Download**, or **Copy to Clipboard**. Find older captures under **View all** in the popup.

## Keyboard shortcuts
| Keys | Action |
|---|---|
| `Ctrl+Shift+S` (`Cmd+Shift+S` on Mac) | Start a region capture |
| `Alt+Shift+F` | Capture the full page |
| `Alt+Shift+V` | Capture the visible area |
| `Enter` | Capture the selected box |
| `Esc` | Cancel the countdown, selection or capture |
| `C` / `B` / `R` / `A` / `H` / `T` | Crop / Blur / Box / Arrow / Highlight / Text in the preview |
| `Ctrl+Z` | Undo the last edit |

## Permissions explained
- **activeTab**: lets ScrollShot see and capture only the tab you're on, and only after you click its icon or press its shortcut. It can't read other sites.
- **scripting**: adds the selection box and capture toolbar to that tab.
- **offscreen**: stitches the screenshots together on a hidden canvas inside your browser.
- **downloads**: saves the finished image or PDF to your computer.
- **storage**: remembers your export format, delay, whether to ask where to save, and that you've seen the welcome tips.

Your captures are processed and stored locally (history uses the extension's own browser storage). Nothing is sent anywhere.

## FAQ
**What happens with a very long page?**
Chrome can't create images taller than about 32,000 pixels. Instead of cutting the page off, ScrollShot scales the capture down so all of it fits, and the preview tells you. If you need full resolution, capture the page in parts with Region capture.

**Can a website see my screenshot?**
No. The preview and editor are sealed off from the page's own scripts, and the image never appears in the page. Your captures stay in the extension's own storage on your computer.

**What if I switch tabs during a capture?**
ScrollShot pauses and continues when you come back. It never stitches another tab into your image.

**Can it save without asking where every time?**
Yes. Untick **Ask where to save each download** in the popup.

**Can I capture a chat or code panel that scrolls on its own?**
Yes. Start a region capture and click the panel when it's highlighted green, and ScrollShot captures its whole content.

**Is the blur safe for passwords or personal details?**
Blur pixelates the area in the exported image itself, so the original text isn't in the file. For anything very sensitive, use a large blur box or crop it out entirely.

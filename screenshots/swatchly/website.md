# Swatchly: Eyedropper & Page Palette

**Tagline:** Pick, collect and check the colours of any web page.

## What it does
Swatchly is a small colour tool for designers, developers and anyone who needs "that exact colour". Pick any pixel on your screen, see every colour a website uses, check whether text is readable against its background, and copy colours as HEX, RGB or HSL in one click.

## Key features
- **Eyedropper**: pick a colour from anywhere on screen and it is copied instantly
- **Page palette**: every colour the page uses, most used first, with filters for backgrounds, text & icons and borders
- **Export**: copy the palette as CSS variables, JSON or a plain list, or download a .json file
- **Contrast checker**: WCAG AA and AAA results for normal text, large text and UI elements
- **One-click contrast fix**: suggests the closest text colour that passes, in the same hue
- **History** of your last 32 colours
- **Paint page**: preview a new background colour on the page, then undo it
- HEX, RGB and HSL formats, light and dark popup, full keyboard support
- No account, no tracking, nothing sent anywhere

## How to use
1. Install Swatchly and pin it to your toolbar.
2. Open any web page and click the Swatchly icon (or press **Alt+Shift+C**).
3. Click **Pick colour** and click anywhere on screen. The colour is copied.
4. Open **Page palette** to see the page's colours. Click one to copy it, or use **Export** to copy them all.
5. Open **Contrast**, pick a text colour and a background colour, and read the result. Click **Apply** to use the suggested fix.
6. Choose **HEX**, **RGB** or **HSL** at the top to change the copy format.

## Keyboard shortcuts
- **Alt+Shift+C**: open Swatchly
- **E**: start the eyedropper (in the popup)
- **C**: copy the current colour (in the popup)
- **Esc**: cancel the eyedropper
- **Left / Right arrows**: move between tabs and options
- **Delete**: remove a colour from history

## Permissions, explained simply
- **Active tab**: only when you open Swatchly, it may read the colours of the page you are looking at, or change its background when you click Paint page. Other tabs are never touched.
- **Scripting**: runs Swatchly's own built-in palette scan in that tab. Nothing is downloaded from the internet.

Swatchly does not ask to "read and change all your data on all websites". The eyedropper is built into the browser and needs no permission.

## FAQ
**Why can't I see a palette on some pages?**
Chrome does not let any extension read its own pages (like Settings), the Chrome Web Store or the built-in PDF viewer. The eyedropper still works on those pages.

**Does it work on local files?**
Yes, after you turn on "Allow access to file URLs" for Swatchly on the chrome://extensions page.

**Are colours from images included in the palette?**
No. The palette lists colours from the page's styles (backgrounds, text, borders, icons and gradients). Use the eyedropper to pick colours from photos or videos.

**Is my data collected?**
No. Your history and settings stay on your computer, and nothing is sent anywhere.

**How is "Paint page" different from a dark mode?**
It only previews one background colour on the current page until you undo it or reload. It is a quick way to test a colour, not a theme.

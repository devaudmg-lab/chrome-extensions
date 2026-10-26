# Universal Form Autofiller

**Fill any web form with realistic test data in one click, or automatically every time your test site loads.**

## What it does

Universal Form Autofiller fills sign-up, checkout and settings forms with believable people, addresses, unique emails and payment-gateway test cards. It works with React, Vue and Angular apps, shadow DOM, iframes and rich-text editors. If a form needs real context, such as a medical intake or insurance questionnaire, it can ask Google Gemini to fill it using your own API key.

## Key features

- **One-click fill** for text fields, selects, radios, checkboxes, dates, textareas and rich-text editors, in every frame on the page.
- **Auto-fill on page load**: switch it on for a site and every page is filled as soon as it loads, including route changes in single-page apps (empty fields only, never with AI), with a toast that shows how to undo.
- **Realistic test data**: 30 built-in personas or a new person on every fill, in 15 locales, with matching country, state and phone formats.
- **Fill as a chosen persona**, or rotate through them, from the popup.
- **Unique emails and usernames** with plus-addressing (`you+ff…@gmail.com`), timestamps or random suffixes.
- **Gateway test cards** for Stripe, Braintree, Adyen and PayPal, including declined and 3-D Secure cards, always with a future expiry.
- **Right-click any field**: **Fill this field** fills just that one (even if it has a value), and **Insert test value** types a name, unique email, phone, address, strong password, paragraph, or an edge case (too long, emoji, RTL, padded spaces, XSS or SQL probe). Undo works on both.
- **On-page feedback**: fills started with a shortcut or the right-click menu show a short toast with the result and the undo shortcut.
- **Keep / Change / Skip each field** from the side panel, so you can keep a name and only change the email on every run.
- **Undo and Clear**, plus **Edge-case mode** with long, Unicode, RTL and SQL/XSS probe strings for negative testing.
- **URL rules and custom mappings** to set fixed values for specific pages or fields.
- **Optional Gemini AI** for forms that need context, with your own key.
- **Export / Import** your settings to share them with your team (the API key is never exported).

## How to use

1. Download the ZIP, extract it, open `chrome://extensions`, turn on **Developer mode**, click **Load unpacked** and choose the extracted folder.
2. Pin FormFiller from the puzzle-piece menu.
3. Open any page with a form and click the FormFiller icon.
4. Click **Fill Current Form** (or press `Ctrl + Shift + F`). Use **Undo** if you want the old values back.
5. Optional: pick a persona under **Fill as**, or turn on **Auto-fill this site on load** for your staging or local site.
6. Optional: click **Keep / Change** to open the side panel and lock the fields you want to keep the same.
7. Right-click a single field for **Fill this field** or **Insert test value** (for example a unique email or an XSS probe).

## Keyboard shortcuts

| Action | Windows / Linux | Mac |
|---|---|---|
| Open the FormFiller popup | `Alt + Shift + F` | `Option + Shift + F` |
| Fill the form (empty fields only, by default) | `Ctrl + Shift + F` | `Control + Shift + F` |
| Fill using AI | `Ctrl + Shift + Y` | `Control + Shift + Y` |
| Undo last fill | `Alt + Shift + U` | `Option + Shift + U` |
| Keep / Change / Skip the focused field | `Alt + L` | `Option + L` |

You can change these at `chrome://extensions/shortcuts`.

## Permissions explained

| Permission | Why |
|---|---|
| Read and change data on all websites | To find and fill form fields on the pages you choose, including forms inside iframes. Fields are only touched when you start a fill, use the side panel or `Alt + L`, or on a site where you turned on auto-fill. |
| Active tab and scripting | To add the filler to tabs that were open before you installed or updated the extension. |
| Web navigation | To find every frame on a page, and to know when a page on an auto-fill site has finished loading. |
| Storage | To save your settings, personas, rules and field modes in your browser. This storage is closed to the websites you visit and to the extension's own scripts on those sites. |
| Context menus | For the right-click menu (fill the form or one field, insert a test value, overwrite, undo, clear, open the panel). |
| Side panel | For the Keep / Change / Skip panel. |
| generativelanguage.googleapis.com | Only for AI fills, to call Gemini with your own key. |

## FAQ

**Does it send my data anywhere?**
No. There is no server and no analytics. Everything stays in your browser. Only if you turn on Gemini AI are field labels and options (never values, passwords or card fields) sent to Google with your key.

**Are the card numbers real?**
No. They are the public test numbers that Stripe, Braintree, Adyen and PayPal publish for sandbox testing. They pass format checks but can't be charged.

**Will auto-fill overwrite what I typed?**
No. Auto-fill only fills empty fields, never uses AI, and shows a toast with the undo shortcut. You can turn it off for a site in the popup or remove sites in Options.

**Where is my Gemini API key kept?**
In this browser's extension storage, which only FormFiller's own pages and background can read. The scripts FormFiller runs on websites can't read it, it never appears in a page, and it is never exported. It is sent only to Google, in a request header, when you run an AI fill or click **Test key**.

**What does the page see when I use AI?**
Only the values that end up in its form fields, exactly as if you had typed them. Gemini's answer is never placed anywhere else in the page.

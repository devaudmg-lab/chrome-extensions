# Meta Competitor Intelligence

**Turn the public Meta Ad Library into your own private, searchable swipe file of competitor ads.**

## What it does

Meta Competitor Intelligence adds Save buttons to every ad in the Meta Ad Library and keeps the ads you save in a side panel next to the page. You can add notes, tags and folders, see how split-test variations differ, and spot patterns such as the ads that have been running the longest. Everything is stored locally in your browser.

## Key features

- One-click Save Ad and Save Brand buttons on every Ad Library card, with already-saved ads marked
- Collect All: scrolls a search and saves up to 500 ads automatically
- Split-test grouping with highlighted headline and copy changes
- Private notes on any ad, plus folders and tags with an inline picker
- One search box for copy, headlines, brands, CTAs, landing domains, tags and notes
- Days live on every ad, using the real end date for ads that stopped
- Insights: longest-running ads, launches per month, calls to action, landing domains, video share and brand comparison
- Watch brands, take a snapshot, and see which ads are new later
- Thumbnails stored locally, so saved ads keep their images after Meta's links expire
- Landing page and UTM tracing for every call to action
- Optional AI copy analysis with your own Gemini or OpenAI key
- Export to CSV, Excel or a self-contained HTML swipe report
- Full backup and restore: ads, notes, tags, folders, watched brands and history in one JSON file

## How to use

1. Open the Meta Ad Library and search for a competitor or keyword.
2. Click the extension icon (or press Alt+Shift+M) to open the side panel.
3. Click Save Ad or Save Brand on any ad, or start Collect All from the Search tab.
4. Open the Ads tab to search, tag, file and compare saved ads. Use 📝 Note to write down why an ad works.
5. Open Insights to see long-running ads, launch timing, CTAs and landing pages.
6. Watch important brands, take a snapshot, and use Check now later to spot new ads.

## Keyboard shortcuts

- **Alt+Shift+M**: open the side panel (change it at chrome://extensions/shortcuts)
- **/**: search your saved ads
- **Alt+1 to Alt+6**: switch between the panel tabs
- **Esc**: close the folder/tag picker or clear the search
- **Enter**: create the folder or tag you typed in the picker
- **Ctrl+Enter**: save the note you are writing

## Permissions explained

- **Meta Ad Library pages**: adds the Save buttons and reads the ads you choose to save.
- **l.facebook.com**: reads Meta's outbound links to show each ad's real landing page.
- **fbcdn.net**: loads ad images so thumbnails can be stored and reports can include them.
- **Side panel**: shows your workspace beside the Ad Library.
- **Storage**: keeps your settings on this computer. Web pages cannot read it, including an optional AI key.
- **Downloads**: saves your exports and, if you want, copies of ad creatives.

## FAQ

**Is my data uploaded anywhere?**
No. Saved ads, brands and settings stay in your browser. The only exception is optional AI analysis, which sends an ad's text to the AI provider you choose, using your own API key.

**Does it work on Facebook itself or only the Ad Library?**
Only the public Meta Ad Library. It does not read your feed, messages or account.

**How does it know which ads are split tests?**
It groups ads from the same brand that share the same copy or the same image (an image fingerprint that tells apart different creatives made from one template), then shows what each variation changes.

**Does it contact the advertisers' websites?**
No. The landing page is read from Meta's own outbound link, so no request is sent to the advertiser. Images are only loaded from Meta's CDN.

**How do I move my swipe file to another computer?**
Click Backup (JSON) on the Search tab, then Restore backup on the other computer. Notes, tags, folders, watched brands and thumbnails come along. Restoring merges with what is already there.

**Can websites see what I saved?**
The Save buttons and badges on the Ad Library live in a closed part of the page, so the site's scripts cannot read which ads you saved or which brands you watch. Your data stays in the extension.

This extension is not affiliated with or endorsed by Meta.

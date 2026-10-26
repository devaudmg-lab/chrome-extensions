# Musicox

**Background music from YouTube videos, YouTube playlists and audio streams. Close the popup and keep listening.**

## What it does

Musicox is a small music player that lives in your Chrome toolbar. Paste a YouTube video, a whole YouTube playlist or an internet radio / audio URL, press play, and close the popup: the music keeps going while you work in other tabs. Build your own queue that mixes YouTube and audio links, and set a sleep timer when you're winding down.

## Key features

- **Plays whole YouTube playlists**: paste any link with `list=` and you get every video, with next / previous and a *4 / 12* position. Click any video in the list to jump to it.
- **Your own queue**: mix YouTube videos, playlists and audio URLs. Paste several links at once, drag to reorder, remove with one click.
- **Shuffle and repeat** (off, all, or this track), and the next track starts by itself.
- **Seek bar** with elapsed time and duration.
- **Sleep timer**: 15 to 90 minutes or *end of track*, with a gentle fade-out.
- **Keyboard shortcuts** for play/pause, next and previous, from any tab.
- **Picks up where you left off**, even inside a playlist.
- **Recent tracks**, a **Use tab** button for the page you're on, and clear messages when a video can't be played.
- **Private**: no account, no server, no analytics.

## How to use

1. Install Musicox (unzip, then **Load unpacked** at `chrome://extensions` with Developer mode on) and pin it to the toolbar.
2. Click the Musicox icon and paste a YouTube video, YouTube playlist or audio stream URL.
3. Press **▶** to play it now, or **+ Queue** to line it up (you can paste several links at once).
4. Close the popup. The music keeps playing.
5. Open the **Queue** tab to reorder or jump around, and the **Settings** tab to set a sleep timer.

## Keyboard shortcuts

| Shortcut | Action |
| --- | --- |
| Alt+Shift+P | Play / pause |
| Alt+Shift+N | Next track |
| Alt+Shift+B | Previous track |
| Alt+Shift+M | Open Musicox |

In the popup: Space play/pause, ← / → seek 10 seconds, N / P next/previous, S shuffle, R repeat. You can change the shortcuts at `chrome://extensions/shortcuts`.

## Permissions explained

- **Offscreen document**: a hidden page that plays the audio, so music continues after the popup closes.
- **Storage**: remembers your queue, volume, settings and recent tracks on your computer only.
- **Active tab**: reads the current tab's address only when you click **Tab**.
- **Access to www.youtube.com**: lets YouTube's embedded player work inside the extension and looks up video titles. Musicox does not read or change the YouTube pages you visit.

## FAQ

**Does Musicox skip YouTube ads?**
No. YouTube may play an ad before some videos, just like on its site. Musicox doesn't block or skip them. The music starts when the ad ends.

**Why won't a particular video play?**
Some video owners (often music labels) don't allow their videos to be played outside YouTube. Musicox shows a clear message, and inside a playlist it skips to the next video.

**Can I play internet radio or my own MP3 links?**
Yes. Any direct audio address (MP3, AAC, OGG or a radio stream) works and can sit in the same queue as YouTube links.

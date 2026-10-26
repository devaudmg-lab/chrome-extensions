# Musicox

**Background music from YouTube videos, YouTube playlists and audio streams. Close the popup and keep listening.**

## What it does

Musicox is a small music player that lives in your Chrome toolbar. Paste a YouTube video, a whole YouTube playlist or an internet radio / audio URL, press play, and close the popup: the music keeps going while you work in other tabs. Build your own queue that mixes YouTube and audio links, save it as a playlist for later, and set a sleep timer when you're winding down.

## Key features

- **Plays whole YouTube playlists**: paste any link with `list=` and you get every video, with next / previous and a *4 / 12* position. Click any video in the list to jump to it.
- **Your own queue**: mix YouTube videos, playlists and audio URLs. Paste several links at once, drag to reorder, remove with one click. **Play next** (Alt+Enter) puts a link right after the current track.
- **Saved playlists**: save the queue under a name, load it again in one click, or add it to what's playing. **Copy links** exports the queue as a list of links.
- **Keeps going**: a video that can't be embedded or a broken stream is skipped with a short note instead of stopping your queue.
- **Shuffle and repeat** (off, all, or this track), and the next track starts by itself.
- **Seek bar** with elapsed time and duration.
- **Sleep timer**: 15 to 90 minutes or *end of track*, with a gentle fade-out. Press play during the fade to cancel it.
- **Volume and mute**, with keyboard control in the popup.
- **Keyboard shortcuts** for play/pause, next and previous, from any tab.
- **Picks up where you left off**, even inside a playlist.
- **Recent tracks**, a **Use tab** button for the page you're on, and clear messages when a video can't be played.
- **Private**: no account, no server, no analytics.

## How to use

1. Install Musicox (unzip, then **Load unpacked** at `chrome://extensions` with Developer mode on) and pin it to the toolbar.
2. Click the Musicox icon and paste a YouTube video, YouTube playlist or audio stream URL.
3. Press **▶** to play it now, or **+ Queue** to line it up (you can paste several links at once).
4. Close the popup. The music keeps playing.
5. Open the **Queue** tab to reorder or jump around, or press **Save** to keep the queue as a playlist. The **Settings** tab has the sleep timer.

## Keyboard shortcuts

| Shortcut | Action |
| --- | --- |
| Alt+Shift+P | Play / pause |
| Alt+Shift+N | Next track |
| Alt+Shift+B | Previous track |
| Alt+Shift+M | Open Musicox |

In the popup: Space play/pause, ← / → seek 10 seconds, ↑ / ↓ volume, M mute, N / P next/previous, S shuffle, R repeat. In the link field: Enter plays, Shift+Enter adds to the queue, Alt+Enter plays next. You can change the shortcuts at `chrome://extensions/shortcuts`.

## Permissions explained

- **Offscreen document**: a hidden page that plays the audio, so music continues after the popup closes.
- **Storage**: remembers your queue, saved playlists, volume, settings and recent tracks on your computer only.
- **Active tab**: reads the current tab's address only when you click **Tab**.
- **Access to www.youtube.com**: lets YouTube's embedded player work inside the extension and looks up video titles. Musicox does not read or change the YouTube pages you visit.

## FAQ

**Does Musicox skip YouTube ads?**
No. YouTube may play an ad before some videos, just like on its site. Musicox doesn't block or skip them. The music starts when the ad ends.

**Why won't a particular video play?**
Some video owners (often music labels) don't allow their videos to be played outside YouTube. Musicox shows a clear message, and inside a playlist it skips to the next video.

**Can I play internet radio or my own MP3 links?**
Yes. Any direct audio address (MP3, AAC, OGG or a radio stream) works and can sit in the same queue as YouTube links.

**How do I keep a queue for later?**
Open the **Queue** tab and press **Save**, then give it a name. Your saved playlists are listed under the queue: click one to play it, or press **+** to add it to the end of the current queue. Saving again under the same name updates it.

**What happens if I remove the song that's playing?**
It finishes, and then the queue continues with the song that came after it.

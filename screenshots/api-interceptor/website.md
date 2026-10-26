# API Interceptor Pro

**Inspect and mock your app's API calls right inside Chrome DevTools, with no proxy to set up.**

## What it does

API Interceptor Pro adds an **API Monitor Pro** tab to Chrome DevTools that lists every `fetch` and `XMLHttpRequest` call a page makes, with headers, payloads and pretty-printed responses. With one click you can turn any request into a mock rule and return your own status, body, headers and delay, so you can build and test empty, slow and error states before the backend is ready. Everything runs locally in your browser.

## Key features

- Live list of fetch/XHR calls with method, status, latency and type, plus filters for Fetch, XHR, GraphQL, Mocked and Errors
- Headers, request payload and syntax-highlighted JSON response for each call
- **Mock this**: turn a captured request into a mock rule in one click
- Template library: empty list, 401 expired session, 404, 429 rate limit, 500, 503, slow network, offline and more
- GraphQL aware: see operation names and mock a single query on a shared `/graphql` endpoint
- Latency with random jitter, and simulated network failures
- Limit rules to specific sites, such as `localhost` or your staging server
- Import a HAR file to replay a recorded session as mocks
- Flip mocks on and off from the toolbar popup; the icon badge shows how many are active
- Replay a request, copy it as cURL, export the session as HAR, share rules as JSON
- Light and dark themes that follow DevTools

## How to use

1. Install the extension and open the page you are working on.
2. Press <kbd>F12</kbd> and open the **API Monitor Pro** tab, then use the page or reload it.
3. Click a request to see its headers, payload and response.
4. Press **Mock this** (or <kbd>M</kbd>), change the status or body, or pick a template, and click **Save Mock Rule**.
5. Reload the page: matching requests now get your mocked response. Turn rules off from the panel or the toolbar popup when you are done.

## Keyboard shortcuts

| Keys | Action |
| --- | --- |
| <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> | Pause / resume capture |
| <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>M</kbd> | Turn all mocks off (press again to restore) |
| <kbd>/</kbd> | Filter requests (in the DevTools panel) |
| <kbd>↑</kbd> <kbd>↓</kbd> | Move through requests |
| <kbd>M</kbd> | Mock the selected request |
| <kbd>Ctrl</kbd>+<kbd>Enter</kbd> | Save the mock rule |

## Permissions explained

- **Storage**: keeps your mock rules, settings and the last 150 captured calls on your computer.
- **Read and change data on all websites**: needed to see and mock the API calls of whatever site you are debugging. The extension only wraps `fetch` and `XMLHttpRequest` on the page; nothing is sent anywhere.

## FAQ

**Does it send my API data anywhere?**
No. Captured calls and rules stay in your browser's local storage. There is no account, server or analytics.

**Why don't I see some requests?**
Only `fetch` and `XMLHttpRequest` calls made by the page are captured. Images, scripts, WebSockets and requests made by service workers are not. If the list is empty, reload the page with DevTools open.

**I forgot a mock was on and my app looks broken. How do I tell?**
The toolbar icon shows the number of active mock rules, and mocked calls carry a purple MOCK tag in the panel. Press <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>M</kbd> to switch every mock off at once.

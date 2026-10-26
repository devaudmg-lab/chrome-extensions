// Compose a consistent 1280x800 marketing screenshot for the website / store.
//
//   const { showcase } = require('C:/dev/Projects/chrome-extensions/tools/showcase.js');
//   await showcase({
//     out: 'screenshots/zoomer/01-zoom.png',
//     title: 'Zoom toward your cursor',            // short headline
//     caption: 'Hold Alt and scroll to zoom in.',  // one sentence
//     page: 'raw/page.png',       // optional: full-page/browser-area capture (any size, will be fitted)
//     popup: 'raw/popup.png',     // optional: popup/side panel capture, floated on the right
//     accent: '#4f46e5',          // optional: brand colour of the extension
//   });
//
// Capture raw images with Playwright first (page.screenshot / popupPage.screenshot),
// then call showcase() to put them in the shared frame.
const path = require('path');
const fs = require('fs');
const { chromium } = require('C:/dev/Projects/Chrome Extensions/blur-remover/node_modules/playwright');

const toData = (p) => p && `data:image/png;base64,${fs.readFileSync(p).toString('base64')}`;
const esc = (s = '') => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

let browser;
async function getBrowser() {
  if (!browser) browser = await chromium.launch();
  return browser;
}

async function showcase({ out, title, caption = '', page, popup, accent = '#4f46e5' }) {
  const pageImg = toData(page);
  const popupImg = toData(popup);
  const onlyPopup = popupImg && !pageImg;
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>
  *{box-sizing:border-box;margin:0}
  body{width:1280px;height:800px;overflow:hidden;font-family:"Segoe UI",Inter,system-ui,sans-serif;
    background:radial-gradient(1200px 700px at 0% 0%, ${accent}33, transparent 60%),
               radial-gradient(900px 600px at 100% 100%, ${accent}26, transparent 60%), #f6f7fb;color:#0f172a}
  header{position:absolute;left:64px;top:44px;right:64px}
  h1{font-size:40px;font-weight:700;letter-spacing:-.02em}
  p{font-size:20px;color:#475569;margin-top:8px;max-width:1000px}
  .bar{position:absolute;left:64px;top:30px;width:56px;height:6px;border-radius:3px;background:${accent}}
  .win{position:absolute;left:64px;right:${popupImg ? 300 : 64}px;top:176px;bottom:0;border-radius:14px 14px 0 0;
    background:#fff;box-shadow:0 30px 80px -20px #0f172a55,0 0 0 1px #0f172a14;overflow:hidden}
  .chrome{height:36px;background:#eef0f4;display:flex;align-items:center;gap:8px;padding:0 14px}
  .chrome i{width:12px;height:12px;border-radius:50%;background:#d1d5db;display:block}
  .win img{display:block;width:100%;height:calc(100% - 36px);object-fit:cover;object-position:top left}
  .pop{position:absolute;right:${onlyPopup ? 'auto' : '56px'};${onlyPopup ? 'left:50%;transform:translateX(-50%);' : ''}top:${onlyPopup ? 170 : 150}px;
    max-height:${onlyPopup ? 600 : 620}px;max-width:${onlyPopup ? 900 : 420}px;border-radius:12px;background:#fff;
    box-shadow:0 40px 90px -20px #0f172a77,0 0 0 1px #0f172a1f;overflow:hidden}
  .pop img{display:block;max-height:inherit;max-width:inherit}
  </style></head><body>
  <div class="bar"></div>
  <header><h1>${esc(title)}</h1>${caption ? `<p>${esc(caption)}</p>` : ''}</header>
  ${pageImg ? `<div class="win"><div class="chrome"><i></i><i></i><i></i></div><img src="${pageImg}"></div>` : ''}
  ${popupImg ? `<div class="pop"><img src="${popupImg}"></div>` : ''}
  </body></html>`;
  const b = await getBrowser();
  const p = await b.newPage({ viewport: { width: 1280, height: 800 } });
  await p.setContent(html);
  fs.mkdirSync(path.dirname(out), { recursive: true });
  await p.screenshot({ path: out });
  await p.close();
}

async function closeShowcase() {
  if (browser) await browser.close();
  browser = undefined;
}

module.exports = { showcase, closeShowcase };

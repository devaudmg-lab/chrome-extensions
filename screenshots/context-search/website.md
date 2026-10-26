# ContextSearch

**Select any code or error and get an AI answer, follow-ups and the best developer sources without leaving the page.**

## What it does

ContextSearch works out what you selected (an error message, a CLI command, an npm package, an API name, a snippet of code) and where you are (GitHub, Stack Overflow, MDN, npm and more), then offers the most useful actions for it. AI answers stream right into the page and you can keep asking follow-up questions. For a deeper look, the side panel searches Stack Overflow, GitHub, npm and MDN at once and ranks the results.

## Key features

- **Context-aware palette**: press Ctrl+Shift+Space on selected text to get actions that fit it, like Explain, Debug, Generate Tests or Docs.
- **AI answers with follow-ups**: answers stream into the page, and you can ask up to 6 follow-up questions that keep the earlier conversation.
- **Your choice of AI**: Google Gemini, OpenAI, Anthropic Claude, or a free local model through Ollama. Without a key, Demo Mode shows sample answers.
- **Local Ollama made easy**: ContextSearch notices when Ollama is running and lists your installed models so you can pick one with a click.
- **Deep Research side panel**: Stack Overflow, GitHub, npm (with bundle sizes) and MDN in one ranked list, with an AI summary and pinned bookmarks.
- **Search history hints**: see your recent searches, get reminded when you researched something before, and spot results you already opened.
- **Custom actions you can share**: build your own search links and AI prompts, then export them as a small file for your team.
- **Private by design**: no telemetry and no ContextSearch server. Requests go straight from your browser to the AI provider and search sites you use.

## How to use

1. Install ContextSearch and pin it to your toolbar.
2. Open **Options > AI Models** and add an API key, or click **Use Ollama** if you run Ollama locally. (You can skip this and try Demo Mode first.)
3. Select some code, an error or a term on any page.
4. Press **Ctrl+Shift+Space** (Cmd+Shift+Space on Mac) or right-click the selection.
5. Pick an action. AI answers appear next to your selection: type a follow-up question at the bottom of the panel.
6. Choose **Research** to open the side panel with results from Stack Overflow, GitHub, npm and MDN.

## Keyboard shortcuts

| Keys | What it does |
| --- | --- |
| Ctrl+Shift+Space (Cmd+Shift+Space on Mac) | Open the palette for the selected text |
| 1 to 9, or arrow keys and Enter | Run an action from the palette |
| / | Jump to the follow-up box (in the AI panel) or the search box (in the side panel) |
| Esc | Close the palette, AI panel or side-panel drawers |

You can change the main shortcut, or add one for the side panel, at `chrome://extensions/shortcuts`.

## Permissions, explained simply

- **Read and change data on websites**: needed to see the text you select and show the palette on the page. Nothing is read until you select text, and password fields are ignored. The same access lets ContextSearch talk to the AI provider and search sites you use.
- **Local addresses (localhost)**: only used to talk to an AI model running on your own computer, such as Ollama.
- **Right-click menu**: adds ContextSearch actions to the menu when you right-click selected text.
- **Storage**: keeps your settings, custom actions, search history and bookmarks on your computer. API keys never sync to other devices.
- **Side panel**: shows the Deep Research panel.
- **Active tab and scripting**: lets the toolbar popup read the current page, and makes ContextSearch work in tabs that were already open when you installed it.

## FAQ

**Do I need an API key?**
No. Without a key, ContextSearch runs in Demo Mode with sample answers, and all search features work. For real AI answers, add a Gemini, OpenAI or Claude key, or use a free local model with Ollama.

**Is my code sent anywhere?**
Only when you choose an AI action, and only to the AI provider you set up (or to your own computer if you use Ollama). There is no ContextSearch server and no tracking.

**Can my team use the same custom actions?**
Yes. Go to **Options > Custom Actions** and click **Export Action Pack**. Your teammates click **Import Action Pack** and see the list before anything is added. Packs never include settings, history or API keys.

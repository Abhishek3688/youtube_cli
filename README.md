# 🎥 `ytcli` - Lightweight Terminal YouTube Browser & Player for Windows

> **A fast, native Windows alternative to `ytfzf` built with Python, `yt-dlp`, and `mpv.net`.**

`ytcli` lets you search, preview, and watch YouTube videos directly from your terminal with a floating Picture-in-Picture window — perfect for watching tutorials or lofi streams while coding in VS Code!

---

## ✨ Features

- 🔍 **Fast YouTube Search:** Search YouTube instantly without needing API keys (`yt-dlp` backend).
- 📌 **Always-on-Top Floating Player:** Opens a compact mini-window over your editor so you can code without distraction.
- 🖼️ **Terminal Thumbnail Previews:** Converts and previews video thumbnails right inside your terminal console (`climage`).
- 🎧 **Audio-Only Mode:** Stream music, podcasts, or ambient audio without a video window (`-a`).
- ⚡ **Resolution Control:** Cap video resolution to 360p, 480p, 720p, 1080p, etc. (`-q`).
- 🛡️ **IP Rate-Limit Safe:** Uses lightweight flat search extractions to keep your IP 100% safe.

---

## 🛠️ Prerequisites & Installation

### 1. Install `mpv.net` (Media Player for Windows)

In PowerShell, run:

```powershell
winget install --id mpv.net -e
```

Add `mpv.net` to your user PATH:
```powershell
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";$env:LOCALAPPDATA\Programs\mpv.net", "User")
```

### 2. Install Python Dependencies

```powershell
pip install yt-dlp climage pillow requests
```

---

## 🚀 Quick Start

Run a search query directly from your terminal:

```powershell
python main.py "python tutorial"
```

---

## 📋 Command Cheat Sheet & Usage Examples

| Flag | Full Option | Description | Example |
| :--- | :--- | :--- | :--- |
| *(default)* | `query` | Search query or direct YouTube link | `python main.py "cyberpunk 2077 trailer"` |
| **`-1`** | `--first` | Play the #1 search result immediately | `python main.py "lofi beats" -1` |
| **`-t`** | `--thumb` | Show high-resolution terminal thumbnail preview | `python main.py "python tutorial" -t` |
| **`-a`** | `--audio` | Play audio only (no video window) | `python main.py "lex fridman podcast" -a` |
| **`-q`** | `--quality` | Cap video resolution (e.g. `720`, `1080`) | `python main.py "4k space footage" -q 720` |
| **`-n`** | `--max-results` | Change number of search results (default: `10`) | `python main.py "music" -n 20` |

### 💡 Example Commands

```powershell
# 1. Search and pick from top 10 results
python main.py "machine learning tutorial"

# 2. Auto-play top result with thumbnail preview while coding
python main.py "lofi hip hop radio" -1 -t

# 3. Stream podcast in audio-only mode
python main.py "huberman lab podcast" -a

# 4. Watch 720p video from a direct link
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -q 720
```

---

## 💻 Optional: Add PowerShell Shortcut

To run `ytcli` from **any directory** in PowerShell, add this function to your PowerShell profile:

1. Open profile:
   ```powershell
   notepad $PROFILE
   ```
2. Add this line:
   ```powershell
   function ytcli { python "D:\practice\CLI\main.py" $args }
   ```
3. Restart PowerShell. Now you can run:
   ```powershell
   ytcli "python beginner guide" -1 -t
   ```

---

## 📄 License

MIT License. Built for seamless terminal productivity!

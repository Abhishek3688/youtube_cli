# 🎬 `youtube_cli` - Lightweight Terminal YouTube Browser & Player

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Player: mpv.net](https://img.shields.io/badge/Player-mpv.net%20%2F%20mpv-purple.svg)](https://github.com/mpvnet-player/mpv.net)
[![Backend: yt-dlp](https://img.shields.io/badge/Backend-yt--dlp-red.svg)](https://github.com/yt-dlp/yt-dlp)

> **A fast, native Windows & cross-platform terminal YouTube client built with Python, `yt-dlp`, and `mpv.net` / `mpv`.**

`youtube_cli` lets you search, preview, and stream YouTube videos directly from your terminal without opening a web browser. It features an always-on-top Picture-in-Picture floating mini-player so you can watch tutorials or listen to music while coding uninterrupted.

---

## ✨ Features

- 🔍 **Instant YouTube Search**: Search YouTube without requiring any Google API keys or credentials using `yt-dlp` flat extraction.
- 🪟 **Floating Picture-in-Picture Player**: Automatically positions an always-on-top mini window (`480x270`) in the corner of your screen over your code editor.
- 🖼️ **Terminal Thumbnail Previews**: Renders high-resolution video thumbnails directly in your terminal console using Unicode half-block characters (`climage` + Pillow).
- 📻 **Audio-Only Mode (`-a`)**: Stream podcasts, lo-fi beats, or music playlists with `--no-video` for minimal CPU and bandwidth usage.
- 📺 **Resolution Control (`-q`)**: Cap stream resolution (`360p`, `480p`, `720p`, `1080p`, `1440p`, `2160p`) to conserve network bandwidth.
- 👤 **Channel & Handle Support**: Search directly by YouTube handle (e.g. `@Fireship`) or channel URL to fetch recent uploads.
- 🔗 **Direct URL & Shorts Detection**: Paste any standard YouTube URL, `youtu.be` link, or YouTube Shorts link to stream immediately.
- 🔁 **Interactive Workflow**: Interactive result list with quick selection, instant re-search (`s`), and clean exit (`q`).
- ⚡ **Zero Video Download Overhead**: Streams audio/video directly through `mpv.net` / `mpv` without saving large video files to disk.

---

## 📁 Project Structure

```text
youtube_cli/
├── main.py          # CLI entry point, argument parsing, interactive menu loop
├── search.py        # Fast yt-dlp search engine & channel query resolver
├── player.py        # Player launcher (detects mpvnet/mpv, configures PiP & quality)
├── thumbnail.py     # Thumbnail downloader, 16:9 image scaler, and terminal renderer
├── .gitignore       # Git ignore rules (pycache, temporary thumbnail cache)
└── README.md        # Documentation and usage guide
```

---

## 🚀 Prerequisites & Installation

### 1. Install Media Player (`mpv.net` or `mpv`)

`youtube_cli` uses `mpv.net` (recommended on Windows) or standard `mpv`.

#### Windows (via winget):
```powershell
winget install --id mpv.net -e
```

Ensure `mpv.net` is in your system `PATH`:
```powershell
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";$env:LOCALAPPDATA\Programs\mpv.net", "User")
```

#### Linux / macOS:
```bash
# Ubuntu / Debian
sudo apt install mpv

# macOS (Homebrew)
brew install mpv
```

### 2. Clone the Repository & Install Dependencies

```powershell
# Clone the repository
git clone https://github.com/Abhishek3688/youtube_cli.git
cd youtube_cli

# Install Python packages
pip install yt-dlp climage pillow requests
```

---

## 💻 Usage & Command Reference

### Basic Syntax

```powershell
python main.py [QUERY / URL] [OPTIONS]
```

### CLI Flags & Arguments

| Flag | Long Option | Description | Default | Example |
| :--- | :--- | :--- | :--- | :--- |
| *(positional)* | `query` | Search keywords, `@channel` handle, or YouTube URL | `None` (prompts) | `python main.py "python tutorial"` |
| **`-t`** | `--thumb` | Render terminal thumbnail preview before playback | `False` | `python main.py "rust lang" -t` |
| **`-a`** | `--audio` | Audio-only playback (no video window) | `False` | `python main.py "lofi hip hop" -a` |
| **`-q`** | `--quality` | Cap maximum resolution (`360`, `480`, `720`, `1080`, `1440`, `2160`) | `None` (Best) | `python main.py "space 4k" -q 1080` |
| **`-n`** | `--max-results`| Maximum number of search results to fetch | `50` | `python main.py "music" -n 15` |
| | `--version` | Display version information | | `python main.py --version` |

---

## 🎮 Interactive Controls

When search results appear in your terminal:

```text
--- Results for 'python tutorial' ---
 [ 1] [  12:34] Python Tutorial for Beginners (Programming with Mosh)
 [ 2] [4:20:15] Python Full Course for Beginners [2024] (freeCodeCamp.org)
 ...

Select video [1-50], 's' to search again, 'q' to quit (default 1):
```

- **`1 - 50`** (or press `Enter` for `1`): Play selected video in the floating PiP window.
- **`s`** / **`search`** / **`r`**: Prompt for a new search query without restarting the program.
- **`q`** / **`quit`** / **`exit`**: Cleanly exit `youtube_cli`.

---

## 📖 Examples

### 1. Keyword Search with Interactive Selection
```powershell
python main.py "fastapi tutorial for beginners"
```

### 2. Channel Search by Handle
```powershell
python main.py "@Fireship"
python main.py "@freecodecamp" -n 10
```

### 3. Stream in Audio-Only Mode
```powershell
python main.py "lex fridman podcast" -a
```

### 4. Cap Video Quality to 720p with Thumbnail Preview
```powershell
python main.py "learn neovim in 100 seconds" -q 720 -t
```

### 5. Play Direct Video URL or YouTube Shorts Directly
```powershell
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -t
python main.py "https://youtu.be/dQw4w9WgXcQ" -a
```

### 6. Interactive Mode (No Arguments)
```powershell
python main.py
```

---

## ⚡ Optional: Set Up a Global Terminal Shortcut

To run `youtube_cli` from any directory in PowerShell:

1. Open your PowerShell profile:
   ```powershell
   notepad $PROFILE
   ```
2. Add a function pointing to your `main.py` path:
   ```powershell
   function youtube_cli { python "$HOME\youtube_cli\main.py" $args }
   ```
3. Save and reload your profile:
   ```powershell
   . $PROFILE
   ```
4. Now you can use `youtube_cli` anywhere:
   ```powershell
   youtube_cli "system design interview" -t -q 720
   ```

---

## 🛠️ Built With

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Fast metadata extraction and media streaming
- [mpv.net](https://github.com/mpvnet-player/mpv.net) / [mpv](https://mpv.io/) - High-performance, scriptable media player
- [climage](https://github.com/pnoy2008/climage) - Image-to-ANSI/Unicode terminal conversion
- [Pillow (PIL)](https://python-pillow.org/) - Aspect ratio normalization & image processing
- [Requests](https://requests.readthedocs.io/) - HTTP library for thumbnail asset fetching

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

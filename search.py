import yt_dlp

def format_duration(seconds):
    if not seconds:
        return "N/A"
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"

def search_youtube(query: str, max_results: int = 10) -> list[dict]: 
    ydl_opts = {
        "cachedir": False,
        "extract_flat": "in_playlist",
        "skip_download": True,
        "quiet": True,
    }

    search_query = f"ytsearch{max_results}:{query}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=False)

    videos = []
    if info and "entries" in info:
        for entry in info["entries"]:
            if not entry:
                continue
            v_id = entry.get("id")
            if not v_id:
                continue
            raw_dur = entry.get("duration")
            videos.append({
                "id": v_id,
                "title": entry.get("title", "Untitled"),
                "url": f"https://www.youtube.com/watch?v={v_id}",
                "thumbnail": entry.get("thumbnail") or f"https://img.youtube.com/vi/{v_id}/hqdefault.jpg",
                "channel": entry.get("uploader") or entry.get("channel") or "Unknown Channel",
                "duration_str": format_duration(raw_dur),
                "duration": raw_dur,
            })

    return videos


if __name__ == "__main__":
    query = input("Enter your search query: ")
    results = search_youtube(query, max_results=5)

    for i, video in enumerate(results, 1):
        print(f"{i}. [{video['duration_str']}] {video['title']} - {video['channel']}")
        print(f"   Link: {video['url']}\n")
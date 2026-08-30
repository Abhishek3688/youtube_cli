# CLI entry point & argument parser
import argparse
import sys
from search import search_youtube
from thumbnail import process_youtube_thumbnail
from player import play_video

def is_url(text: str) -> bool: 
    return text.startswith("https://www.") or text.startswith("http://") \
            or text.startswith("youtube.com") \
            or text.startswith("youtu.be")

def main(): 
    parser = argparse.ArgumentParser(
        prog="ytcli", 
        description="Search & play YouTube videos directly from your terminal.",
        epilog="Powered by yt-dlp & mpv.net"
    )

    parser.add_argument(
        "query", 
        help="Search query or YouTube URL to play",
        type=str, 
        nargs="?"
    )

    parser.add_argument(
        "-a", 
        "--audio", 
        action="store_true", 
        help="Play audio only (no video window)"
    )
    
    parser.add_argument(
        "-n", 
        "--max-results", 
        type=int,
        default=10,  
        help="Number of search results (default: 10)"
    )
    
    parser.add_argument(
        "-q", 
        "--quality", 
        type=int, 
        choices=[360, 480, 720, 1080, 1440, 2160], 
        help="Maximum video resolution (e.g., 720p)"
    )

    parser.add_argument(
        "-1", 
        "--first", 
        action="store_true", 
        help="Automatically play the first search result"
    )
    
    parser.add_argument(
        "-t",
        "--thumb",
        action="store_true",
        help="Show thumbnail preview in terminal before playing"
    )

    parser.add_argument(
        "--version", 
        action="version", 
        version="%(prog)s 1.0.0",
    )
    
    args = parser.parse_args()
    
    # Handle missing query 
    if not args.query: 
        args.query = input("Enter search query or URL: ").strip()
        if not args.query:
            print("Error: No query provided")
            sys.exit(1)

    # Direct URL Check
    if is_url(args.query):
        print(f"Direct URL provided. Playing: {args.query}")
        if args.thumb:
            try:
                process_youtube_thumbnail(args.query)
            except Exception as e:
                print(f"(Thumbnail unavailable: {e})")
        play_video(args.query, audio_only=args.audio, quality=args.quality, on_top=True)
        return

    # Search YouTube
    print(f"Searching YouTube for '{args.query}'...")
    results = search_youtube(args.query, max_results=args.max_results)

    if not results:
        print("No videos found.")
        return 
    
    # Select Video
    if args.first or len(results) == 1:
        selected = results[0]
    else:
        print(f"\n--- Search Results for '{args.query}' ---")
        for i, video in enumerate(results, 1):
            print(f" [{i}] [{video['duration_str']}] {video['title']} ({video['channel']})")

        try:
            choice = input(f"\nSelect video number [1-{len(results)}] (default 1): ").strip()
            idx = int(choice) - 1 if choice else 0
            if idx < 0 or idx >= len(results):
                idx = 0
        except ValueError:
            idx = 0
            
        selected = results[idx]

    print(f"\nSelected: {selected['title']}")
    print(f"Channel: {selected['channel']}")
    print(f"URL: {selected['url']}")

    # Render Thumbnail if requested
    if args.thumb:
        try:
            thumb_source = selected.get("thumbnail") or selected["url"]
            process_youtube_thumbnail(thumb_source)
        except Exception as e:
            print(f"(Thumbnail unavailable: {e})")

    # Play Stream
    play_video(selected["url"], audio_only=args.audio, quality=args.quality, on_top=True)

if __name__ == "__main__": 
    main()
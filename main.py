# CLI entry point & argument parser
import argparse
import sys
from search import search_youtube
from thumbnail import process_youtube_thumbnail
from player import play_video

def is_single_video_url(text: str) -> bool: 
    if "/@" in text or "/c/" in text or "/channel/" in text or "/user/" in text:
        return False
    return ("watch?v=" in text or "youtu.be/" in text or "shorts/" in text)

def main(): 
    parser = argparse.ArgumentParser(
        prog="youtube_cli", 
        description="Search & play YouTube videos directly from your terminal.",
        epilog="Powered by yt-dlp & mpv.net"
    )

    parser.add_argument(
        "query", 
        help="Search query, channel name/handle (@channel), or YouTube URL to play",
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
        default=50,  
        help="Number of search results (default: 50)"
    )
    
    parser.add_argument(
        "-q", 
        "--quality", 
        type=int, 
        choices=[360, 480, 720, 1080, 1440, 2160], 
        help="Maximum video resolution (e.g., 720p)"
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
    
    try:
        current_query = args.query

        while True:
            # Handle missing query 
            if not current_query: 
                current_query = input("\nEnter search query, channel (@handle), or URL (or 'q' to quit): ").strip()
                if not current_query or current_query.lower() in ['q', 'quit', 'exit']:
                    print("Exiting youtube_cli. Bye!")
                    sys.exit(0)

            # Direct Single Video URL Check
            if is_single_video_url(current_query):
                print(f"Direct video URL provided. Playing: {current_query}")
                if args.thumb:
                    try:
                        process_youtube_thumbnail(current_query)
                    except Exception as e:
                        print(f"(Thumbnail unavailable: {e})")
                play_video(current_query, audio_only=args.audio, quality=args.quality, on_top=True)
                return

            # Search YouTube (or Channel videos)
            print(f"Searching YouTube for '{current_query}'...")
            results = search_youtube(current_query, max_results=args.max_results)

            if not results:
                print("No videos found.")
                current_query = None
                continue
            
            # Display results list
            print(f"\n--- Results for '{current_query}' ---")
            for i, video in enumerate(results, 1):
                print(f" [{i:2d}] [{video['duration_str']:>7}] {video['title']} ({video['channel']})")

            while True:
                choice = input(f"\nSelect video [1-{len(results)}], 's' to search again, 'q' to quit (default 1): ").strip().lower()

                if choice in ['q', 'quit', 'exit']:
                    print("Exiting youtube_cli. Bye!")
                    sys.exit(0)
                elif choice in ['s', 'search', 'r', 'retry']:
                    current_query = input("Enter new search query: ").strip()
                    break  # Breaks inner loop to re-search
                else:
                    try:
                        idx = int(choice) - 1 if choice else 0
                        if idx < 0 or idx >= len(results):
                            idx = 0
                    except ValueError:
                        print("Invalid input. Type a video number, 's' to search again, or 'q' to quit.")
                        continue
                        
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
                    return

    except (KeyboardInterrupt, EOFError):
        print("\n\nExited youtube_cli. Goodbye!")
        sys.exit(0)

if __name__ == "__main__": 
    main()


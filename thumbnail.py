import os
import sys
import requests
import climage
from PIL import Image
from io import BytesIO

# ensure UTF-8 output in Windows Terminal 
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

def process_youtube_thumbnail(url_input, output_filename="yt_thumb.png", width=80):
    # 1. Determine source
    if url_input.startswith("http") and ("maxres" in url_input or ".jpg" in url_input or ".png" in url_input or ".webp" in url_input):
        img_url = url_input
    else:
        # extract video ID 
        if "youtu.be/" in url_input: 
            video_id = url_input.split("youtu.be/")[1].split("?")[0]
        elif "v=" in url_input: 
            video_id = url_input.split("v=")[1].split("&")[0]
        elif "shorts/" in url_input: 
            video_id = url_input.split("shorts/")[1].split("?")[0]
        else:
            raise ValueError("Invalid Youtube URL provided")

        # Max Resolution (maxresdefault) is ideal for clarity
        img_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

    print(f"Fetching thumbnail from: {img_url}")

    # 2. Download the asset stream safely into memory
    response = requests.get(img_url)
    if response.status_code != 200 and 'video_id' in locals():
        # Fallback to standard high-quality if maxres is missing
        img_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
        response = requests.get(img_url)

    if response.status_code != 200: 
        raise IOError(f"Failed to fetch thumbnail from {img_url}")

    # 3. Open image buffer with Pillow and standardise dimensions
    img = Image.open(BytesIO(response.content))
    
    # Force strict 16:9 aspect ratio canvas mapping
    target_width, target_height = 1280, 720
    img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    img.save(output_filename, format="PNG")
   
    # 4. Generate terminal preview using climage
    print("\n--- Terminal Visual Preview ---")
    try:
        # width=80 limits column character canvas width so it fits text consoles
        # is_unicode=True uses half-block characters for high-density rendering
        terminal_preview = climage.convert(output_filename, width=width, is_unicode=True)
        print(terminal_preview)
    except Exception as e:
        # Safe ASCII fallback for environments with system charmap limitations
        terminal_preview = climage.convert(output_filename, width=width, is_unicode=False)
        print(terminal_preview)

if __name__ == "__main__":
    # Example Execution:
    video_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    process_youtube_thumbnail(video_link)


import subprocess
import shutil

def get_player_executable() -> str:
    """Detects whether mpvnet or mpv is available on Windows PATH."""
    if shutil.which("mpvnet"):
        return "mpvnet"
    elif shutil.which("mpv"):
        return "mpv"
    return "mpvnet"  # Default fallback

def play_video(
    url: str, 
    audio_only: bool = False, 
    quality: int = None, 
    on_top: bool = True, 
    speed: float = 1.0, 
    volume: int = 100
):
    """
    Launches mpvnet to stream YouTube video.
    
    :param url: YouTube video URL or ID
    :param audio_only: If True, plays audio only without opening a video window
    :param quality: Maximum video resolution cap (e.g. 720, 1080)
    :param on_top: Pins video window on top of VS Code while coding
    :param speed: Playback speed multiplier (e.g. 1.25, 1.5)
    :param volume: Playback volume (0 to 100)
    """
    exe = get_player_executable()
    cmd = [exe, url]

    # Floating Picture-in-Picture window while coding
    if on_top and not audio_only:
        cmd.extend([
            "--ontop",                     # Always on top of VS Code window
            "--geometry=480x270-20-20",    # Small 480x270 window in bottom-right corner
            "--autofit=480x270",
            "--title=YouTube CLI Player"
        ])

    if audio_only:
        cmd.append("--no-video")

    if speed != 1.0:
        cmd.append(f"--speed={speed}")

    if volume != 100:
        cmd.append(f"--volume={volume}")

    if quality:
        cmd.append(f"--ytdl-format=bestvideo[height<={quality}]+bestaudio/best")

    print(f"▶ Launching player: {url}")
    subprocess.run(cmd)

if __name__ == "__main__":
    # Test playback
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    play_video(test_url, on_top=True)

import os
from moviepy.editor import VideoFileClip

def get_total_video_length(folder_path: str) -> tuple[float, int]:
    """
    Recursively scans a folder and all its subfolders, summing the duration of all video files.

    Supports formats: .mp4, .mov, .avi, .mkv, .flv, .wmv

    Args:
        folder_path (str): Path to the folder to scan.

    Returns:
        Total duration of all video files in seconds and total number of files scanned.
    """
    
    total_duration = 0
    total_files = 0
    video_extensions: tuple[str, ...] = (".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv")

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(video_extensions):
                total_files += 1
                video_path = os.path.join(root, file)
                try:
                    with VideoFileClip(video_path) as clip:
                        duration = clip.duration
                        print(f"Found '{file}' - duration: {duration:.2f} seconds")
                        total_duration += duration
                except Exception as e:
                    print(f"Could not process '{file}': {e}")

    return total_duration, total_files

def main():
    folder = r"C:\Users\YourName\Videos"  # UPDATE THIS PATH TO WHERE YOUR VIDEOS ARE
    total_seconds, total_files = get_total_video_length(folder)
    total_minutes = total_seconds / 60
    print(f"\nTotal files scanned: {total_files}")
    print(f"Total video runtime: {total_minutes:.2f} minutes ({total_seconds:.2f} seconds)")

if __name__ == "__main__":
    main()

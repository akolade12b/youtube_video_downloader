import os
import sys
import yt_dlp

def download_youtube_video(url, download_path):
    """Download a YouTube video using yt-dlp."""
    try:
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'format': 'best[ext=mp4]',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nDownload complete!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    
def main():
    try:
        # Get URL from command-line arguments
        if len(sys.argv) < 2:
            print("Usage: python youtube_downloader.py <YouTube URL>")
            return

        url = sys.argv[1]

        # Confirm download location
        download_path = input("\nEnter the download directory (leave blank for current directory): ")
        if not download_path:
            download_path = os.getcwd()

        # Check if directory exists
        if not os.path.exists(download_path):
            print("\nError: The specified directory does not exist.")
            return

        # Download the video
        download_youtube_video(url, download_path)

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()

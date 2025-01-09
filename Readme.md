# YouTube Video Downloader

This Python script allows you to download YouTube videos by providing a YouTube URL. It utilizes the `yt_dlp` library to fetch video information and download the selected stream. The script supports selecting the resolution and customizing the download directory.

## Features
- Displays video title and author.
- Lists available resolutions along with file sizes.
- Allows the user to select the desired resolution for download.
- Option to specify the download directory.
- Graceful handling of errors.

## Prerequisites
1. Python 3.6 or higher.
2. Install the `yt-dlp` library:
```bash
pip install yt-dlp
```

## Usage
1. Clone or download this repository.
```bash
git clone https://github.com/akolade12b/youtube-video-downloader.git
cd youtube-video-downloader
```

2. Run the script with the following command:
   ```bash
python youtube_downloader.py <YouTube URL>
   ```

### Example:
```bash
python youtube_downloader.py "https://youtu.be/exampleURL"
```

3. The script will:
   - Display the video title and available resolutions.
   - Prompt you to select a resolution by entering the corresponding number.
   - Ask for a download directory (leave blank to use the current directory).

4. The selected video will be downloaded to the specified directory.

## Error Handling
- If the video title or author cannot be fetched, the script will display placeholders.
- If the URL is invalid or inaccessible, an appropriate error message will be displayed.
- Ensures that the download directory exists before proceeding.

## Troubleshooting
If you encounter issues:
1. Ensure that the `yt-dlp` library is up to date:
   ```bash
pip install --upgrade yt-dlp
   ```
2. Check your internet connection and ensure the YouTube URL is valid.

## Contact
For support or inquiries, you can reach me via WhatsApp at: **09123663660**

## License
This project is licensed under the MIT License. Feel free to modify and use it as per your needs.


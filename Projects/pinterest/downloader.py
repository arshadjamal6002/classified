import yt_dlp

def download_pinterest_videos(file_path):
    with open(file_path, "r") as f:
        links = [line.strip() for line in f if line.strip()]

    if not links:
        print("No links found in the file.")
        return

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Save with video title as filename
        'format': 'bestvideo+bestaudio/best',  # Let yt-dlp decide the best format
        'merge_output_format': 'mp4',  # Convert to MP4 if needed
        'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}],
        'ignoreerrors': True,  # Continue even if some links fail
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)

if __name__ == "__main__":
    file_path = "links.txt"  # Change this to your actual file path
    download_pinterest_videos(file_path)

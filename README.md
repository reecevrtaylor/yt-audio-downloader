# YouTube Audio Downloader

## Introduction
YouTube Audio Downloader is a small personal application written for me to save the hundreds of music videos that play in the background while I work. It (obviously) allows you to download audio from YouTube videos and provides a simple GUI for easy interaction, enabling users to input the URL of a YouTube video and choose a destination folder for the downloaded audio file.

## Features
- Simple and intuitive GUI.
- Download audio from YouTube videos in high quality.
- Display download progress with speed and ETA.
- Customize the download location via a file dialog.

## Dependencies
This application requires `pytube` and `tqdm` libraries:

```bash
pip install pytube tqdm
```

## Usage
1. Run the script: `python youtube_audio_downloader.py`
2. Enter the YouTube URL in the provided text field.
3. Select the destination folder by clicking the 'Browse' button.
4. Click 'Download' to start the download process.
5. The application will display the download progress, including speed and ETA.
import math
import time
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from tqdm import tqdm
from threading import Thread


def on_progress(stream, bytes_remaining):
    current = ((stream.filesize - bytes_remaining) / stream.filesize)
    percent = current * 100
    speed = (stream.filesize - bytes_remaining) / (time.time() - start)
    eta = math.ceil(bytes_remaining / speed)
    eta_formatted = '{:02d}:{:02d}'.format(eta // 60, eta % 60)
    download_progress.set(
        f'Downloading: {percent:.1f}% - ETA: {eta_formatted} - Speed: {speed / (1024 * 1024):.2f} Mbps')


def format_title(title):
    return title.replace(" ", "_").lower()


def download_audio():
    global start
    url = url_entry.get()
    save_path = save_path_entry.get()

    if not url or not save_path:
        download_progress.set(
            "Please enter a YouTube URL and select a save path.")
        return

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        video_title.set("Video Title: " + yt.title)
        audio_stream = yt.streams.filter(only_audio=True).first()
        start = time.time()
        file_name = format_title(yt.title)
        audio_stream.download(save_path, filename=file_name + ".mp3")
        download_progress.set('Download completed!')
    except Exception as e:
        download_progress.set(f"Error: {e}")


def browse_folder():
    folder_selected = filedialog.askdirectory()
    save_path_entry.set(folder_selected)


def start_download():
    Thread(target=download_audio).start()


# Set up the GUI
root = tk.Tk()
root.title("YouTube Audio Downloader")

# URL Entry
tk.Label(root, text="Enter YouTube URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Save Path Entry
tk.Label(root, text="Select Download Folder:").pack()
save_path_entry = tk.StringVar()
tk.Entry(root, textvariable=save_path_entry, width=50).pack()
tk.Button(root, text="Browse", command=browse_folder).pack()

# Download Button
tk.Button(root, text="Download", command=start_download).pack()

# Progress and Info
video_title = tk.StringVar()
tk.Label(root, textvariable=video_title).pack()
download_progress = tk.StringVar()
tk.Label(root, textvariable=download_progress).pack()

# Run the GUI
root.mainloop()

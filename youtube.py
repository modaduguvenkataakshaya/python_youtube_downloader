import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

# Function to download the video
def download_video():
    url = url_entry.get()
    folder = folder_path.get()
    
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    
    if not folder:
        messagebox.showerror("Error", "Please select a download folder")
        return
    
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(folder)
        messagebox.showinfo("Success", f"Video downloaded successfully to:\n{folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Function to browse and select download folder
def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

# Create the main application window
app = tk.Tk()
app.title("YouTube Video Downloader")
app.geometry("500x200")
app.resizable(False, False)

# YouTube URL entry
tk.Label(app, text="YouTube URL:", font=("Arial", 12)).pack(pady=5)
url_entry = tk.Entry(app, width=50, font=("Arial", 12))
url_entry.pack(pady=5)

# Download folder selection
tk.Label(app, text="Download Folder:", font=("Arial", 12)).pack(pady=5)
folder_path = tk.StringVar()
folder_entry = tk.Entry(app, textvariable=folder_path, width=40, font=("Arial", 12), state="readonly")
folder_entry.pack(side="left", padx=10, pady=5)
browse_button = tk.Button(app, text="Browse", font=("Arial", 12), command=browse_folder)
browse_button.pack(pady=5)

# Download button
download_button = tk.Button(app, text="Download", font=("Arial", 14, "bold"), command=download_video)
download_button.pack(pady=20)

# Run the application
app.mainloop()

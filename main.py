import tkinter as tk
from tkinter import *
from pytube import YouTube
import customtkinter


def download(op):
    try:
        ytlink = link.get()
        ytobj = YouTube(ytlink, on_progress_callback=on_progress)
        if op == "Audio":
            video = ytobj.streams.get_audio_only()
        else:
            video = ytobj.streams.get_by_resolution(op)

        title.configure(text=ytobj.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!", text_color="green")

    except:
        finishLabel.configure(text="Error in Downloading!", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    per = str(int(percentage))
    progress.configure(text=per + '%')
    progress.update()

    progressbar.set(float(percentage) / 100)


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app_logo = 'C:\\Users\\91770\\Documents\\.Studies\\python\\pythonProject\\logo.png'

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YT-Downloder")

app.iconbitmap(app_logo)

title = customtkinter.CTkLabel(app, text="Insert a YouTube Link", width=200, height=50, font=("arial", 25))
title.pack(padx=10, pady=10)

url = tk.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=50, textvariable=url)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progressbar = customtkinter.CTkProgressBar(app, width=200)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

option = ['144p','240p','360p','480p','720p','1080p']
res = StringVar()
res.set('144p')
drop = customtkinter.CTkOptionMenu(master=app, values=option)
drop.pack()

button = customtkinter.CTkButton(app,text="Download", command=lambda: download(res)).pack()

download_audio = customtkinter.CTkButton(app, text="Audio-MP3", command=lambda: download("Audio"))
download_audio.pack(padx=20, pady=50)

app.mainloop()

import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink = link.get()  
        ytObject = YouTube(ytlink) 
        video = ytObject.streams.get_highest_resolution()  
        video.download()
    except:
        print("Youtube link is invalid")
    print("Download Complete!")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=460, height=40, textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

app.mainloop()

#sample link: https://youtu.be/tCDvOQI3pco?si=p7hY6pRbQsrW3Unb


from tkinter import*
from tkinter import filedialog
import moviepy.editor as movie

def convert():
    clip = movie.VideoFileClip(fname)
    
    clip.audio.write_audiofile("audio.mp3")
    msgForGenerate.set("Audio file generated successfully")

def UploadAction():
    
    filename = filedialog.askopenfilename(filetypes =[('Mp4 Files', '*.mp4'),('WMV Files', '*.wmv'),('AVI Files','*.avi'),('MKV Files','*.mkv')])
    
    msgForUpload.set("Uploaded:"+filename)
    
    global fname
    
    fname=filename

root =Tk()

root.geometry("600x200")

root["bg"]="#0B6E69"

root.title("Video to Audio Converter") 

global msgForUpload
global msgForGenerate
msgForUpload=StringVar()
msgForGenerate=StringVar()

Label(root,text="Hello",textvariable=msgForUpload,font="Arial 12",bg="#0B6E69",fg="white").place(x=80,y=30)

Button(root, text='Upload Video', command=UploadAction,font="Arial 12 bold",width="12",bg="#AB1C0D",fg="white").place(x=80,y=70)

Button(root,text="Convert",font="Arial 12 bold",width="10",command=convert,bg="#AB1C0D",fg="white").place(x=350,y=70)

Label(root,text="Hello",textvariable=msgForGenerate,font="Arial 12",bg="#0B6E69",fg="white").place(x=80,y=120)
root.mainloop()
import tkinter 
import tkinter.filedialog
from pytube import YouTube
from urllib.request import urlopen 
from PIL import Image, ImageTk
from io import BytesIO

w = tkinter.Tk()
radio = tkinter.IntVar()
w.title("Youtube Downloader")
w.geometry("900x300")


def download():
 url = urltextbox.get("1.0","end-1c") 
 try:
  yt = YouTube(url)
 except VideoUnavailable:
  print("Video unavailable")
 else:
  s = yt.streams.get_by_itag(resolution)
  s.download(path)
  l4 = tkinter.Label(w,text="Downloaded\t"+yt.title,height = 2,width =100)
  l4.grid(row=5,column=0,columnspan=3)

def browse():
 global path
 path = tkinter.filedialog.askdirectory()
 l3 = tkinter.Label(w,text=path,height = 2,width = 80)
 l3.grid(row=1,column=1)
 


def res():
 global resolution
 resolution = str(radio.get()) 
   
l1 = tkinter.Label(w,text="Video URL")
l1.grid(row=0,column=0)    

urltextbox = tkinter.Text(w,height = 2, width = 50)
urltextbox.grid(row=0,column=1)

l2 = tkinter.Label(w,text="Path")
l2.grid(row=1,column=0)

browse_button = tkinter.Button(w,text="Browse",command=browse,font=("Arial Italic",20), bg="blue",fg ="white")
browse_button.grid(row=1,column=2)

l3 = tkinter.Label(w,text="Resolution")
l3.grid(row=2,column=0)

radio_button1 = tkinter.Radiobutton(w,text = "360p",variable= radio,value=18, command = res )
radio_button1.grid(row=2,column=1)
radio_button2 = tkinter.Radiobutton(w,text = "720p",variable= radio,value=22, command = res )
radio_button2.grid(row=3,column=1)
radio_button3 = tkinter.Radiobutton(w,text = "Audio",variable= radio,value=251, command = res )
radio_button3.grid(row=4,column=1)

download_button = tkinter.Button(w,text="Download",command=download, font=("Arial Italic",20), bg="red",fg ="white")
download_button.grid(row=3,column=2)





def thumbnail():
 url = urltextbox.get("1.0","end-1c")
 yt = YouTube(url)
 rawtn= urlopen("http://tinypic.com/images/goodbye.jpg").read()
 img = Image.open(BytesIO(rawtn)).resize((2,2))
 tkimg = ImageTk.PhotoImage(img)
 l5 = tkinter.Label(w, image = tkimg)
 l5.grid(row=4,column=0)

w.mainloop()

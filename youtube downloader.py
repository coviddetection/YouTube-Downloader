import pytube
import os

from tkinter import *
from tk import *
from tkinter import Frame
from tkinter import ttk

from PIL import ImageTk,Image


class Application(Frame):


     def createWidgets(self):
         self.QUIT = Button(self)
         self.QUIT["text"] = "QUIT"
         self.QUIT["fg"]   = "red"
         self.QUIT["command"] =  self.quit

         self.QUIT.pack({"side": "left"})

         self.hi_there1 = Button(self)
         self.hi_there1["text"] = "Find Person " 
         self.hi_there1["command"] = self.q
  
         
         self.hi_there1.pack({"side": "left"})

  
         
        

         self.entry2 = Entry (root)

         canvas2 =Canvas(root, width = 400, height = 300)
         canvas2.create_window(200, 140, window=self.entry2)
         self.entry2.pack({"side":"right"})

         

         self.entry3 = Entry (root)

         canvas3 =Canvas(root, width = 400, height = 300)
         canvas3.create_window(200, 140, window=self.entry3)
         self.entry3.pack({"side":"right"})

    


     def __init__(self, master=None):
            Frame.__init__(self, master)
            self.pack()
            self.createWidgets()





 

     def q(self):
         b=self.entry3.get()
         a=self.entry2.get()
         video=pytube.YouTube(a)
         stream=video.streams.ge_by_itag(22)
         print("Downloading...")
         stram.download(filename=b)

         

root = Tk()
root.title("YouTube Downloader")
app = Application(master=root)       
app.mainloop()
root.destroy()

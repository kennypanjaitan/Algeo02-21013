import tkinter as tk
from tkinter import filedialog, Text, PhotoImage, Label
from PIL import Image, ImageTk
import tkinter.filedialog
from tkinter import *
import sys
import time
global count

root = tk.Tk()
root.title('Algeo02 - KennyBisa')
root.geometry('1000x600')

background = tk.PhotoImage(file="Desktop - 1.png")

my_label = tk.Label(root, image= background)
my_label.place(x=0, y=0,relwidth=1, relheight=1)

def addImage():
    filename = tk.filedialog.askopenfilename(initialdir="/", title="Select File",
                filetypes=(("dataset", "*.jpg"), ("Jpg Files", "*.jpg")))
    if filename:
        img = Image.open(filename)
        img = img.resize((256,256), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        e1 = tk.Label(root, image=img)
        e1.image = img
        e1.place(x=400, y=212)

def addApps():
    filename = tk.filedialog.askdirectory(initialdir="/", title="Select Folder")


openDataset = tk.Button(root, text='Choose Folder', fg="#457373", bg='#E5E5E5', bd=0, command=addApps, font="Dongle")
openDataset.place(x=41, y= 220, relx=0.01, rely=0.01)

openFile = tk.Button(root, text='Choose File', fg='#457373', bd=0, bg='#E5E5E5', command=addImage, font="Dongle")
openFile.place(x=50, y= 326, relx=0.01, rely=0.01)

def result(pathresult):
    imgresult = tk.PhotoImage(file= pathresult)

# class stopwatch():
#     def reset(self):
#         global count
#         count = 1
#         self.t.set('00:00:00')
#     def start(self):
#         global count
#         count = 0
#         self.timer()
#     def stop(self):
#         global count
#         count = 1
#     def timer(self):
#         global count
#         if count == 0:
#             self.d = str(self.t.get())
#             h, m, s = map(int, self.d.split(":"))
#             h = int(h)
#             m = int(m)
#             s = int(s)
#             if (s < 59):
#                 s += 1
#             elif (s == 59):
#                 s = 0
#                 if (m < 59):
#                     m += 1
#                 elif (m == 59):
#                     m = 0
#                     h += 1
#             if (h < 10):
#                 h = str(0) + str(h)
#             else:
#                 h = str(h)
#             if (m < 10):
#                 m = str(0) + str(m)
#             else:
#                 m = str(m)
#             if (s < 10):
#                 s = str(0) + str(s)
#             else:
#                 s = str(s)
#             self.d = h + ":" + m + ":" + s
#             self.t.set(self.d)
#             if (count == 0):
#                 self.root.after(1000, self.timer) 

root.mainloop()
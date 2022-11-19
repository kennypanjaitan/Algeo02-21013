import tkinter as tk
from tkinter import filedialog, Text, PhotoImage, Label
from PIL import Image, ImageTk
import tkinter.filedialog

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
        img = img.resize((250,250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        e1 = tk.Label(root, image=img)
        e1.image = img
        e1.place(x=400, y=212)

def addApps():
    filename = filedialog.askdirectory(initialdir="/", title="Select Folder",
                filetypes=("All Folders", "*.*"))

button = Image.open('button.png')
activebutton = Image.open('Clicked.png')

openDataset = tk.Button(root, text='Choose Folder', fg="#457373", bg='#E5E5E5', bd=0, command=addApps, font="Dongle")
openDataset.place(x=41, y= 220, relx=0.01, rely=0.01)

openFile = tk.Button(root, text='Choose File', fg='#457373', bd=0, bg='#E5E5E5', command=addImage, font="Dongle")
openFile.place(x=50, y= 326, relx=0.01, rely=0.01)

root.mainloop()
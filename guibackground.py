import tkinter as tk
from tkinter import filedialog, Text, PhotoImage, Label
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Algeo02 - KennyBisa')
root.geometry('1000x600')

background = tk.PhotoImage(file="Desktop - 1.png")
# apps = []
def addImage():
    # for widget in frame.winfo_children():
    #     widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                filetypes=(("dataset", "*.jpg"), ("All Files", "*.*")))
    # apps.append(filename)
    # print(filename)
    # for app in apps:
    #     label = tk.Label(frame, text=app, bg="gray")

def addApps():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                filetypes=(("dataset", "*.*"), ("All Folders", "*.*")))


my_label = tk.Label(root, image= background)
my_label.place(x=0, y=0,relwidth=1, relheight=1)

button = Image.open('Frame.png')
activebutton = Image.open('Clicked.png')

root.button = ImageTk.PhotoImage(button)
root.activebutton = ImageTk.PhotoImage(activebutton)

def on_enter(event):
    openDataset.config(image=root.button)
    openFile.config(image=root.button)

def on_leave(enter):
    openDataset.config(image=root.activebutton)
    openFile.config(image=root.activebutton)

openDataset = tk.Button(root, image=button, bd=0, command=addApps, font="Dongle")
openDataset.place(x=34, y= 215, relx=0.01, rely=0.01)

openFile = tk.Button(root, image=button, bd=0, command=addImage, font="Dongle")
openFile.place(x=34, y= 319, relx=0.01, rely=0.01)

openDataset.bind("<Enter>", on_enter)
openDataset.bind("<Leave>", on_leave)

openFile.bind("<Enter>", on_enter)
openFile.bind("<Leave>", on_leave)

root.mainloop()
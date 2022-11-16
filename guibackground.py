import tkinter as tk
from tkinter import filedialog, Text

root = tk.Tk()
root.title('Algeo02 - KennyBisa')
root.geometry('1000x600')

background = tk.PhotoImage(file="Desktop - 1.png")
# apps = []
def addApp():
    # for widget in frame.winfo_children():
    #     widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                filetypes=(("dataset", "*.jpg"), ("all files", "*.*")))
    # apps.append(filename)
    # print(filename)
    # for app in apps:
    #     label = tk.Label(frame, text=app, bg="gray")

# def runApps():


my_label = tk.Label(root, image= background)
my_label.place(x=0, y=0,relwidth=1, relheight=1)

openDataset = tk.Button(root, text="Choose File", fg="#2f4d4d",bg="#D8D8D6", command=addApp, font="Dongle")
openDataset.place(x=50, y= 220, relx=0.01, rely=0.01)

openFile = tk.Button(root, text="Choose File", fg="#2f4d4d", bg="#D8D8D6", command=addApp, font="Dongle")
openFile.place(x=50, y= 323, relx=0.01, rely=0.01)

root.mainloop()
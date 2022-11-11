# nyoba
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# INIT
main = tk.Tk()
main.configure(background = "navy")
main.geometry("500 x 400")
main.resizable(False, False)
main.title("Face Recognition")

# variabel
NAMA = tk.StringVar()

# fungsi
def klik():
    print("Hello, " + NAMA.get())
    pesan = f"Semangat {NAMA.get()}!"
    showinfo(title = "Your Name", message = pesan)

# GUI
desc = ttk.Label(main, text = "Welcome to Our APP!")

# Frame buat input
input_frame = ttk.Frame(main)
input_frame.pack(padx = 20, pady = 10, fill = "x", expand = True)

# Pesan di atas input
input_desc = ttk.Label(input_frame, text = "Masukkan nama kalian!")
input_desc.pack(padx = 10, pady = 10, fill = "x", expand = True)

# Box input nama
input_nama = ttk.Entry(input_frame, textvariable = NAMA)
input_nama.pack(padx = 10, pady = 10, fill = "x", expand = True)

# Tombol
sapa = ttk.Button(input_frame, text = "Hello!", command = klik)
sapa.pack(padx = 10, pady = 10, fill = "x")

main.mainloop()

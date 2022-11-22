import os
import cv2
import numpy as np
from qrDecomposition import *
from euclideanDistance import *
import tkinter as tk
from tkinter import filedialog, Text, PhotoImage, Label
import tkinter.filedialog
from tkinter import *
from PIL import ImageTk
import PIL.Image
import sys
import time
# from webcam import *
# from training import savedataset

root = tk.Tk()
root.title('Algeo02 - KennyBisa')
root.geometry('1000x600')
root.resizable(False, False)

# background utama gui
background = tk.PhotoImage(file="Desktop - 1.png")

my_label = tk.Label(root, image= background)
my_label.place(x=0, y=0,relwidth=1, relheight=1)

file_path_var = StringVar()
folder_path_var = StringVar()
closest_path_var = StringVar()


# choose file jpg
def addImage():
    filepath = tk.filedialog.askopenfilename(initialdir="/",title="Select File",
                filetypes=(("dataset", "*.jpg"), ("Jpg Files", "*.jpg")))
    if filepath:
        img = PIL.Image.open(filepath)
        img = img.resize((256,256))
        img = ImageTk.PhotoImage(img)
        e1 = tk.Label(root, image=img)
        e1.image = img
        e1.place(x=390, y=212)
    file_path_var.set(filepath)
    file_path_var.get()

# choose folder
def addApps():
    folderpath = tk.filedialog.askdirectory(initialdir="/", title="Select Folder")
    folder_path_var.set(folderpath)
    folder_path_var.get()


# cambutton = ImageTk.PhotoImage(PIL.Image.open('button_camera.png').resize((58, 58)))

# closest = ImageTk.PhotoImage(PIL.Image.open(closest_path_var.get()))
# closest.place(x= 900, y= 80)

# button nyalain kamera
# webcam = tk.Button(root, image=cambutton, bd=0, bg='#E3CD99',  command=savedataset, font=("Dongle", 12))
# webcam.place(x=858, y= 60, relx=0.01, rely=0.01)

# button choose folder
openDataset = tk.Button(root, text='Choose Folder', fg="#4B4D4E", bg='#E5E5E5', bd=0, command=addApps, font=("Dongle", 12), cursor='spider')
openDataset.place(x=64, y= 221, relx=0.01, rely=0.01)

# button choose file
openFile = tk.Button(root, text='Choose File', fg='#4B4D4E', bd=0, bg='#E5E5E5', command=addImage, font=("Dongle", 12), cursor='spider')
openFile.place(x=72, y= 326, relx=0.01, rely=0.01)

# if webcam:
#     foldername = 'C:/Users/eunic/Documents/Algeo02-21013/datasetcam/foto0.jpg'
# elif openFile:
#     foldername = file_path_var.get()



# execution time
# m = 0
# s = 0
# ms = 0

# stop = 0
# def start():
#     global m, s, ms, stopwatch
#     time.sleep(0.00001)
#     ms += 1
#     if ms == 10:
#         ms = 0
#         s += 1
#     if s == 60:
#         s = 0
#         m += 1
#     if m == 60:
#         m = 0
#         h += 1

#     # condition digital time
#     if s < 10:
#         if m < 10:
#             stopwatch = f"0{m}:0{s}:{ms}"
#         else:
#             stopwatch = f"{m}:0{s}:{ms}"
#     else:
#         if m < 10:
#             stopwatch = f"0{m}:{s}:{ms}"
#         else:
#             stopwatch = f"{m}:{s}:{ms}"
    
#     # print
#     if stop == 0:
def eunice():
    width = 256
    height = 256

    # menyimpan nama training image dalam sebuah array
    folder = folder_path_var.get()
    img_names = []
    for filename in os.listdir(folder):
        img_names.append(filename)


    # membaca training image dan menyimpan dalam array
    training_img   = np.ndarray(shape=(len(img_names), height*width))
    for i in range(len(img_names)):
        img = cv2.imread(os.path.join(folder,img_names[i]),0)
        img = cv2.resize(img,(height,width))
        training_img[i] = img.reshape(1,height*width)


    #  menghitung mean
    matMean = np.zeros((1,height*width))
    for i in range (len(img_names)):
        matMean = np.add(matMean,(1/(len(img_names)))*training_img[i])
    # print(matMean)
    # haha = np.reshape(matMean.astype(np.uint8),(height,width))
    # cv2.imshow('image',haha)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # menghitung selisih  / normalize vector
    normalize_training_img = np.ndarray(shape=(len(img_names), height*width))
    for i in range(len(img_names)):
        normalize_training_img[i] = np.subtract(training_img[i],matMean)
        # haha = np.reshape(normalize_training_img[i].astype(np.uint8),(height,width))
        # cv2.imshow('image',haha)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


    #  membuat matriks A untuk menghitung Covarian
    A = np.zeros((len(img_names),height*width))
    for i in range (len(img_names)):
        A[i,:] = normalize_training_img[i]
        # haha = np.reshape(A[i,:].astype(np.uint8),(height,width))
        # cv2.imshow('image',haha)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


    # menghitung Covarian
    matCovarian = A @ (np.transpose(A))


    # mencari eigen value dan eigen vector
    val, vec = qr_to_eig(matCovarian)


    # mencari eigen face
    normalize_vector = np.zeros((len(img_names),height*width))
    for i in range(len(img_names)):
        normalize_vector[i] = np.transpose(vec)[:,len(vec)-1-i] @ A
        # haha = np.reshape(eigenFace[i+1].astype(np.uint8),(height,width))
        # cv2.imshow('image',haha)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    eigenFace = normalize_vector.copy()
    for i in range(len(img_names)):
        eigenFace[i] = normalize_vector[len(img_names)-1-i] / euclidean_distance((vec[(len(img_names)-1)-i]),2)
        # haha = np.reshape(eigenFace[i].astype(np.uint8),(height,width))
        # cv2.imshow('image',haha)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


    # memilih eigen vector yang memiliki eigen value >= 1
    eigenfaces_used = 0
    for i in range (len(val)):
        if (val[i] > 1):
            eigenfaces_used  += 1
    # print(count) = 104
    # print(len(val)) = 105

 


    # mencari weight
    w = np.zeros((len(eigenFace),eigenfaces_used))
    for i in range (len(eigenFace)):
        for j in range (eigenfaces_used):
            w[i,j] = eigenFace[j] @ normalize_training_img[i]
        

    '''_____________________________________________________________________________'''
    # if openFile:
    #     foldername = file_path_var.get()
    # if webcam:
    #     foldername = 'C:/Users/eunic/Documents/Algeo02-21013/datasetcam/foto0.jpg'
    # membaca test image
    foldername = file_path_var.get()
    print(foldername)
    img = cv2.imread(os.path.join(foldername),0)
    img = cv2.resize(img,(width,height))
    test_img = img.reshape(1,height*width)


    # menghitung selisih  / normalize vector
    normalize_test_img = np.subtract(test_img,matMean)
    # haha = np.reshape(normalize_uface_vector.astype(np.uint8),(height,width))
    # cv2.imshow('image',haha)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # print(haha)


    # mencari weight
    w_test = np.zeros((1,eigenfaces_used))
    for i in range (eigenfaces_used):
        w_test[0,i] = eigenFace[i] @ normalize_test_img[0]


    # mencari euclidean distance minimum
    dist = np.zeros((1,len(img_names)))
    for i in range(len(img_names)):
        dist[0,i] = euclidean_distance(w_test[0,:],w[i,:])
        if (i == 0) :
            min = dist[0,i]
            ayey = i
        else:
            if (min > dist[0,i]):
                min = dist[0,i]
                ayey = i
    print(min)
    # global stop
    # mencari nama dengan distance minimum dan menampilkan training imagenya
    for i in range(len(img_names)):
        if (i == ayey):
            print(img_names[i])
            haha = np.reshape(training_img[i].astype(np.uint8),(height,width))
            # cv2.imshow('image',haha)
            closest_path_var = os.path.join(folder, img_names[i])
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # closest = os.path.join(haha)
            print(closest_path_var)
            # ----------------nyoba buat buka
            img2 = PIL.Image.open(closest_path_var)
            img2 = img2.resize((256,256))
            img2 = ImageTk.PhotoImage(img2)
            e2 = tk.Label(root, image=img2)
            e2.image = img2
            e2.place(x=675, y=212)
            duration = (time.time() - start) * 0.001
            label = Label(root, text= duration, font=("Dongle", 12), bg='#E1C787', fg='#4B4D4E')
            label.after(300, duration)
            label.place(x =525, y= 495)

start  = time.time()     

startbutton = tk.Button(root, command= lambda: [start, eunice()], text="Start", font=("Dongle", 12), bd= 0, fg='#4B4D4E', bg='#E5E5E5', cursor='spider').place(x= 435, y= 520)
root.mainloop()
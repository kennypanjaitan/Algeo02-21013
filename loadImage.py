import cv2
import os

def load_images_from_folder(folder):
    count = 0
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            count += 1
            cv2.imshow('image',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    print(count)

def load_folder_from_folder(foldername):
    for folder in os.listdir(foldername):
        name = foldername+"/"+folder
        load_images_from_folder(name)

foldername = 'dataset'
load_folder_from_folder(foldername)
import cv2
import os
import numpy as np

def load_images_from_folder(folder):
    count = 0
    rows, cols = (256,256)
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img.resize(256,256)
        if img is not None:
            count += 1
            matrix = np.add(matrix,img)
            # cv2.imshow('image',img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
    print(count)
    matrixMean = matrix * (1/count)
    print(matrixMean)

def load_folder_from_folder(foldername):
    for folder in os.listdir(foldername):
        name = foldername+"/"+folder
        load_images_from_folder(name)

foldername = 'dataset'
load_folder_from_folder(foldername)
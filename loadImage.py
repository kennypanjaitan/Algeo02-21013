import cv2
import os
import numpy as np
# from eigen import *
from qrDecomposition import *

def covarian(matrixMean,folder): # cari matrix covarian
    count = 0
    for filename in os.listdir(folder):
        mat = cv2.imread(os.path.join(folder,filename),0)
        mat = cv2.resize(mat,(256,256))
        count += 1
        mat = mat - matrixMean
        mat = np.abs(mat)
        if (count == 1):
            matNew = mat
        else:
            matNew = np.concatenate((matNew, mat), axis=1)
    matNewTranspose = np.transpose(matNew)
    matCovarian = np.matmul(matNew,matNewTranspose)
    return matCovarian

def mean(folder): # cari matrix mean
    count = 0
    rows, cols = (256,256)
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),0)
        img = cv2.resize(img,(256,256))
        count += 1
        matrix = np.add(matrix,img)
        # cv2.imshow('image',img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    # print(matrix)
    matrixMean = matrix * (1/count)
    matrixMean = matrixMean.astype(int)
    # print(matrixMean)
    return matrixMean

# main
foldername = 'dataset/105_classes_pins_dataset' # nama folder datasetnya
count = 0
for folder in os.listdir(foldername):
    name = foldername+"/"+folder
    matrixMean = mean(name)
    matrixCovarian = covarian(matrixMean,name)
    print(folder)
    print(matrixCovarian)
    # print(eigenval(matrixCovarian))
    val, vec = find_eig_qr(matrixCovarian)
    print(val)
    print(vec)
    count += 1
    if (count == 2):
        break

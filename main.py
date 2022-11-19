import cv2
import os
import numpy as np
from qrDecomposition import *
from numpy import linalg as LA

def mean(folder): # cari matrix mean
    count = 0
    matrix = [[0 for i in range(256)] for j in range(256)]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),0)
        img = cv2.resize(img,(256,256))
        img = img[50:206, 50:206]
        img = cv2.resize(img,(256,256))
        # print(img)
        # cv2.imshow('imageSelisih',img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        count += 1
        matrix = np.add(matrix,img)
    matrixMean = matrix * (1/count)
    matrixMean = matrixMean.astype(np.uint8)
    return matrixMean

def selisih(mean):
    count = 0
    matrix = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),0)
        img = cv2.resize(img,(256,256))
        img = img[50:206, 50:206]
        img = cv2.resize(img,(256,256))
        count += 1
        selisih = np.subtract(img,mean)
        # selisih = selisih.astype(np.uint8)
        # print(selisih)
        # cv2.imshow('imageSelisih',selisih)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        matrix.append(selisih)
        if (count == 1):
            matNew = selisih
        else:
            matNew = np.concatenate((matNew, selisih), axis=1)
    matrix = np.array(matrix)
    matCovarian = np.cov(matNew)
    # matCovarian = matNew @ np.transpose(matNew)
    # matCovarian = matCovarian.astype(np.uint8)
    # print(matCovarian)
    # cv2.imshow('imageCov',matCovarian)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return matCovarian, matrix
    # return matrix


folder = 'dataset' # nama folder datasetnya
matrixMean = mean(folder)
# print(matrixMean)
# cv2.imshow('imageMean',matrixMean)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
matCovarian, selisih = selisih(matrixMean)
# matrix = selisih(matrixMean)
# for i in range (len(matrix)):
#     img = matrix[i]
#     cv2.imshow('imageSelisih',img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# cov_matrix = cov_matrix.astype(np.uint8)
# print(cov_matrix)
# cv2.imshow('imageCov',cov_matrix)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

val, vec = find_eig_qr(matCovarian)
# print(val)
# print(vec)

eigenFace = []
for i in range (len(selisih)):
    matEigFace = vec @ selisih[i]
    # matEigFace = matEigFace.astype(np.uint8)
    # print(i)
    # cv2.imshow('image',matEigFace)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    eigenFace.append(matEigFace)
eigenFace = np.array(eigenFace)

input = 'testcase/Adriana Lima225_126.jpg'
# rows, cols = (256,256)
# matAdd = [[100 for i in range(cols)] for j in range(rows)]
matImg = cv2.imread(input,0)
matImg = cv2.resize(matImg,(256,256))
matImg = matImg[50:206, 50:206]
matImg1 = cv2.resize(matImg,(256,256))
# matImg1 = np.add(matAdd,matImg1)
# print(matImg1)
# cv2.imshow('image',matImg1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
matImg2 = np.subtract(matImg1,matrixMean)
# matImg2 = matImg2.astype(np.uint8)
# matImg = np.round(matImg)
matEigImg = vec @ matImg2
# matEigImg = matEigImg.astype(np.uint8)
# matEigImg = matEigImg.astype(np.uint8)
# print(matEigImg)
# cv2.imshow('image3',matEigImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
count = 0
for i in range (len(eigenFace)):
    dist = np.linalg.norm(matEigImg-eigenFace[i])
    if (i == 0) :
        min = dist
        ayey = i
    else :
        if (min > dist) :
            min = dist
            ayey = i

# print(min)
# cv2.imshow('image2',eigenFace[ayey])
# cv2.waitKey(0)
# cv2.destroyAllWindows()

n = 0
for filename in os.listdir(folder):
    if (n == ayey):
        print(filename)
    n += 1

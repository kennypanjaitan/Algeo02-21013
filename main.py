import os
import cv2
import numpy as np
from qrDecomposition import *
from euclideanDistance import *

width = 256
height = 256

# menyimpan nama training image dalam sebuah array
folder = 'datasett'
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
val, vec = find_eig_qr(matCovarian)


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
# count = 0
# for i in range (len(val)):
#     if (val[i] > 1):
#         count += 1
# print(count) = 104
# print(len(val)) = 105

eigenfaces_used = 104


# mencari weight
w = np.zeros((len(eigenFace),eigenfaces_used))
for i in range (len(eigenFace)):
    for j in range (eigenfaces_used):
        w[i,j] = eigenFace[j] @ normalize_training_img[i]
    

'''_____________________________________________________________________________'''

# membaca test image
foldername = 'testcase/Dwayne Johnson99_1699.jpg'
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


# mencari nama dengan distance minimum dan menampilkan training imagenya
for i in range(len(img_names)):
    if (i == ayey):
        print(img_names[i])
        haha = np.reshape(training_img[i].astype(np.uint8),(height,width))
        cv2.imshow('image',haha)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
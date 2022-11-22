import os
import cv2
import numpy as np
from qrDecomposition import *
from euclideanDistance import *

def training_image(folder):
    width = 256
    height = 256

    # menyimpan nama training image dalam sebuah array
    # folder = 'datasett'
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
    normalize_vector = np.zeros((height*width,len(img_names)))
    normalize_vector = A.transpose() @ vec
        # haha = np.reshape(eigenFace[i+1].astype(np.uint8),(height,width))
        # cv2.imshow('image',haha)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    normalize_vector = normalize_vector.transpose()
    eigenFace = normalize_vector.copy()
    for i in range(len(img_names)):
        eigenFace[i] = np.divide(normalize_vector[i],euclidean_distance((normalize_vector[i]),2))
        # haha = np.reshape(eigenFace[i].astype(np.uint8),(height,width))
        # cv2.imshow('image',haha)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


    # memilih eigen vector yang memiliki eigen value >= 1
    eigenfaces_used = 0
    # for i in range (len(val)):
    #     if (val[i] > 1):
    #         eigenfaces_used += 1
    eigsum = np.sum(val)
    csum = 0
    for i in range (len(val)):
        csum = csum + val[i]
        tv = csum / eigsum
        if tv > 0.95:
            eigenfaces_used = i
            break
    # print(count) = 104
    # print(len(val)) = 105


    # mencari weight
    w = np.zeros((len(eigenFace),eigenfaces_used))
    for i in range (len(eigenFace)):
        for j in range (eigenfaces_used):
            w[i,j] = eigenFace[j] @ normalize_training_img[i]
    
    return w, matMean, eigenfaces_used, eigenFace, img_names, training_img

'''_____________________________________________________________________________'''


def test_image(folder, w, matMean, eigenfaces_used, eigenFace, img_names, training_img):

    width = 256
    height = 256
    
    # membaca test image
    # foldername = 'testcase/Dwayne Johnson99_1699.jpg'
    img = cv2.imread(os.path.join(folder),0)
    img = cv2.resize(img,(width,height))
    test_img = img.reshape(1,height*width)


    # menghitung selisih  / normalize vector
    normalize_test_img = np.subtract(test_img,matMean)
    # haha = np.reshape(normalize_test_img.astype(np.uint8),(height,width))
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
            max = dist[0,i]
            min = dist[0,i]
            ayey = i
        else:
            if (min > dist[0,i]):
                min = dist[0,i]
                ayey = i
            if (max < dist[0,i]):
                max = dist[0,i]
    print(min)


    # mencari nama dengan distance minimum dan menampilkan training imagenya
    for i in range(len(img_names)):
        if (i == ayey):
            if (min < (1/2*(max))):
                print(img_names[i])
                haha = np.reshape(training_img[i].astype(np.uint8),(height,width))
                cv2.imshow('image',haha)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("not found")

# folder = 'datasett'
# w, matMean, eigenfaces_used, eigenFace, img_names, training_img = training_image(folder)
# foldername = 'testcase/Dwayne Johnson99_1699.jpg'
# test_image(foldername, w, matMean, eigenfaces_used, eigenFace, img_names, training_img)
import numpy as np

def euclidean_distance(pointX, pointY):
    temp = np.subtract(pointX,pointY)
    dist = np.sqrt(np.transpose(temp) @ temp)
    return dist
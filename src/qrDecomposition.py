import numpy as np
from euclideanDistance import *

def qr_decomposition(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        #calculate Householder matrix i: rows and i: columns from A i: rows and ith column
        H[i:, i:] = householder(A[i:, i])
        Q = np.matmul(Q,H)
        A = np.matmul(H,A)
    return Q, A
 
def householder(A):
    #find prependicular vector to mirror
    u = A / (A[0] + np.copysign(euclidean_distance(A,0), A[0]))
    u[0] = 1
    H = np.eye(A.shape[0])
    #finding Householder projection
    H -= (2 / np.dot(u, u)) * u[:, None] @ u[None, :]
    return H

def qr_to_eig(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    for i in range(1):
            Q,R = qr_decomposition(X)
            pQ = np.matmul(pQ,Q)
            X = np.matmul(R,Q)
    return np.diag(X), pQ
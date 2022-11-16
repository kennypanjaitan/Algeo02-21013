# Importing NumPy Library
import numpy as np
import sys

# Reading number of unknowns
import numpy as geek
import numpy as np
from sympy import Eq, solve, symbols, Matrix
import sympy as sp, sys

lamd = symbols('λ')
det = 0
matIdentity = geek.identity(3, dtype= int) # bikin matrix identitas
mat = np.array([[2, 1, 0], [1, 2, 0], [0, 0, 3]])
expr = Matrix((lamd * matIdentity) - mat) # bikin persamaan matrixnya
# print(expr)
det = sp.det(expr)

eq1 = sp.Function('eq1')
eq1 = Eq(det, 0) # determinan = 0
sol = solve(eq1)
# print(eq1)
# print(sol)
eigenvalue = Matrix(sol) #dapet eigenvalue
# print(eigenvalue)
# vecMat = Matrix(vec)

for b in range(0, len(eigenvalue), 1):
            vec = Matrix(symbols('v:%d' %len(eigenvalue)))
            subss = expr.subs(lamd, eigenvalue[b]) #substitusi eigenvalue ke matrix
            print(subss)

for c in range(0, len(subss), 1):
                        # for k in range(0, len(subss), 1):
                zeroMat = [[0.0], [0.0], [0.0]]
                matAug = np.append(subss, zeroMat, axis= 1) 
                # print(matAug)

# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix
# a = np.zeros((len(subss), len(subss) + 1))

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(len(matAug))

# Reading augmented matrix coefficients
# print('Enter Augmented Matrix Coefficients:')
# for i in range(len(subss)):
#     for j in range(len(subss)+1):
#         a[i][j] = float(subss)

# Applying Gauss Jordan Elimination
for i in range(len(matAug)):
    if matAug[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
        
    for j in range(len(matAug)):
        if i != j:
            ratio = matAug[j][i]/matAug[i][i]

            for k in range(len(matAug)+1):
                matAug[j][k] = matAug[j][k] - ratio * matAug[i][k]
    print(matAug)

# Obtaining Solution

for i in range(len(matAug)):
    x[i] = matAug[i][len(matAug)]/matAug[i][i]
    print(x[i])
# Displaying solution
print('\nRequired solution is: ')
for i in range(len(matAug)):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
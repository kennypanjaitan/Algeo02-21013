import numpy as geek
import numpy as np
from sympy import Eq, solve, symbols, Matrix
import sympy as sp, sys

lamd = symbols('λ')
det = 0
matIdentity = geek.identity(3, dtype= float) # bikin matrix identitas
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

for i in range(0, len(eigenvalue), 1):
            vec = Matrix(symbols('v:%d' %len(eigenvalue)))
            subss = expr.subs(lamd, eigenvalue[i]) #substitusi eigenvalue ke matrix
            print(subss)

    # bikin matrix augmented
for j in range(0, len(subss), 1):
                        # for k in range(0, len(subss), 1):
                zeroMat = [[0.0], [0.0], [0.0]]
                matAug = np.append(subss, zeroMat, axis= 1) 
                print(matAug)


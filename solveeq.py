import numpy as geek
import numpy as np
from sympy import Eq, solve, symbols, Matrix
import sympy as sp

lamd = symbols('λ')
det = 0

lamd = symbols('λ')
det = 0
mat = np.array([[2, 1, 0], [1, 2, 0], [0, 0, 3]])
matIdentity = geek.identity(len(mat), dtype= float) # bikin matrix identitas
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
    # for j in range(0, len(eigenvalue), 1):
        vec = Matrix(symbols('v:%d' %3))
        # print(vec)
        subss = expr.subs(lamd, eigenvalue[i]) #substitusi eigenvalue ke matrix
        print(subss)
        matt = np.matmul(subss, vec) #matrix yg udh disusbtitusi di kaliin sama variable v
        print(matt)
        eq = Eq(Matrix(matt), 0)
        print(solve(eq))
        # for j in range(0, len(matt), 1):
        #     matAug = Matrix(np.append(matt[j], 0))
        #     print(matAug)

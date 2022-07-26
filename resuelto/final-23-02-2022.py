from numpy import ndarray
import numpy as np
import math

# w' = f(w) = w**3 - 10 w**2 + 10 w + 1

#Ej 1

def soltrsup(A, b):
    n = A.shape[0]
    x = b

    for idx in range(n-1, -1, -1):
        for jdx in range(n-1, idx, -1):
            x[idx] = x[idx] - A[idx, jdx] * x[jdx]
        x[idx] = x[idx] / A[idx, idx]

    return x
    
def egauss(A: ndarray, b: ndarray):
    n = len(b)
    y = np.copy(b)
    U = np.copy(A)


    for k in range(0, n):
        for i in range(k+1, n):
            if(U[k, k] == 0):
                print('El elemento u_kk es cero.')
                return None
            m = U[i, k] / U[k, k]
            for j in range(0, n):
                if j < k+1:
                    U[i, j] = 0
                else:
                    U[i, j] = U[i, j] - m*U[k, j]
            y[i] = y[i] - m*y[k]

    return (U, y)

def soleg(A: ndarray, b:ndarray):
    U, y = egauss(A, b)
    return soltrsup(U, y)


def rbisec(fun, I, err, mit):
    a, b = I[0], I[1]
    u, v = fun(a), fun(b)
    e = abs(b-a)
    hx = []
    hf = []
    if math.copysign(1,u) == math.copysign(1,v): 
        return hx, hf
    for k in range(mit-1):
        e = e/2
        c = a+e
        w = fun(c)
        hx.append(c)
        hf.append(w)
        if abs(e)<err:
            break
        if math.copysign(1,u) != math.copysign(1,w):
            b = c
            v = w
        else:
            a = c
            u = w

    return hx, hf

def f(w):
    return w**3 - 10* w**2 + 10*w + 1 - 0.2

# w' = 0.2 => 0 = = w**3 - 10 w**2 + 10 w + 1 - 0.2 con w entre [8, 10]

U = np.array([
        [3, 1, 1],
        [1, 3, 1],
        [1, 1, 3],
    ], dtype="float"
    )
b = np.array([1, 1, 1], dtype="float")
print(soleg(U,b))

hx, hy = rbisec(f, [8, 10], 1e-5, 100)

print("(w,y,z) = : {}, {}, {}".format(hx[len(hx)-1], soleg(U,b)[2], soleg(U,b)[2]))


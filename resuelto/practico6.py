from numpy import ndarray
import numpy as np
from scipy import linalg

#Ejericio 1
#2020
def soltrsup(A, b):
    n = A.shape[0]
    x = b

    for idx in range(n-1, -1, -1):
        for jdx in range(n-1, idx, -1):
            x[idx] = x[idx] - A[idx, jdx] * x[jdx]
        x[idx] = x[idx] / A[idx, idx]

    return x

def soltrinf(A, b):
    n = A.shape[0]
    x = b
    
    for idx in range(n):
        for jdx in range(idx):
           x[idx] = x[idx] - A[idx, jdx] * x[jdx]
        x[idx] = x[idx] / A[idx, idx]

    return x

#wi
def soltrinf(A: ndarray, b: ndarray) -> ndarray:
    n = len(b)
    #x = np.zeros(n)
    for i in range(0, n):
        sum = 0
        for j in range(0, i):
            sum += x[j] * A[i, j]
        x[i] = (b[i] - sum)/A[i, i]
    return x

def soltrsup(A: ndarray, b: ndarray) -> ndarray:
    B = np.flip(A, 0) # Doy vuelta las filas
    return soltrinf(B, b)

def test_soltrsup():
    U = np.array([
        [1, 1, 1],
        [0, 1, 1],
        [0, 0, 1],
    ], dtype="float"
    )
    b = np.array([3, 2, 1], dtype="float")
    print(soltrsup(U, b)) # Nos deberia dar [1, 1, 1]

#Ejercicio 2
#wil
def egauss(A: ndarray, b: ndarray):
    n = len(b)
    y = np.copy(b)
    U = np.copy(A)


    for k in range(0, n): # por cada pivot
        for i in range(k+1, n): # por cada fila abajo del pivot
            if(U[k, k] == 0):
                print('El elemento u_kk es cero.')
                return None
            m = U[i, k] / U[k, k]
            for j in range(0, n): # por cada elemento de la fila a la derecha de la diagonal(inclusive)
                if j < k+1:
                    U[i, j] = 0
                else:
                    U[i, j] = U[i, j] - m*U[k, j]
            y[i] = y[i] - m*y[k]

    return (U, y)

#Opción 1 - Calcular los ceros de la matriz
def egauss(A_, b_):

    A = A_.copy()
    b = b_.copy()
    n = A.shape[0]

    for k in range(n-1):
        for i in range(k+1,n):
            if A[k,k] == 0:
                print('El elemento a_kk es igual a cero.')
                return None
            
            m = A[i,k] / A[k,k]

            for j in range(k,n):
                A[i,j] = A[i,j] - m * A[k,j]    
            b[i] = b[i] - m * b[k]

    return A, b

def soleg(A: ndarray, b:ndarray):
    U, y = egauss(A, b)
    return soltrsup(U, y)

#Ejercicio 3
def sollu(A, b):
    P, L, U = linalg.lu(A)

    b_tilde = P.T @ b
    y = np.linalg.solve(L, b_tilde) # esto deberia ser soltrinf(L, b_tilde)
    x = soltrsup(U, y)

    return x

#Ejercicio 5
#Opcion 1 (? xd)
def jacobi(A,b,err,mit):
    M = np.diag(np.diag(A))
    N = M - A
    Minv = np.diag(1/np.diag(M))
    x0 = np.zeros(b.shape)

    for k in range(mit):
        x1 = Minv @ ( N @ x0 + b)

        if np.linalg.norm(x1-x0, ord=np.inf) < err:
            break
        else:
            x0 = x1.copy()

    return [x1,k]

#Opcion 2
def jacobi(A,b,err,mit):

    n = A.shape[0]
    x = np.zeros(n)
    x_n = np.zeros(n)
    k = 0
    while k < mit:
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s = s + A[i,j] * x[j]
        
            x_n[i] = (b[i]-s)/A[i,i]
        
        if np.linalg.norm(x_n - x, np.inf) <= err:
            print('La norma infinito de la diferencia es menor que la tolerancia dada')
            return x_n,k
        
        x = x_n
        x_n = np.zeros(n)
        k+=1
        
    return x, ks

def gaussseild(A,b,err,mit):

    n = A.shape[0]
    x = np.zeros(n)
    x_n = np.zeros(n)
    k = 0
    while k < mit:
        for i in range(n):
            s = 0
            for j in range(i-1):
                if j != i:
                    s = s + A[i,j] * x_n[j]
            for j in range(i+1, n):
                if j != i:
                    s = s + A[i,j] * x[j]
        
            x_n[i] = (b[i]-s)/A[i,i]
        
        if np.linalg.norm(x_n - x, np.inf) <= err:
            print('La norma infinito de la diferencia es menor que la tolerancia dada')
            return x_n,k
        
        x = x_n
        x_n = np.zeros(n)
        k+=1
        
    return x, ks

#ej 4
A1 = np.array([[4,-1,0],[-1,4,-1],[0,-1,4]],dtype = float)
A2 = -np.eye(3)

A12 = np.hstack([A1,A2])
A21 = np.hstack([A2,A1])

A = np.vstack([A12,A21])

b1 = np.array([1,1,1,0,0,0], dtype = float)
b2 = np.array([1,1,1,1,1,1], dtype = float)

x11 = soleg(A,b1)
x12 = sollu(A,b1)

x21 = soleg(A,b2)
x22 = sollu(A,b2)

print(x11)
print(x12)
print(x21)
print(x22)

print(np.allclose(A @ x11, b1))
print(np.allclose(A @ x12, b1))
print(np.allclose(A @ x21, b2))
print(np.allclose(A @ x22, b2))


def fact_lu(n, A):
    n = A.shape[0]
    l = np.zeros(n)
    u = np.zeros(n)

    for k in range(n):
        for j in range(k, n):
            s = 0
            for m in range (1, k-1):
                s += l[k,m]*u[m,j]
            u[k,j] = (A[k,j] - s)/ u[k,k]

        for i in range(k+1, n-1):
            s = 0
            for m in range (1, k-1):
                s += l[i,m]*u[m,k]
            l[i,k] = (A[i,k] - s)/ u[k,k]

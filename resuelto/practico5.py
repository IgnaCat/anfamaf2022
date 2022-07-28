import numpy as np
import math
import matplotlib.pyplot as plt
#Ejercicio 1
 
def intenumcomp(fun, a, b, N, regla):
    puntos = np.linspace(a, b, N + 1)
    evals = np.array([fun(x) for x in puntos])
    h = (b - a) / N

    s = 0
    if regla == "pm":
        if N % 2 == 1:
            print("No es intervalo par")
            return None
        s = 2*h * np.sum(evals[1::2])

    elif regla == "simpson":
        #Algoritmo visto en clase
        n = 2 * N
        h = (b-a)/n
        sx0 = fun(a) + fun(b)
        sx1 = 0
        sx2 = 0
        x = a
        for j in range(1, n):
            x = x + h
            if j%2==0:
                sx2 += fun(x)
            else:
                sx1 += fun(x)
        return ( sx0 + 2*sx2 + 4*sx1) * h / 3

    elif regla == "trapecio":
        # puntos sin los extremos usando [1:-1]
        s = (s + fun(a) + 2 * np.sum(evals[1:-1]) + fun(b)) * (h / 2)

    else:
        print("Regla invalida")

    return s

#Ejercicio 3

def senint(x):
    N = math.ceil(x / 0.1) 
    # if N % 2 == 1: # para PM o Simpson necesito N par
    #     N = N + 1

    return intenumcomp(math.cos, 0, x, N, 'trapecio')

x = np.arange(0, 2 * np.pi, 0.5)
y = np.sin(x)
y_aprox = []

for xi in x:
    y_aprox.append(senint(xi))

plt.plot(x, y, label='seno')
plt.plot(x, y_aprox, label='senint')
plt.legend()
plt.show()

def simpson(fun, a: float, b: float, N: int):
    n = 2 * N
    h = (b-a)/n
    sx0 = fun(a) + fun(b)
    sx1 = 0
    sx2 = 0
    x = a
    for j in range(1, n):
        x = x + h
        if j%2==0:
            sx2 += fun(x)
        else:
            sx1 += fun(x)
    return (sx0 + 2*sx2 + 4*sx1) * h / 3

def trap(fun, a: float, b: float, N: int):
    h = (b-a)/N
    sx0 = fun(a) + fun(b)
    sx = 0
    x = a
    for _ in range(1, N):
        x = x+h
        sx += fun(x)
    return (sx0 + 2*sx) * h / 2

def pm(fun, a: float, b: float, N: int):
    h = (b-a)/N #N+2(?
    sx = 0
    x = a
    for _ in range(0, N+1, 2):
        x += 2*h
        sx += fun(x)
    return 2*h*sx
    for _ in range(0, N-1):
        x += h
        sx += fun(x)
    

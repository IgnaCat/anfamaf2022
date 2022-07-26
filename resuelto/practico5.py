import numpy as np
import math
import matplotlib.pyplot as plt
#Ejercicio 1
 
def intenumcomp(fun, a, b, N, regla):
    # Primero debemos definir la partición (puntos) de acuerdo a la cantidad de intervalos que se pide.
    puntos = np.linspace(a, b, N + 1)
    evals = np.array([fun(x) for x in puntos])
    # Definimos el ancho de cada intervalo
    h = (b - a) / N

    s = 0
    if regla == "pm":
        if N % 2 == 1:
            print("No es intervalo par")
            return None
        # Si queremos acceder a todos los nodos impares de un arreglo de Numpy,
        # podemos utilizar el slicing comienzo:fin:paso, que deberíamos
        # reemplazar por 1::2
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
        # Podemos acceder a todos los puntos sin los extremos usando [1:-1]
        s = (s + fun(a) + 2 * np.sum(evals[1:-1]) + fun(b)) * (h / 2)

    else:
        print("Regla invalida")

    return s

#Ejercicio 3

def senint(x):
    N = math.ceil(x / 0.1) # np.ceil nos puede devolver un flotante (OJO)
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

# 5
# print(f"a: {quad(lambda x:np.exp(-x**2), -np.inf, np.inf)}")
# print(f"b: {quad(lambda x:x**2*np.log(x+np.sqrt(x**2+1)), 0, 2)}")

def simp(fun, a: float, b: float, N: int):
    # Este algoritmo aplica la regla de simpson cada 2 subintervalos
    # por ende N aplicaciones => n subintervalos
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
    h = (b-a)/N #N+2?
    sx = 0
    x = a
    for _ in range(0, N+1, 2):
        x += 2*h
        sx += fun(x)
    return 2*h*sx
    for _ in range(0, N-1):
        x += h
        sx += fun(x)
    

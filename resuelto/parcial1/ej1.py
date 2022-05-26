
#Ignacio Martinez Goloboff
#Ejercicio 1

import math

def factorial(n):
    x = 1
    while True :
        if (n-1) == 0 :
            break
        x = x * n
        n = n-1
    return x

def serie_seno(x):
    sum = 0
    for n in range(0, 5):
        sum += (((-1)**n)/factorial(2*n+1))*(x**(2*n+1))

    return sum


#Ignacio Martinez Goloboff
#Ejercicio 2

import numpy as np
import matplotlib.pyplot as plt

x = [0, 1.5, 2, 2.9, 4, 5.6, 6, 7.1, 8.05, 9.2, 10, 11.3, 12]
y = [0.1, 0.2, 1, 0.56, 1.5, 2.0, 2.3, 1.3, 0.8, 0.6, 0.4, 0.3, 0.2]

#Inciso A
def a():
    plt.plot(x, y, "o", label="Datos existentes")
    plt.legend()
    plt.show()

#Inciso B
def trapecio_adaptativo(x, y):
    sum = 0
    for i in range(len(x)-1):
        sum = sum + ((x[i+1] - x[i])/2) * (y[i] + y[i+1])
    return sum

#Inciso C
volumen = (trapecio_adaptativo(x,y))*10
print(f"Deben ser removidos para nivelar el terreno {volumen} m^3")

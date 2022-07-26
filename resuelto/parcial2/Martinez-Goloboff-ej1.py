
#Ignacio Martinez Goloboff
#Ejercicio 1

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#Inciso A
def a():
    data = np.loadtxt("./irma.csv", delimiter=",", dtype="float")
    x = data[:,1]
    y = data[:,2]

    plt.plot(x, y, "o", label="Datos existentes huracan")
    plt.legend()
    plt.show()

#Inciso B
def ilagrange(x, y, z):
    n = len(x)
    w = []
    for k in z:
        sum = 0
        for i in range(n):
            prod = 1
            for j in range(n):
                if (j != i):
                    prod = prod * (k - x[j])/ (x[i] - x[j])
            sum = sum + y[i]*prod
        
        w.append(sum)
    
    return w


data = np.loadtxt("./irma.csv", delimiter=",", dtype="float")
hour = data[:,0].astype(int)
x = data[:,1]
y = data[:,2]
hour_dia = np.arange(0,25)

#Longitud
longitud_lagrange = ilagrange(hour, x, hour_dia)
pol_longitud = interp1d(hour, x, kind='cubic')
longitud_spline = pol_longitud(hour_dia)

#Latitud
latitud_lagrange = ilagrange(hour, y, hour_dia)
pol_latitud = interp1d(hour, y, kind='cubic')
latitud_spline = pol_latitud(hour_dia)

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Inciso B')
ax1.plot(hour,x,'o',label='Datos Longitud')
ax1.plot(hour_dia,longitud_spline,label='Spline Cubico')
ax1.plot(hour_dia, longitud_lagrange, label="Lagrange")
ax1.set_ylabel('Longitud')
ax1.legend()

ax2.plot(hour,y,'o',label='Datos Latitud')
ax2.plot(hour_dia,latitud_lagrange,label='Spline Cubico')
ax2.plot(hour_dia, latitud_spline, label="Lagrange")
ax2.set_ylabel('Latitud')
ax2.legend()

plt.show()





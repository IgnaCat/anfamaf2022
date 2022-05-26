
#Ignacio Martinez Goloboff
#Ejercicio 2

import matplotlib.pyplot as plt
from ej1 import serie_seno

x = [(0.01 * i)+0.01 for i in range(0, 640)]
y = [serie_seno(0.01 * xi) for xi in range(0, 640)]
plt.plot(x, y)

plt.grid()
plt.ylim(-2,8)

plt.show()
plt.savefig('figure.png')



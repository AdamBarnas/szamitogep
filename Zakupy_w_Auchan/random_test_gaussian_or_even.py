#CD = {}

from random import random
import matplotlib.pyplot as plt

lista = []

for i in range(100000):
    lista.append(random())

plt.hist(lista)
plt.show()

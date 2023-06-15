import random
from random import randint

Matriz = []
i = 0
i2 = 0
n = 0
for i in range(5):
    Matriz.append([0] * 5)

while n != 5:
    Matriz[n][i2] = random.randint(1, 10)
    i2 = i2 + 1
    if i2 > 4:
        n = n + 1
        i2 = 0

i = 0
n = 0
i2 = 0
while n != 5:
    if Matriz[n][i2] == 10:
        i = i + 1
    i2 = i2 + 1
    if i2 > 4:
        n = n + 1
        i2 = 0

print(f"Existem {i} Numeros 10 na Matriz {Matriz}")
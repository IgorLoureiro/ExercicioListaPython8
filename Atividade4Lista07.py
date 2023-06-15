import random

Matriz = []
Lista = []
from random import randint
i = 0
i2 = 0

for n in range(4):
    Matriz.append([0] * 4)

while i != 4:
    Matriz[i][i2] = random.randint(1, 100)
    i2 = i2 + 1
    if i2 == 4:
        i = i + 1
        i2 = 0

i = 0
i2 = 0

while i != 4:
    Lista.append(Matriz[i][i2])
    i2 = i2 + 1
    if i2 == 4:
        i = i + 1
        i2 = 0

print(max(Lista))

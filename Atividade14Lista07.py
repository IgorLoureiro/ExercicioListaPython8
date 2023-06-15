import random

Matriz = []
List = []
i = 0
i2 = 0

for n in range(5):
    Matriz.append([0] * 5)

while i < 5:
    r = random.randint(1, 99)
    if r not in List:
        Matriz[i][i2] = r
        List.append(r)
        i2 = i2 + 1
    if i2 == 5:
        i2 = 0
        i = i + 1

print(Matriz)


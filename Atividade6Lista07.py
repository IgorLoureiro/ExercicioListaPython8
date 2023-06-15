import random

Matriz1 = []
Matriz2 = []
Matriz3 = []

for n in range(4):
    Matriz1.append([0] * 4)

for n in range(4):
    Matriz3.append([0] * 4)

for n in range(4):
    Matriz2.append([0] * 4)

i = 0
i2 = 0

while i != 4:
    Matriz1[i][i2] = random.randint(1, 100)
    i2 = i2 + 1
    if i2 == 4:
        i = i + 1
        i2 = 0

i = 0
i2 = 0

while i != 4:
    Matriz2[i][i2] = random.randint(1, 100)
    i2 = i2 + 1
    if i2 == 4:
        i = i + 1
        i2 = 0

i = 0
i2 = 0

while i != 4:
    if Matriz1[i][i2] > Matriz2[i][i2]:
        Matriz3[i][i2] = Matriz1[i][i2]
        i2 = i2 + 1
        if i2 == 4:
            i = i + 1
            i2 = 0
    else:
        Matriz3[i][i2] = Matriz2[i][i2]
        i2 = i2 + 1
        if i2 == 4:
            i = i + 1
            i2 = 0

print(f"Matriz 1 : {Matriz1}")
print(f"Matriz 2: {Matriz2}")
print(f"Matriz 3: {Matriz3}")
Matriz = []

for n in range(4):
    Matriz.append([1] * 4)

for x in range(4):
    print(Matriz[x])

for z in range(4):
    Matriz[z][z] = 0

for x in range(4):
    print(Matriz[x])


import random

Matriz = []
Lista = []
i = 0
i2 = 0

for n in range(5):
    Matriz.append([0] * 5)

while i != 5:
    Matriz[i][i2] = random.randint(1, 100)
    i2 = i2 + 1
    if i2 == 5:
        i = i + 1
        i2 = 0

i = 0
i2 = 0

Num = int(input("Informe um numero para verificar se ele existe na Matriz"))

while i != 5:
    if Matriz[i][i2] == Num:
        print(f"O numero existe na matriz e se encontra na linha {i} coluna {i2}")
        break
    elif Matriz[i][i2] == Matriz[4][4]:
        print("Infelizmente o Numero informado não existe na Matriz")
    elif i2 == 4:
        i = i + 1
        i2 = 0
    else:
        i2 = i2 + 1

import random

Provas = []

for n in range(10):
    Provas.append([0] * 3)

i = 0
i2 = 0
Pior1 = []
Pior2 = []
Pior3 = []
while i < 10:
    Provas[i][i2] = random.randint(1, 10)
    i2 = i2 + 1
    if i2 == 3:
        i2 = 0
        i = i + 1

i = 0
i2 = 0

while i < 10:
    if Provas[i][0] <= Provas[i][1] and Provas[i][0] <= Provas[i][2]:
        Pior1.append(1)
    elif Provas[i][1] <= Provas[i][0] and Provas[i][1] <= Provas[i][2]:
        Pior2.append(1)
    else:
        Pior3.append(1)
    i = i + 1

print(f"A nota dos Alunos com as piores notas na Prova 1 é de {len(Pior1)}")
print(f"A nota dos Alunos com as piores notas na Prova 2 é de {len(Pior2)}")
print(f"A nota dos Alunos com as piores notas na Prova 3 é de {len(Pior3)}")
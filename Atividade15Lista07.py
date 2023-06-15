import random

Prova = []
Alunos = []
Gabarito = ["a", "d", "c", "b", "a", "d", "c", "b", "a", "d"]
Respostas = ["a", "b", "c", "d"]

i = 0
i2 = 0

for n in range(5):
    Prova.append(["z"] * 10)

while i != 5:
    r = random.choice(Respostas)
    Prova[i][i2] = r
    i2 = i2 + 1
    if i2 == 10:
        i = i + 1
        i2 = 0

i = 0
i2 = 0
i3 = 0

while i != 5:
    if Prova[i][i2] == Gabarito[i2]:
        i3 = i3 + 1
    i2 = i2 + 1
    if i2 == 10:
        Alunos.append(i3)
        i3 = 0
        i2 = 0
        i = i + 1

for x in range(5):
    print(f"A nota do Aluno {x} foi de {Alunos[x]}")


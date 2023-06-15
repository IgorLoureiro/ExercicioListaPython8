import random

Vetor = []
Lista = []
i = 0
i2 = 0
for n in range(1, 21):
    Lista.append(n)

while len(Vetor) < 20:
    r = random.choice(Lista)
    Vetor.append(r)

print(f"Vetor antes: {Vetor}")

while i != len(Vetor):
    if i2 > len(Vetor) or i > len(Vetor):
        break
    if Vetor[i] == Vetor[i2] and i != i2:
        del Vetor[i2]
    i2 = i2 + 1
    if i2 == len(Vetor):
        i = i + 1
        i2 = 0

print(f"Vetor depois: {Vetor}")

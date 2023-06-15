import random

Vetor1 = []
Vetor2 = []
VetorRandom = []

for n in range(1, 101):
    VetorRandom.append(n)

for x in range(0, 10):
    Vetor1.append(random.choice(VetorRandom))

for y in range(0, 10):
    Vetor2.append(random.choice(VetorRandom))

Vetor1 = set(Vetor1)
Vetor2 = set(Vetor2)

Vetor3 = Vetor2.union(Vetor1)

Vetor3 = list(Vetor3)

print(Vetor3)

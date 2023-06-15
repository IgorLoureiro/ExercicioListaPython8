Vetor = []

for x in range(0, 50):
    Vetor.append(x)

for n in range(0, 50):
    Vetor[n] = ((n + 5) * n) % (n + 1)

print(Vetor)
print(len(Vetor))
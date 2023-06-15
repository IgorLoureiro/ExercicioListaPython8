Vetor = []

for n in range(1, 101):
    z = n
    List = []
    z = str(z)
    z = list(z)
    if n % 7 != 0 and z[-1] != '7':
        Vetor.append(n)

print(Vetor)

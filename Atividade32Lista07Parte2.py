Vetor1 = []
Vetor2 = []
Vetor3 = [0, 0, 0, 0, 0]
i = 0

while i != 10:
    Num = int(input("Digite um numero \n"))
    i = i + 1
    if len(Vetor1) == 5:
        Vetor2.append(Num)
    else:
        Vetor1.append(Num)

print(f"Vetor 1: {Vetor1}")
print(f"Vetor 2: {Vetor2}")

Pergunta = int(input("Digite \n 1 - Somar os Vetores \n 2 - Multiplicar os vetores \n 3 - Diferença entre os vetores \n"
                     " 4 - Intersecção entre os vetores \n 5 - Intersecção entre os vetores \n 6 - Sair \n"))

match Pergunta:
    case 1:
        for n in range(0, 5):
            Vetor3[n] = Vetor1[n] + Vetor2[n]

        print(Vetor3)
    case 2:
        for n in range(0, 5):
            Vetor3[n] = Vetor1[n] * Vetor2[n]
    case 3:
        Vetor2 = set(Vetor2)
        Vetor1 = set(Vetor1)
        Vetor4 = Vetor1.difference(Vetor2)
        Vetor4 = list(Vetor4)
        print(Vetor4)
    case 4:
        Vetor2 = set(Vetor2)
        Vetor1 = set(Vetor1)
        Vetor4 = Vetor1.intersection(Vetor2)
        Vetor4 = list(Vetor4)
        print(Vetor4)
    case 5:
        Vetor2 = set(Vetor2)
        Vetor1 = set(Vetor1)
        Vetor4 = Vetor1.union(Vetor2)
        print(Vetor4)
    case 6:
        print("Adeus meu amor, que nossas almas se encontrem novamente na vastidão do universo observavel")
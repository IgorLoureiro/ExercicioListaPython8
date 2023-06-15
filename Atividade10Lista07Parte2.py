Matriz = []

while len(Matriz) < 15:
     Num = int(input(f"Digite a nota do seu aluno de numero {len(Matriz) + 1} \n"))
     Matriz.append(Num)

soma = 0

for valor in Matriz:
    soma = soma + valor

print(f"A média das notas foi de {soma/len(Matriz)}")
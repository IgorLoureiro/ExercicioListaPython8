import random

Lista = []
ListaMult = []
i = 0

for n in range(1, 11):
    r = random.randint(1, 100)
    Lista.append(r)

Num = int(input("Informe um numero para ver quantos numeros multiplos deste existem na Matriz: \n"))

for n in range(10):
    if Lista[n] % Num == 0:
        ListaMult.append(Lista[n])

if len(ListaMult) == 0:
    print("Não há multiplos")
else:
    print(f"Existem {len(ListaMult)} multiplos e eles são {ListaMult}")


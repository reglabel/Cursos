from random import sample

numeros = tuple(sample(range(1, 21), 5))
print(f"Você sorteou os números {numeros}.\nO maior valor foi {max(numeros)} e o menor {min(numeros)}.")

"""maiorValor = menorValor = 0
valor1 = valor2 = valor3 = valor4 = valor5 = 0
for i in range(0, 4):
    if i == 0:
        valor1 = randint(0, 20)
        maiorValor = menorValor = valor1
    elif i == 1:
        while True:
            valor2 = randint(0, 20)
            if valor2 != valor1:
                if valor2 > maiorValor:
                    maiorValor = valor2
                if valor2 < menorValor:
                    menorValor = valor2
                break
    elif i == 2:
        while True:
            valor3 = randint(0, 20)
            if valor3 != valor1 and valor3 != valor2:
                if valor3 > maiorValor:
                    maiorValor = valor3
                if valor3 < menorValor:
                    menorValor = valor3
                break
    elif i == 3:
        while True:
            valor4 = randint(0, 20)
            if valor4 != valor1 and valor4 != valor2 and valor4 != valor3:
                if valor4 > maiorValor:
                    maiorValor = valor4
                if valor4 < menorValor:
                    menorValor = valor4
                break
    elif i == 4:
        while True:
            valor5 = randint(0, 20)
            if valor5 != valor1 and valor5 != valor2 and valor5 != valor3 and valor5 != valor4:
                if valor5 > maiorValor:
                    maiorValor = valor5
                if valor5 < menorValor:
                    menorValor = valor5
                break

tupla = (valor1, valor2, valor3, valor4, valor5)
print(f"Os números sorteados foram: {tupla}.\nO maior número foi {maiorValor} e o menor foi {menorValor}.")
"""

"""
from random import randint
numeros = (randint(1,21), randint(1,21), randint(1,21), randint(1,21), randint(1,21))"""

from random import randint
from time import sleep


def sorteio(cadeia):
    print("Sorteando 5 valores da lista: ", end="")
    for j in range(5):
        valor = randint(1, 10)
        cadeia.append(valor)
        print(f"{valor} ", end="")
        sleep(0.5)
    print("PRONTO!")


def somapar(lista):
    print(f"Somando os valores pares de {lista}, temos ", end="")
    soma_dos_pares = 0
    for r in lista:
        if r % 2 == 0:
            soma_dos_pares += r
    sleep(0.5)
    print(soma_dos_pares, ".")


numeros = []
sorteio(numeros)
somapar(numeros)

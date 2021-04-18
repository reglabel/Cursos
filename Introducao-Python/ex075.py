"""valor1 = int(input("Diga um número: ").strip())
valor2 = int(input("Diga um número: ").strip())
valor3 = int(input("Diga um número: ").strip())
valor4 = int(input("Diga um número: ").strip())

tupla = (valor1, valor2, valor3, valor4)"""

"""
tupla = tuple(int(input('Digite o {}º numero: '.format(i+1))) for i in range(4))
"""

tupla = (int(input("Diga um número: ").strip()),
         int(input("Diga um número: ").strip()),
         int(input("Diga um número: ").strip()),
         int(input("Diga um número: ").strip()))
contador = 0

print(f"Os números digitados foram {tupla}.")

"""for i in range(4):
    if tupla[i] == 9:
        contador += 1
print(f"O número 9 foi digitado {contador} vez(es).")"""

print(f"O número 9 foi digitado {tupla.count(9)} vez(es).")

if 3 in tupla:
    procurar_tres = tupla.index(3)
    print(f"O número 3 é o {procurar_tres + 1}º elemento da tupla.")
else:
    print("Não foi digitado o número 3.")

for i in range(4):
    if tupla[i] % 2 == 0:
        print(f"{tupla[i]} é PAR. ", end="")
    else:
        print(f"{tupla[i]} é ÍMPAR. ", end="")

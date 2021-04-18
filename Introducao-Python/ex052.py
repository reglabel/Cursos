# nao tinha conseguido
prova_contra = 0
numero = int(input("Diga um número: "))
for i in range(1, numero + 1):
    if numero % i == 0:
        print("\033[31m", end="")
        prova_contra += 1
    else:
        print("\033[33m", end="")
    print(f"{i} ", end="")
if prova_contra == 2:
    print("\033[m\nEsse número é primo.")
else:
    print("\033[m\nNão é primo.")
soma = 0
for i in range(1, 7):
    numero = int(input("Diga um número: "))
    if numero % 2 == 0:
        soma += numero
print(f"A soma dos pares é {soma}.")
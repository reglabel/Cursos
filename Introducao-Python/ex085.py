numeros = [[], []]
for i in range(7):
    valor = int(input(f"Diga o {i + 1}º número: ").strip())
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
    if i == 6:
        print("-=" * 30, "\nEm ordem crescente:\nPARES: ", end="")
        numeros[0].sort()
        numeros[1].sort()
print(f"{numeros[0]}\nÍMPARES: {numeros[1]}.")

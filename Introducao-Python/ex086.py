tamanho = 3
matriz = [[], [], []]
for i in range(tamanho):
    for j in range(tamanho):
        matriz[i].append(int(input(f"Digte o valor [{i}][{j}]: ").strip()))
print("\n", "-="*17)
for i in range(tamanho):
    for j in range(tamanho):
        print(f"\t[{matriz[i][j]:^5}]", end="")
    print()
print("-="*17)

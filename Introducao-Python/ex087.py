tamanho = 3
matriz = [[], [], []]
soma_pares = soma_terceira_coluna = maior_segunda_linha = 0
for i in range(tamanho):
    for j in range(tamanho):
        matriz[i].append(int(input(f"Digte o valor [{i}][{j}]: ").strip()))
print()
print("-=" * 17)
for i in range(tamanho):
    for j in range(tamanho):
        print(f"\t[{matriz[i][j]:^5}]", end="")
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        if i == 1:
            if j == 0:
                maior_segunda_linha = matriz[i][j]
            else:
                if matriz[i][j] > maior_segunda_linha:
                    maior_segunda_linha = matriz[i][j]
        if j == 2:
            soma_terceira_coluna += matriz[i][j]
    print()
print("-=" * 17, "\n\n", "-=" * 21, f"\n\tA soma de todos os pares foi {soma_pares}.\n\tA "
                                  f"soma da terceira coluna foi {soma_terceira_coluna}.\n\tO "
                                  f"maior valor da segunda linha foi {maior_segunda_linha}.\n", "-=" * 21)

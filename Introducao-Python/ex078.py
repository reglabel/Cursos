valores = []
maior_valor = menor_valor = 0
for i in range(5):
    valores.append(int(input(f"Digite um valor para a posição {i}: ").strip()))
    if i == 0:
        maior_valor = menor_valor = valores[i]
    else:
        if valores[i] > maior_valor:
            maior_valor = valores[i]
        elif valores[i] < menor_valor:
            menor_valor = valores[i]
print(f"\nVocê digitou os valores {valores}.")
print(f"\nO menor valor foi {menor_valor}, na(s) posição(ões):...", end="")
for i in range(5):
    if valores[i] == menor_valor:
        print(f"{i}...", end="")
print(f"\nO maior valor foi {maior_valor}, na(s) posição(ões):...", end="")
for i in range(5):
    if valores[i] == maior_valor:
        print(f"{i}...", end="")

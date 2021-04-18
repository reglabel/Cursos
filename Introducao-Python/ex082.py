valores = []
pares = []
impares = []
while True:
    print("-="*30)
    valores.append(int(input("Diga um valor: ").strip()))
    resposta = str(input("Você deseja continuar? Digite [S]im ou [N]ão.\nSua resposta: ").upper().strip()[0])
    while True:
        if resposta != 'S' and resposta != 'N':
            resposta = str(input("\nResposta inválida. \nDigite [S] ou [N]: ").strip().upper()[0])
        elif resposta == 'S':
            break
        else:
            print("-="*30)
            break
    if resposta == 'N':
        break
print(f"Você digitou, em ordem crescente, os valores {valores}.")
for i in range(len(valores)):
    if valores[i] % 2 == 0:
        pares.append(valores[i])
    else:
        impares.append(valores[i])
print(f"Os valores {pares} foram pares e os valores impares foram {impares}.")

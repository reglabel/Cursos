valores = []
while True:
    valores.append(int(input("Digite um valor: ").strip()))
    while True:
        resposta = str(input("\nDeseja continuar? "
                             "Digite [S]im ou [N]ão.\nSua resposta: ").strip().upper()[0])
        if resposta != 'S' and resposta != 'N':
            print("\nResposta inválida! Tente novamente!")
        elif resposta == 'S':
            print("-="*30)
            break
        elif resposta == 'N':
            print("\n", "-="*30)
            break
    if resposta == 'N':
        break
valores.sort(reverse=True)
print(f"Ao todo, foram digitados {len(valores)} números.\nEm ordem descrescente, são {valores}.")
if 5 in valores:
    print(f"O valor '5' foi encontrado na(s) posição(ões):...", end="")
    for i in range(len(valores)):
        if valores[i] == 5:
            print(f"{i}...", end="")
    print("\nAté a próxima...")
else:
    print("O valor '5' não foi encontrado na lista.")
    print("Até a próxima...")

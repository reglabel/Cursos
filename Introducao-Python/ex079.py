valores = []
resposta = ""
while True:
    valor = int(input("Digite um valor: ").strip())
    if valor in valores:
        print("\nEste valor já foi registrado. Tente outro valor...")
    else:
        valores.append(valor)
        resposta = str(input("Valor adicionado com sucesso!\nDeseja continuar? "
                             "Digite [S]im ou [N]ão.\nSua resposta: ").strip().upper()[0])
        while True:
            if resposta != 'S' and resposta != 'N':
                print("\nResposta inválida! Tente novamente...")
                resposta = str(input("Digite [S]im ou [N]ão.\nSua resposta: ").strip().upper()[0])
            elif resposta == 'S':
                print("-="*30)
                break
            elif resposta == 'N':
                print("\n", "-="*30, "\nEntendido...")
                break
    if resposta == 'N':
        break
valores.sort()
print(f"Você digitou o(s) valor(es) {valores}.\nAté a próxima!")

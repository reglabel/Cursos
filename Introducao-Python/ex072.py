numerosTotais = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
                 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
                 'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DEZESSEIS',
                 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    while True:
        usuario = int(input("Digite um número: ").strip())
        if 0 <= usuario <= 20:
            break
        else:
            print("Tente novamente! ", end='')
    print(f"Você digitou o número {numerosTotais[usuario]}.")
    while True:
        resposta = str(input("Você deseja continuar? Digite [S]im ou [N]ão.\nSua resposta: ").strip().upper()[0])
        if resposta != 'S' and resposta != 'N':
            print("Resposta inválida. Tente novamente.")
        else:
            break
    if resposta == 'N':
        print("Até a próxima.")
        break

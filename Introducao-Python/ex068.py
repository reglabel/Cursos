from random import randint
vitorias = 0
print("Vamos jogar um jogo!")
while True:
    while True:
        jogador = int(input("Escolha um número: ").strip())
        if jogador in range(0, 11):
            break
    computador = randint(0, 10)
    while True:
        escolha = str(input("Você quer par (P) ou ímpar (I)? ").strip().upper()[0])
        if escolha in 'PI':
            break
    resultado = jogador + computador
    if resultado % 2 == 0:
        if escolha == 'P':
            print(f"Parabéns, você venceu! Escolhes-te {jogador} e eu, {computador}, o que deu {resultado}.")
            vitorias += 1
        else:
            print(f"Desculpe, você perdeu. Escolhes-te {jogador} e eu, {computador}, o que deu {resultado}.")
            print(f"Você venceu {vitorias} partida(s).")
            break
    else:
        if escolha == 'I':
            print(f"Parabéns, você venceu! Escolhes-te {jogador} e eu, {computador}, o que deu {resultado}.")
            vitorias += 1
        else:
            print(f"Desculpe, você perdeu. Escolhes-te {jogador} e eu, {computador}, o que deu {resultado}.")
            print(f"Você venceu {vitorias} partida(s).")
            break

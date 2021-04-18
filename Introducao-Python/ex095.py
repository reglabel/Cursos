relatorio_total = []
contador = 0

while True:
    print("-=" * 40)
    dicio = {'jogador': str(input("Nome: ").capitalize().strip())}
    partidas = int(input(f"Quantas partidas {dicio['jogador']} jogou? ").strip())
    registrando_gols = []
    total_de_gols = 0
    for i in range(partidas):
        registrando_gols.append(int(input(f"Quantos gols {dicio['jogador']} fez na {i + 1}º partida? ").strip()))
    dicio['gols'] = registrando_gols[:]
    dicio['total'] = sum(registrando_gols)
    # dicio['partidas'] = partidas

    relatorio_total.append(dicio.copy())
    dicio.clear()

    resposta = str(input("\nVocê deseja continuar ([S]im/[N]ão)?\nSua resposta: ").strip().upper()[0])
    while resposta != 'S' and resposta != 'N':
        resposta = str(input("\nResposta inválida. Digite [S] ou [N]: ").strip().upper()[0])
    if resposta == 'N':
        print()
        print("-=" * 40)
        print("PROCESSANDO...")
        print("-=" * 40, "\n")
        break

# não tinha conseguido fazer tabela bonita
print("-=" * 40, f"\n{'RELATÓRIO FINAL':^50}", f"\n{'CÓDIGO':<5}{'JOGADOR':>20}{'GOLS':>20}{'TOTAL':>20}")
for pos, v in enumerate(relatorio_total):
    print(f"{pos:<5}", end="")
    for d in v.values():
        print(f"{str(d):>20}", end='')
    print()
print("-=" * 40, "\n")

while True:
    print("-=" * 40)
    escolha = int(input("Mostrar dados de qual jogador (999 = SAI DO PROGRAMA)?\nSua resposta: ").strip())
    while escolha < 0 or escolha >= len(relatorio_total):
        if escolha == 999:
            break
        escolha = int(input("Por favor, insira um código válido (999 = SAI DO PROGRAMA).\nSua resposta: ").strip())
        if 0 < escolha < len(relatorio_total) or escolha == 999:
            break
    if escolha == 999:
        print("\nAté a próxima...")
        break
    else:
        print("-=" * 40)
        print(f"O jogador(a) {relatorio_total[escolha]['jogador']} jogou {len(relatorio_total[escolha]['gols'])} partidas.")
        for j, i in enumerate(relatorio_total[escolha]['gols']):
            print(f"\t=> Na {j + 1}º partida, foi/foram {i} gol/gols.")
        print(f"No total, foram {relatorio_total[escolha]['total']} gols.")
        print("-=" * 40, "\n")

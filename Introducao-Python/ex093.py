relatorio = {'Jogador': str(input("Nome: ").capitalize().strip())}
partidas = int(input(f"Quantas partidas {relatorio['Jogador']} jogou? ").strip())
registrando_gols = []
"""total_de_gols = 0"""
for i in range(partidas):
    """contando_gols = int(input(f"Quantos gols {relatorio['Jogador']} fez na {i + 1}º partida? ").strip())
    total_de_gols += contando_gols
    registrando_gols.append(contando_gols)"""
    registrando_gols.append(int(input(f"Quantos gols {relatorio['Jogador']} fez na {i + 1}º partida? ").strip()))
relatorio['Gols'] = registrando_gols[:]
"""relatorio['Total'] = total_de_gols"""
relatorio['Total'] = sum(registrando_gols)
print("-="*40)
print(relatorio)
print("-="*40)
for k, v in relatorio.items():
    print(f"O campo {k} tem valor {v}.")
print("-="*40)
print(f"O jogador(a) {relatorio['Jogador']} jogou {partidas} partidas.")
for j, i in enumerate(relatorio['Gols']):
    print(f"\t=> Na {j + 1}º partida, foi/foram {i} gol/gols.")
print(f"No total, foram {relatorio['Total']} gols.")

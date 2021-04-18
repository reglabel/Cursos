def ficha(nome = "<desconhecido>", gols=0):
	print(f"O jogador {nome} fez {gols} gol(s) no campeonato!")

jogador = str(input("Qual o nome do jogador? ").strip().capitalize())
acertos = str(input("Quantos gols ele fez? ").strip())

if acertos.isnumeric():
	acertos = int(acertos)
else:
	acertos = 0
if jogador == '':
	ficha(gols=acertos)
else:
	ficha(jogador, acertos)

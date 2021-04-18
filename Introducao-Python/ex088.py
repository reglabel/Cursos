from random import randint
from time import sleep

numero_de_jogos = elementos = contador = 0
jogos = []
print("-=" * 30, "\n\t\t\t\t\tJOGO DA MEGA-SENA\n", "-=" * 30)
quantidade = int(input("Quantos jogos você quer gerar?\nSua resposta: ").strip())

for i in range(quantidade):
    jogos.append([])
for i in range(len(jogos)):
    for j in range(6):
        valor = randint(1, 60)
        if valor not in jogos[i]:
            jogos[i].append(valor)
        else:
            while True:
                valor = randint(1, 60)
                if valor not in jogos[i]:
                    jogos[i].append(valor)
                    break

print()
print("-=" * 30)
for i in range(len(jogos)):
    jogos[i].sort()

for i in range(len(jogos)):
    print(f"{i + 1}º JOGO: {jogos[i]}")
    sleep(1)
print("-=" * 12, " BOA SORTE ", "-=" * 12)

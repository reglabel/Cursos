from random import choice
from time import sleep

print("Vamos jogar JOKENPÔ?")
print("Faça sua jogada: PEDRA, PAPEL ou TESOURA?\n")
jogador = str(input("Eu escolho: ").strip().upper())
computador = choice(['TESOURA','PEDRA','PAPEL'])

print("\nJO..." , end="")
sleep(1)
print("KEN...", end="")
sleep(1)
print("PÔ!!!\n")
sleep(1)

if computador == 'TESOURA':
    if jogador == 'PEDRA':
        print(f"Você VENCEU! Eu escolhi {computador}.")
    elif jogador == 'TESOURA':
        print(f"EMPATAMOS! Eu também escolhi {computador}.")
    elif jogador == 'PAPEL':
        print(f"Você PERDEU! Eu escolhi {computador}.")

elif computador == 'PEDRA':
    if jogador == 'PEDRA':
        print(f"EMPATAMOS! Eu também escolhi {computador}.")
    elif jogador == 'TESOURA':
        print(f"Você PERDEU! Eu escolhi {computador}.")
    elif jogador == 'PAPEL':
        print(f"Você VENCEU! Eu escolhi {computador}.")

else:
    if jogador == 'PEDRA':
        print(f"Você PERDEU! Eu escolhi {computador}.")
    elif jogador == 'TESOURA':
        print(f"Você VENCEU! Eu escolhi {computador}.")
    elif jogador == 'PAPEL':
        print(f"EMPATAMOS! Eu também escolhi {computador}.")

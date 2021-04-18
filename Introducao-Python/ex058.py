from random import randint
from time import sleep
jogador = -1
tentativas = 0
computador = randint(0, 10)
resposta_invalida = True
print("Vamos jogar! Vou escolher um número de 0 a 10, tente adivinhá-lo!")
while computador != jogador:
    while resposta_invalida:
        jogador = int(input("\nQual número você acha que eu pensei? ").strip())
        if 0 <= jogador <= 10:
            break
        else:
            continue
    if computador == jogador:
        print("\tPROCESSANDO...")
        sleep(2)
        print("\nPARABÉNS! Você ganhou!")
        tentativas += 1
        break
    else:
        print("\tPROCESSANDO...")
        sleep(2)
        print("Você errou! Vou te dar outra chance! rsrs")
        if jogador > computador:
            print("Uma dica, tente um número menor...")
        if jogador < computador:
            print("Uma dica, tente um número maior...")
        tentativas += 1
print(f"Legal demais, você só precisou de {tentativas} tentativas! hehe")

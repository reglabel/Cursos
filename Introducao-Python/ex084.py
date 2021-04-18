pessoas = []
dados = []
pesado = leve = 0

while True:
    dados.append(str(input("Qual o seu nome? ").strip().capitalize()))
    dados.append(float(input("Qual o seu peso? ").strip()))
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input("\nDeseja continuar? Digite [S]im ou [N]ão.\nSua resposta: ").strip().upper()[0])
    while True:
        if resposta != 'S' and resposta != 'N':
            resposta = str(input("Resposta inválida. Digite [S] ou [N]: ").strip().upper()[0])
        else:
            print("-="*30)
            break
    if resposta == 'N':
        break

for i in range(len(pessoas)):
    if i == 0:
        pesado = leve = pessoas[i][1]
    else:
        if pessoas[i][1] > pesado:
            pesado = pessoas[i][1]
        if pessoas[i][1] < leve:
            leve = pessoas[i][1]

print(f"Ao todo, foram cadastradas {len(pessoas)} pessoas.")
print(f"O maior peso foi o de {pesado}kg, pertecente a:...", end="")
for i in range(len(pessoas)):
    if pessoas[i][1] == pesado:
        print(f"{pessoas[i][0]}...", end="")

print(f"\nO menor peso foi o de {leve}kg, pertencente a:...", end="")
for i in range(len(pessoas)):
    if pessoas[i][1] == leve:
        print(f"{pessoas[i][0]}...", end="")

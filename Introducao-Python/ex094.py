relatorio = []
soma_idades = contador = 0
while True:
    print("-="*30)
    dicio = {'nome': str(input("Nome: ").strip().capitalize())}
    sexo = str(input("Sexo ([F]eminino/[M]asculino): ").strip().upper()[0])
    while sexo != 'F' and sexo != 'M':
        sexo = str(input("\nResposta inválida. Digite [F] ou [M]: ").strip().upper()[0])
    dicio['sexo'] = sexo
    idade = int(input("Idade: ").strip())
    soma_idades += idade
    dicio['idade'] = idade
    relatorio.append(dicio.copy())
    dicio.clear()
    resposta = str(input("\nVocê deseja continuar ([S]im/[N]ão)?\nSua resposta: ").strip().upper()[0])
    while resposta != 'S' and resposta != 'N':
        resposta = str(input("\nResposta inválida. Digite [S] ou [N]: ").strip().upper()[0])
    if resposta == 'N':
        print()
        print("-=" * 30)
        print("PROCESSANDO...")
        print("-=" * 30, "\n")
        break

print("-=" * 30)
print(f"No total, foram cadastradas {len(relatorio)} pessoas.\nA(s) mulher(es) cadastrada(s) foi(ram): ", end="")
media = soma_idades / len(relatorio)
for i in relatorio:
    if i['sexo'] == 'F':
        print(f"{i['nome']}...", end="")
    else:
        contador += 1
if contador == len(relatorio):
    print("...nenhuma mulher foi cadastrada...", end="")
contador = 0
print(f"\nA média das idades cadastradas foi de {media:5.2f} anos.\nA(s) pessoa(s) com idade acima da média foi(ram): ")
for i in relatorio:
    if i['idade'] > media:
        print(f"\t => NOME: {i['nome']}, IDADE: {i['idade']}, SEXO: {i['sexo']}")
    else:
        contador += 1
if contador == len(relatorio):
    print("...nenhuma pessoa com idade acima da média foi cadastrada...")
print("-=" * 30)

"""lista = []
for i in range(5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Valor adicionado no final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f"Valor adicionado na posição {posicao} da lista...")
                break
            posicao += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}.')"""

valores = []
j = posicao = 0
for i in range(5):
    valor = int(input("Digite um valor: ").strip())
    if i == 0:
        valores.append(valor)
        print("Valor adicionado no final da lista...")
    else:
        for j in range(len(valores)):
            posicao = 0
            if valor <= valores[j]:
                if valores[(len(valores) - 1)] == valor:
                    valores.append(valor)
                    print("Valor adicionado no final da lista...")
                    break
                else:
                    valores.insert(j, valor)
                    print(f"Valor adicionado na posição {j}...")
                    break
            elif valor > valores[j]:
                if len(valores) == 1:
                    valores.append(valor)
                    print("Valor adicionado no final da lista...")
                    break
                else:
                    for r in range(len(valores)):
                        if valor > valores[r]:
                            posicao = r + 1
                    if (len(valores)) == posicao:
                        valores.append(valor)
                        print("Valor adicionado no final da lista...")
                        break
                    else:
                        valores.insert(posicao, valor)
                        print(f"Valor adicionado na posição {posicao}...")
                        break
print("\n", "-="*30, f"\nVocê digitou, em ordem crescente, os valores: {valores}.")

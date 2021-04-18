# tinha tentado fazer com o len(numeros) e botar o maior_valor =
# numeros[0], só que tinha que fazer um if especial pro caso da função
# não receber nenhum parâmetro, pq dar erro chamar algo q não existe

from time import sleep


def maior(* numeros):
    maior_valor = contador = 0
    print("-=" * 30, f"\nAnalisando os valores passados...\n ->", end="")
    for i in numeros:
        print(f" {i}", end="")
        sleep(0.3)
        if contador == 0:
            maior_valor = i
        else:
            if i > maior_valor:
                maior_valor = i
        contador += 1
    print(f"\nForam {contador} valores ao todo.\n"
          f"O maior valor informado foi {maior_valor}.\n", "-=" * 30, "\n")
    sleep(2.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

"""# primeiro tinha feito essa versão com lista


def maior(valores):
    for i in range(len(valores)):
        if i == 0:
            maior_valor = valores[0]
        else:
            if valores[i] > maior_valor:
                maior_valor = valores[i]
    print(maior_valor)


numeros = []
while True:
    numeros.append(int(input("Diga um valor: ").strip()))
    while True:
        resposta = str(input("Deseja continuar ([S] ou [N]): ").strip().upper()[0])
        if resposta not in 'NS':
            print("Resposta Inválida! ", end="")
        else:
            break
    if resposta == 'N':
        break
maior(numeros)"""

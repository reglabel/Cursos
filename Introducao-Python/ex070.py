nomeMaisBarato = ''
maisDe1000 = totalGasto = produtos = maisBarato = 0
while True:
    print("\n", "-="*20)
    nome = str(input("Nome do produto: ").strip().upper())
    preco = float(input("Preço do produto: R$").strip())
    produtos += 1
    totalGasto += preco
    if preco > 1000:
        maisDe1000 += 1
    if produtos == 1 or preco < maisBarato:
        maisBarato = preco
        nomeMaisBarato = nome
    while True:
        resposta = str(input("\nDeseja continuar [S/N]? ").strip().upper()[0])
        if resposta in 'SN':
            break
    if resposta == 'N':
        break
print("\n", "-="*20)
print("FIM da compra!")
print(f"Você comprou {produtos} produto(s). Ao todo, {maisDe1000} produto(s) custaram mais de R$1000,00.")
print(f"O produto mais barato foi {nomeMaisBarato}, que custou R${maisBarato:.2f}.")
print(f"O valor total da compra foi de R${totalGasto:.2f}.")

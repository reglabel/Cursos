homens = maiores = mulheresMenores = 0
while True:
    print("\n", "-="*20)
    print("Cadastre uma pessoa!")
    print("-="*20)
    while True:
        sexo = str(input("Qual o seu sexo [F/M]? ").strip().upper()[0])
        if sexo in 'FM':
            break
    idade = int(input("Qual a sua idade? ").strip())
    if sexo == 'F' and idade < 20:
        mulheresMenores += 1
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        maiores += 1
    while True:
        resposta = str(input("\nDeseja continuar [S/N]? ").strip().upper()[0])
        if resposta in 'SN':
            break
    if resposta == 'N':
        break
print(f"Você cadastrou {homens} homens, {mulheresMenores} mulheres com menos de 20 anos e {maiores} maiores.")

valor = float(input("Qual o valor do produto? R$").strip())
print("Essas são as formas de pagamento: \n1) A vista ou em cheque\n2) A vista no cartão")
print("3) Até 2x no cartão\n4) De 3x ou mais no cartão")

escolha = int(input("Digite sua escolha: ").strip())

if escolha == 1:
    print(f"O valor a ser pago deve ser de R${(valor * 0.9):.2f}, considerando desconto de 10%.")
elif escolha == 2:
    print(f"O valor a ser pago deve ser de R${(valor * 0.95):.2f}, considerando desconto de 5%.")
elif escolha == 3:
    print(f"O valor a ser pago deve ser de R${valor :.2f}, sem descontos ou juros.")
elif escolha == 4:
    print(f"O valor a ser pago deve ser de R${(valor * 1.2):.2f}, considerando juros de 20%.")

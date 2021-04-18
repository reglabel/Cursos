from datetime import date
maiores = 0
menores = 0
for i in range(1, 8):
    nascimento = int(input("Qual o seu ano de nascimento? "))
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f"Ao todo, temos {maiores} pessoas maiores de 18 anos e {menores} menores de idade.")
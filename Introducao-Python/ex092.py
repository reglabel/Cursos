from datetime import date
dados = {'Nome': str(input("Nome: ").capitalize().strip())}
nascimento = int(input("Ano de nascimento: ").strip())
dados['Idade'] = date.today().year - nascimento
dados['CTPS'] = int(input("Carteira de trabalho (0 = NÂO tem): ").strip())
if dados['CTPS'] != 0:
    contratacao = int(input("Ano de contratação: ").strip())
    dados['Ano de contratação'] = contratacao
    dados['Salário'] = float(input("Salário: R$").strip())
    dados['Aposentadoria'] = (contratacao + 35) - nascimento
print("-="*30)
for k, v in dados.items():
    print(f"{k} tem o valor de {v}.")
print("-="*30)

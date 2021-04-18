from datetime import date
data_atual = date.today()
ano_atual = data_atual.year

nascimento = int(input("Qual o seu ano de nascimento? ").strip())
idade = ano_atual - nascimento

if idade < 10:
    print(f"Você tem {idade} anos, logo, está na categoria MIRIM.")
elif idade < 15:
    print(f"Você tem {idade} anos, logo, está na categoria INFANTIL.")
elif idade < 20:
    print(f"Você tem {idade} anos, logo, está na categoria JUNIOR.")
elif idade < 21:
    print(f"Você tem {idade} anos, logo, está na categoria SÊNIOR.")
else:
    print(f"Você tem {idade} anos, logo, está na categoria MASTER.")
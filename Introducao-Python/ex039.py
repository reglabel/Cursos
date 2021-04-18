from datetime import date

ano_atual = date.today().year
nascimento = int(input("Em que ano você nasceu?").strip())
idade = ano_atual - nascimento

if idade < 18:
    falta = 18 - idade
    print(f"Você ainda vai precisar se alistar no Exército, no ano de {ano_atual + falta}.", end="")
    print(f" Logo, falta(m) {falta} ano(s).")
elif idade == 18:
    print("Você precisa se alistar no Exército neste ano.")
else:
    atraso = idade - 18
    print(f"Você está atrasado em {atraso} ano(s). Deveria ter se inscrito no Exército em {ano_atual - atraso}.")

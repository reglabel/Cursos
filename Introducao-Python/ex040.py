primeira_nota = float(input("Diga sua primeira nota: ").strip())
segunda_nota = float(input("Diga sua segunda nota: ").strip())

media = (primeira_nota + segunda_nota) / 2

if media < 5.0:
    print(f"A sua média é igual a {media:.2f}. Você foi REPROVADO.")
elif media < 6.9:
    print(f"A sua média é igual a {media:.2f}. Você está de RECUPERAÇÃO.")
else:
    print(f"A sua média é igual a {media:.2f}. Você foi APROVADO.")

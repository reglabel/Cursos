somaValor = quantidade = 0
while True:
    valor = int(input("Diga um número (digite 999 para parar): ").strip())
    if valor != 999:
        somaValor += valor
        quantidade += 1
    else:
        break
print(f"Acabou! Você digitou {quantidade} valores e a soma deles é {somaValor}.")

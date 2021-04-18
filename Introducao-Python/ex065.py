resposta = "S"
numero = media_numeros = numeros_lidos = soma_numeros = maior_numero = menor_numero = 0
while resposta == "S":
    numero = float(input("Diga um valor: ").strip())
    numeros_lidos += 1
    soma_numeros += numero
    if numeros_lidos == 1:
        maior_numero = menor_numero = numero
    else:
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero
    resposta = str(input("Você deseja continuar ('S' para sim e 'N' para não)? ").upper().strip()[0])
print("Acabou!")
media_numeros = soma_numeros / numeros_lidos
print(f"A média dos {numeros_lidos} números lidos foi de {media_numeros:.1f}.")
print(f"O menor número lido foi {menor_numero} e o maior foi {maior_numero}.")

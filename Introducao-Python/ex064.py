numero = soma_dos_numeros = quantidade_numeros = 0
while numero != 999:
    numero = int(input("Diga um valor: ").strip())
    if numero != 999:
        soma_dos_numeros += numero
        quantidade_numeros += 1
print("Acabou!")
print(f"A soma dos {quantidade_numeros} números digitados foi {soma_dos_numeros}.")

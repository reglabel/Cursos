frase = str(input("Diga uma frase: ").upper().replace(" ", ""))
frase_original = frase
frase_inversa = frase[::-1]
if frase_inversa == frase_original:
    print("Esse frase é uma palíndroma.")
else:
    print("Esse frase não é uma palindroma.")

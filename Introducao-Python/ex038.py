primeiroValor = int(input("Diga um número inteiro: "))
segundoValor = int(input("Diga outro número inteiro: "))
if primeiroValor > segundoValor:
    print(f"O número {primeiroValor} é maior que o número {segundoValor}.")
elif segundoValor > primeiroValor:
    print(f"O número {segundoValor} é maior que o número {primeiroValor}.")
else:
    print("Os dois números são iguais.")
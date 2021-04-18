valor = int(input("Diga um valor: ").strip())
print(f"Uma sequência de Fibonacci com {valor} termos tem a seguinte configuração: ")
primeiro_elemento = 0
segundo_elemento = 1
elemento = 0
if valor == 1:
    print("0")
elif valor == 2:
    print("0 - 1")
else:
    valor -= 2
    print("0 - 1 ", end="")
    while valor > 0:
        elemento = primeiro_elemento + segundo_elemento
        primeiro_elemento = segundo_elemento
        segundo_elemento = elemento
        valor -= 1
        print(f"- {elemento} ", end="")

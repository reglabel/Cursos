numero = int(input("Diga um número maior que 1: ").strip())
fatorial_da_vez = numero
resultado = 1
contador = True
while fatorial_da_vez > 1:
    if contador:
        resultado = fatorial_da_vez
        print(f"Calculando {numero}! temos = {numero} ", end= "")
        contador = False
    else:
        fatorial_da_vez = fatorial_da_vez - 1
        resultado = resultado * fatorial_da_vez
        print(f"x {fatorial_da_vez} ", end="")
print(f" = {resultado}.")

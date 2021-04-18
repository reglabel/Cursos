tupla = ('CAIXA DE BOMBONS', 9.0 , 'COMPUTADOR', 1800.0, 'BOLO', 20.0,
         'MOUSSE', 5.0, 'SORVETE', 12.0, 'VIDEO GAME', 2000.0,
         'DEZZER', 11.0, 'BICICLETA', 300.0, 'NETFLIX', 32.0)
print("-=" * 21, "\n\t\t\tLISTAGEM DE PREÇOS")
print("-=" * 21, "\nPRODUTOS\t\t\t\t\t\tPREÇO")
for i in range(0, 18, 2):
    print(f"{tupla[i]:.<30}R${tupla[i + 1]:>7.2f}")
print("-=" * 21)

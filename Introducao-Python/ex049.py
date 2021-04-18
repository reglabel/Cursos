numero = int(input('Você quer a tabuada de qual número? '))
print(f"Está é a tabuada de {numero}:")
for i in range(1, 11):
    print(i, " x ", numero, " = ", numero*i)

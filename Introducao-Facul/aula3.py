for valor in [2, 3, 4, 9]:
    print(valor)

for valor in range(5, 10+1, 2):
    print(valor)

for valor in range(9, 5-1, -2):
    print(valor)

estante = ["garrafa", "celular", 3, True, [1, 2]]

for item in estante:
    print(item)

for item in estante[4]:
    print(item)
estante.append("Junior")


while True:
    print("Trava")
    break

x = 1
while x <= 10:
    print(x)
    x = x + 1

while True:
    opcao = int(input("1 - imprimir ou 0 - sair"))
    if opcao == 1:
        print("Opção 1")
    elif opcao == 0:
        break
    else:
        print("Opção inválida")

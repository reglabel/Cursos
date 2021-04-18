valor1 = float(input("Diga um valor: ").strip())
valor2 = float(input("Diga outro: ").strip())
resposta = 0
while resposta != 5:
    print("\n", "-="*20)
    print("Observe essas opções:\n1) Somar\n2) Multiplicar\n3) Qual o maior\n4) Novos números\n5) Sair do programa")
    resposta = int(input("O que deseja fazer? ").strip())
    if resposta == 5:
        print("\nAté mais!")
        break
    elif resposta == 4:
        valor1 = float(input("\nDigite um novo valor: ").strip())
        valor2 = float(input("Digite outro: ").strip())
    elif resposta == 3:
        if valor1 > valor2:
            print(f"\nO número {valor1} é maior que o {valor2}.")
        elif valor2 > valor1:
            print(f"\nO número {valor2} é maior que o {valor1}.")
        else:
            print("\nOs dois valores são iguais, não há maior ou menor.")
    elif resposta == 2:
        print(f"\nA multiplicação desses valores resulta no valor {(valor1 * valor2):.2f}.")
    elif resposta == 1:
        print(f"\nA soma desses valores resulta no valor {(valor1 + valor2):.2f}.")
    else:
        print("\nOpção inválida!")

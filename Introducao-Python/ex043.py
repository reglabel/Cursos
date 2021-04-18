peso = float(input("Qual o seu peso? ").strip())
altura = float(input("Qual a sua altura? ").strip())

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Seu IMC é {imc:.1f}. Você está abaixo do peso.")
elif imc < 25:
    print(f"Seu IMC é {imc:.1f}. Você está com o peso ideal.")
elif imc < 30:
    print(f"Seu IMC é {imc:.1f}. Você está abaixo com sobrepeso.")
elif imc < 40:
    print(f"Seu IMC é {imc:.1f}. Você está com obesidade.")
else:
    print(f"Seu IMC é {imc:.1f}. Você está com obesidade mórbida.")

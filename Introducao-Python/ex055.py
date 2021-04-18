peso_maior = 0.0
peso_menor = 99999.0
for i in range(1, 6):
    peso = float(input("Qual é o seu peso (em kg)? "))
    if peso > peso_maior:
        peso_maior = peso
    if peso < peso_menor:
        peso_menor = peso
print(f"O maior peso foi {peso_maior}kg e o menor foi {peso_menor}kg.")

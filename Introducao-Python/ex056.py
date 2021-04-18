soma_idade = 0
media_idade = 0.0
maior_idade = 0
o_mais_velho = 'vc'
mulheres_jovens = 0
for i in range(1,5):
    print(f"\nVocê é a {i}º pessoa.")
    nome = str(input("Qual o seu nome? ").strip().capitalize())
    idade = int(input("Qual a sua idade? "))
    soma_idade += idade
    sexo = str(input("Qual o seu sexo? Digite 'FEMININO' ou 'MASCULINO'. ").strip().upper())
    if idade > maior_idade and sexo == 'MASCULINO':
        maior_idade = idade
        o_mais_velho = nome
    if sexo == 'FEMININO' and idade < 20:
        mulheres_jovens += 1
media_idade = soma_idade / 4
print(f"Das quatro pessoas analisadas, o senhor {o_mais_velho} é o homem mais velho, com {maior_idade} anos.")
print(f"A média da idade do grupo é de {media_idade} anos e temos {mulheres_jovens} mulheres com menos de 21 anos.")

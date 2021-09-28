# nome = input("Digite seu nome: ")
# print(f"Prazer em conhecê-lo, {nome}")

# idade = int(input("Digite sua idade: "))
# print(type(idade))
# print(f"Sua idade é {idade}")

mulher = True
bonita = True
eu = False
inteligente = True
bolso = 1000
tornoseleira = True
meubolso = 2000

if not mulher:
    print("não deu match")
elif bonita and eu and not tornoseleira:
    print("vou ver e te aviso")
elif inteligente and eu and not tornoseleira:
    print("vo nada")
elif 50 <= bolso < meubolso:
    print("vou pensar")
else:
    print("não deu")

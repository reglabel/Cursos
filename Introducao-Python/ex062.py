razao = int(input("Qual a razão da PA? "))
primeiro_termo = int(input("Qual o primeiro termo? "))
print(f"Os dez primeiros termos da PA são ", end="")
numero_do_termo = 1
quantidade = 10
while numero_do_termo <= 10:
    termo = primeiro_termo + ((numero_do_termo - 1) * razao)
    numero_do_termo += 1
    print(f"{termo}", end="")
    print(", " if numero_do_termo <= 10 else ".", end="")
print("\nVocê quer mostrar mais quantos termos (digite 0 pra encerrar o programa)?")
resposta = int(input("Sua resposta: ").strip())
while resposta != 0:
    quantidade += resposta
    numeros = numero_do_termo + resposta - 1
    print(f"Os próximos {resposta} termos são ", end="")
    while numero_do_termo <= numeros:
        termo = primeiro_termo + ((numero_do_termo - 1) * razao)
        numero_do_termo += 1
        print(f"{termo}", end="")
        print(", " if numero_do_termo <= numeros else ".", end="")
    print("\nVocê quer mostrar mais quantos termos (digite 0 pra encerrar o programa)?")
    resposta = int(input("Sua resposta: ").strip())
    if resposta == 0:
        print("Acabou!")
        break
print(f"Legal! Você viu {quantidade} termos!")
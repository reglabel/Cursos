razao = int(input("Qual a razão da PA? "))
primeiro_termo = int(input("Qual o primeiro termo? "))
print(f"Os dez primeiros termos da PA são ", end="")
numero_do_termo = 1
while numero_do_termo <= 10:
    termo = primeiro_termo + ((numero_do_termo - 1) * razao)
    numero_do_termo += 1
    print(f"{termo}", end="")
    print(", " if numero_do_termo <= 10 else ".", end="")

razao = int(input("Qual a razão da PA? "))
primeiro_termo = int(input("Qual o primeiro termo? "))
print(f"Os dez primeiros termos da PA são ", end="")
for numero_do_termo in range(1, 11):
    termo = primeiro_termo + ((numero_do_termo - 1) * razao)
    print(f"{termo}, ", end="")
print("portanto.")
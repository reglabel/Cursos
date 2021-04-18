notas50 = notas20 = notas10 = notas1 = 0
valor = int(input("Diga o valor que deseja sacar: R$").strip())
while valor > 0:
    if valor >= 50:
        notas50 = valor // 50
        valor -= 50 * notas50
    if valor >= 20:
        notas20 = valor // 20
        valor -= 20 * notas20
    if valor >= 10:
        notas10 = valor // 10
        valor -= 10 * notas10
    if valor >= 1:
        notas1 = valor // 1
        valor -= 1 * notas1
if notas50 > 0:
    print(f"São {notas50} notas de R$50.0.")
if notas20 > 0:
    print(f"São {notas20} notas de R$20.0.")
if notas10 > 0:
    print(f"São {notas10} notas de R$10.0.")
if notas1 > 0:
    print(f"São {notas1} notas de R$1.0.")

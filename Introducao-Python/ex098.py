# fiz essa primeira versão errada (não consegui passar
# os parâmetros):
"""def contador():
    from time import sleep

    print("-=" * 30, f"\n{'CONTANDO DE 1 A 10, DE 1 EM 1':^60}\n", "-=" * 30, "\n\t-> ", end="")
    for i in range(1, 11, 1):
        print(f" {i} ", end="")
        sleep(0.3)
    print(f"  FIM!\n")

    print("-=" * 30, f"\n{'CONTANDO DE 10 A 0, DE 2 EM 2':^60}\n", "-=" * 30, "\n\t-> ", end="")
    for i in range(10, -1, -2):
        print(f" {i} ", end="")
        sleep(0.3)
    print(f"  FIM!\n")

    print("-=" * 30, f"\n{'AORA É SUA VEZ DE PERSONALIZAR A CONTAGEM!':^60}\n",
          "-=" * 30)

    inicio = int(input("Início: ").strip())
    fim = int(input("Fim: ").strip())
    passo = int(input("Passo: ").strip())

    if passo < 0:
        passo = abs(passo)
    elif passo == 0:
        passo = 1

    if fim > inicio:
        print("-=" * 30, f"\n\n{f'CONTANDO DE {inicio} A {fim}, DE {passo} EM {passo}':^60}\n",
              "-=" * 30, "\n\t-> ", end="")
        for i in range(inicio, fim + 1, passo):
            print(f" {i} ", end="")
            sleep(0.3)
        print(f"  FIM!\n")

    elif inicio > fim:
        print("-=" * 30, f"\n\n{f'CONTANDO DE {inicio} A {fim}, DE {passo} EM {passo}':^60}\n",
              "-=" * 30, "\n\t-> ", end="")
        for i in range(inicio, fim - 1, -passo):
            print(f" {i} ", end="")
            sleep(0.3)
        print(f"  FIM!\n")

    else:
        print("\n\n\t-> Inicio e fim iguais. Não temos contagem aqui.", end="")


contador()
"""


def contador(inicio, fim, passo):
    from time import sleep

    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1

    if fim > inicio:
        print("-=" * 30, f"\n{f'CONTANDO DE {inicio} A {fim}, DE {passo} EM {passo}':^60}\n",
              "-=" * 30, "\n\t-> ", end="")
        sleep(2.5)
        incremento = inicio
        while incremento <= fim:
            print(f" {incremento} ", end="")
            incremento += passo
            sleep(0.3)
        print(f"  FIM!\n")

    elif inicio > fim:
        print("-=" * 30, f"\n{f'CONTANDO DE {inicio} A {fim}, DE {passo} EM {passo}':^60}\n",
              "-=" * 30, "\n\t-> ", end="")
        sleep(2.5)
        incremento = inicio
        while incremento >= fim:
            print(f" {incremento} ", end="")
            incremento -= passo
            sleep(0.3)
        print(f"  FIM!\n")

    else:
        print("\n\n\t-> Inicio e fim iguais. Não temos contagem aqui.", end="")


contador(1, 10, 1)
contador(10, 0, 2)
print("-=" * 30, f"\n{'AORA É SUA VEZ DE PERSONALIZAR A CONTAGEM!':^60}\n",
      "-=" * 30)
i = int(input("Início: ").strip())
f = int(input("Fim: ").strip())
p = int(input("Passo: ").strip())
contador(i, f, p)

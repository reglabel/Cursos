from time import sleep
print("-="*30, "\n\t\t\t\tCOLETA DE DADOS")
relatorio = []
contador = 0
while True:
    print("-="*30)
    relatorio.append([[]])
    relatorio[contador].insert(0, str(input("Nome: ").strip().capitalize()))
    relatorio[contador][1].append(float(input("1º Nota: ").strip()))
    relatorio[contador][1].append(float(input("2º Nota: ").strip()))
    relatorio[contador].append((relatorio[contador][1][0] + relatorio[contador][1][1])/2)
    contador += 1
    resposta = str(input("\nDeseja continuar? Digite [S]im ou [N]ão.\nSua resposta: ").upper().strip()[0])
    while resposta != 'S' and resposta != 'N':
        resposta = str(input("Resposta inválida. Digite [S]im ou [N]ão.\nSua resposta: ").upper().strip()[0])
    if resposta == 'N':
        break
print("\n", "-="*30, "\n\t\t\t\tRELATÓRIO FINAL\n", "-="*30, f"\n\t\t\t{'No.':<6}{'NOME':<10}{'MÉDIA':>8}")
for i in range(len(relatorio)):
    print(f"\t\t\t{i:<6}{relatorio[i][0]:<10}{relatorio[i][2]:>8.1f}")
    sleep(1)
print("-="*30, "\n")
while True:
    print("-=" * 30)
    analise = int(input("Mostrar a nota de qual aluno?\n\t(999 = PARAR PROGRAMA)\nSua resposta: ").strip())
    if analise == 999:
        print("FINALIZANDO...")
        sleep(1)
        print("\nAté a próxima.")
        break
    else:
        if len(relatorio) > analise >= 0:
            print(f"NOTAS DO ALUNO '{relatorio[analise][0]}': "
                  f"[{relatorio[analise][1][0]:.1f}] E [{relatorio[analise][1][1]:.1f}]")
        else:
            while True:
                analise = int(input(f"Número de aluno inválido. Escolha entre "
                           f"0 e {len(relatorio) - 1} OU 999 para interromper.\nSua resposta: ").strip())
                if len(relatorio) > analise >= 0 or analise == 999:
                    if analise == 999:
                        print("FINALIZANDO...")
                        sleep(1)
                        print("\nAté a próxima.")
                        break
                    else:
                        print(f"NOTAS DO ALUNO '{relatorio[analise][0]}': "
                              f"[{relatorio[analise][1][0]:.1f}] E [{relatorio[analise][1][1]:.1f}]")
                        break
    if analise == 999:
        break

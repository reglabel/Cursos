frase = list(str(input("Digite uma frase: ").strip().upper()))
parenteses = frase.count('(') + frase.count(')')
ocorrencia_certa = 0
for i in range(parenteses):
    if '(' in frase:
        if ')' in frase:
            if frase.index('(') < frase.index(')'):
                ocorrencia_certa += 1
                frase.remove('(')
                frase.remove(')')
if ocorrencia_certa == (parenteses / 2):
    print("Sua expressão é válida.")
else:
    print("Sua expressão não é válida.")

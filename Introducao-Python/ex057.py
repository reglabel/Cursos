sexo = ''
vez_do_programa = 0
while sexo != 'F' and sexo != 'M':
    if vez_do_programa > 0:
        print("Opção INVÁLIDA! ", end="")
    sexo = str(input("Qual o seu sexo? Digite 'F' para feminino e 'M' para masculino. ").strip().upper()[0])
    vez_do_programa += 1
if sexo == 'F':
    print("Você é uma mulher!")
else:
    print("Você é um homem!")
print("Acabou!")

"""tupla = ('EMINEM', 'REALITY', 'LAB', 'MUSIC', 'ME', 'LIFE', 'MOMENT',
         'SHOT', 'OPORTUNITY', 'KING', 'DAUGHTER', 'LOSE', 'RAP', 'PAIN', 'FAMILY')

vogais = ('A', 'E', 'I', 'O', 'U')
for i in range(len(tupla)):
    print(f"\nA palavra {tupla[i]} possui as vogais: ", end="")
    for j in range(5):
        if vogais[j] in tupla[i]:
            print(f"{vogais[j]} ", end="")"""

tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for i in range(len(tupla)):
    print(f"\nA palavra {tupla[i]} possui as vogais: ", end="")
    for j in tupla[i]:
        if j in 'AEIOU':
            print(f"{j} ", end="")

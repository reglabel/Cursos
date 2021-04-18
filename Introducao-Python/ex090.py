dicio = {'NOME': str(input("Qual o nome do aluno? ").capitalize().strip()),
         'MÉDIA': float(input("Qual a média do aluno? ").strip())}
if 5.00 <= dicio['MÉDIA'] < 7.00:
    dicio['SITUAÇÃO'] = 'RECUPERAÇÃO(A)'
elif dicio['MÉDIA'] < 5.00:
    dicio['SITUAÇÃO'] = 'REPROVADO(A)'
else:
    dicio['SITUAÇÃO'] = 'APROVADO(A)'
print(f"\nO nome do aluno(a) é: {dicio['NOME']}\n"
      f"Sua média é: {dicio['MÉDIA']:.2f}\n"
      f"Sua situação é: {dicio['SITUAÇÃO']}")

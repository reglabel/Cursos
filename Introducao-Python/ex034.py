from time import sleep
n = float(input('Diga o seu salário. R$').strip())
print('CALCULANDO SEU AUMENTO...')
sleep(3)
if n > 1250:
    print('Seu novo salário é: R${:.2f}!'.format(n*1.10))
else:
    print('Seu novo salário é: R${:.2f}!'.format(n*1.15))

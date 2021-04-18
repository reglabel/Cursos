v = int(input('Qual o valor da casa? R$').strip())
s = int(input('Qual o valor do seu salário? R$').strip())
a = int(input('Em quantos anos você deseja poder pagar? ').strip())
parcela = v / (a * 12)
if parcela > (0.3 * s):
    print('Seu empréstimo foi {}negado{}.'.format('\033[31;1m', '\033[m'))
else:
    print('Parabéns, seu empréstimo foi {}concedido{}!'.format('\033[32;4m', '\033[m'))

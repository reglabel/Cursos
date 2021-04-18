from time import sleep
print(' @ '*10)
print('ANALISADOR DE TRIÂNGULO')
print(' @ '*10)
a = float(input('Primeiro segmaento: ').strip())
b = float(input('Segundo segmento: ').strip())
c = float(input('Terceiro segmento: ').strip())
s = a + b
d = a - b
abs(d)
print('ANALISANDO...')
sleep(3)
if s > c > d:
    print('Esses segmentos podem formar um triângulo.')
else:
    print('Esses segmentos não podem formar um triângulo.')

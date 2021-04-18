from datetime import date
from time import sleep
n = int(input('Diga um ano. Diga "14" para ver o ano atual. ').strip())
print('ANALISANDO...')
sleep(3)
if n == 14:
    n = date.today().year
if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print('O ano {} é bissexto.'.format(n))
        else:
            print('O ano {} não é bissexto.'.format(n))
    else:
        print('O ano {} é bissexto.'.format(n))
else:
    print('O ano {} não é bissexto.'.format(n))

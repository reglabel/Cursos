# não tinha conseguido
from random import randint
from time import sleep
from operator import itemgetter
contador = 1
jogos = {'1º JOGADOR': randint(1, 6),
         '2º JOGADOR': randint(1, 6),
         '3º JOGADOR': randint(1, 6),
         '4º JOGADOR': randint(1, 6)}
for k, v in jogos.items():
    sleep(1)
    print(f"O {k} tirou o valor {v}.")
jogos = dict(sorted(jogos.items(), key=itemgetter(1), reverse=True))
print("\n", "-=" * 30, f"\n{'RESULTADO FINAL:':^60}")
for k in jogos.keys():
    sleep(1)
    print(f"O {k} ficou em {contador}º lugar.")
    contador += 1

"""dic = {'759147': 54, '186398060': 8, '199846203': 42, '191725321': 10, '158947719': 4}
for item in sorted(dic, key = dic.get):
    print (dic[item])"""

"""teste = {'eu': 10, 'voce': 8, 'nos': 9}
teste = sorted(teste.items(), key=lambda x: x[1], reverse=True)
print(teste)
# Out: [('eu', 10), ('nos', 9), ('voce', 8)]
"""
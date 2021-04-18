brasileirao = 'CORINTHIAS', 'PALMEIRAS', 'SANTOS', 'GRÊMIO',\
              'CRUZEIRO', 'FLAMENGO', 'VASCO', 'CHAPECOENSE',\
              'ATLÉTICO', 'BOTAFOGO', 'ATLÉTICO - PR', 'BAHIA', 'SÃO PAULO',\
              'FLUMINENSE', 'SPORT RECIFE', 'EC VITÓRIA', 'CORITIBA', 'AVAÍ', \
              'PONTE PRETA', 'ATLÉTICO - GO'
print("-="*150)
print(f"A classificação da Brasileirão é a seguinte: {brasileirao}")
print("-="*150)
print(f"Os cinco primeiros colocados são: {brasileirao[:5]}")
print("-="*150)
print(f"Os últimos 4 colocados são: {brasileirao[-4:]}")
print("-="*150)
print(f"Em ordem alfabética, os times são: {sorted(brasileirao)}")
print("-="*150)
print(f"O chapecoense está na {brasileirao.index('CHAPECOENSE') + 1}º posição.")
print("-="*150)

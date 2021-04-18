import requests
try:
    r = requests.get('http://pudim.com.br/')
except:
    print("\033[31mMEU, Não consegui acessar o site pudim! :(\033[m")
else:
    print("\033[35mMEU, Consegui acessar o site pudim com sucesso! :D\033[m")
finally:
    print("MEU, Obrigada e até uma próxima!")

# O do professor:
#import urllib
#import urllib.request
#try:
#    site = urllib.request.urlopen('http://pudim.com.br/')
#except urllib.error.URLError:
#    print("\033[31mNOSSA, Não consegui acessar o site pudim! :(\033[m")
#else:
#    print("\033[35mNOSSA, Consegui acessar o site pudim com sucesso! :D\033[m")
#finally:
#    print("NOSSA, Obrigada e até uma próxima!")
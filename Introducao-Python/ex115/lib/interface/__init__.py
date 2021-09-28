from time import sleep


def leia_int(msg=''):
    while True:
        try:
            valor = int(input(msg))
        except KeyboardInterrupt:
            print(f"\033[31mO usuário preferiu não digitar esse número.\033[m")
            return 0
        except (ValueError, TypeError):
            print(f"\033[31mERRO!Digite um número inteiro válido\033[m")
            continue
        else:
            return valor


def linha(tam=40, elemento='-'):
    return elemento * tam


def cabecalho(txt, elemento='-', cor_do_meio='roxo', tam=-1):
    ajustar = 1
    if tam == -1:
        tam = len(txt) * 2
    if len(elemento) != 1:
        ajustar = len(elemento)
    if tam % 2 != 0:
        tam += 1
    while tam % ajustar != 0:
        tam += 1
    print(linha(int(tam/ajustar), elemento))
    print(cores(cor_do_meio), f"{txt:^{tam}}", cores('limpa'))
    print(linha(int(tam/ajustar), elemento))


def cores(nome_da_cor):
    palheta = {'amarelo': '\033[33m',
               'azul': '\033[34m',
               'branco': '\033[30;7m',
               'cinza': '\033[37m',
               'roxo': '\033[35m',
               'verde': '\033[32m',
               'vermelho': '\033[31m',
               'limpa': '\033[m'}
    return palheta[nome_da_cor]


def menu_automatico(*alternativas):
    numero_de_alternativas = maior_item = 0
    for i in alternativas:
        numero_de_alternativas += 1
        if numero_de_alternativas == 1:
            maior_item = len(i)
        elif len(i) > maior_item:
            maior_item = len(i)
    if maior_item % 2 != 0:
        maior_item += 1
    maior_item *= 2
    sleep(2)
    print('')
    cabecalho('MENU PRINCIPAL', '-=', 'verde', maior_item)
    for pos, i in enumerate(alternativas):
        print(f"{cores('amarelo')}{pos + 1} -{cores('azul')}{f' {i}':<{maior_item - 3}}{cores('limpa')}")
    print(linha(int(maior_item / 2), '-='))
    while True:
        opcao = leia_int(f"{cores('amarelo')}Sua opção: {cores('limpa')}")
        if opcao <= 0 or opcao > numero_de_alternativas:
            print(f"{cores('vermelho')}Essa opção é inválida! Tente novamente!{cores('limpa')}")
        else:
            print('')
            break
    return opcao

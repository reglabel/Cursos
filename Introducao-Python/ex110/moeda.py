def metade(valor=0.0, formatar=False):
    res = valor / 2
    if formatar:
        res = moeda(res)
    return res


def dobro(valor=0.0, formatar=False):
    res = valor * 2
    if formatar:
        res = moeda(res)
    return res


def aumentar(valor=0.0, taxa=0.0, formatar=False):
    res = ((taxa / 100.0) + 1.0) * valor
    if formatar:
        res = moeda(res)
    return res


def diminuir(valor=0.0, taxa=0.0, formatar=False):
    res = (1.0 - (taxa / 100.0)) * valor
    if formatar:
        res = moeda(res)
    return res


def moeda(valor=0.0, simbolo_moeda="R$"):
    valor_formatado = f"{simbolo_moeda}{valor:.2f}".replace('.', ',')
    return valor_formatado


def resumo(valor=0.0, acrescimo=10.0, decrescimo=5.0):
    lista = [['Preço analisado:', 'Dobro do preço:', 'Metade do preço:',
              f'{acrescimo}% de aumento:', f'{decrescimo}% de redução:'],
             [moeda(valor), dobro(valor, True), metade(valor, True),
              aumentar(valor, acrescimo, True), diminuir(valor, decrescimo, True)]]
    print("-="*25)
    print(f"{'RESUMO DO VALOR':^50}")
    print("-="*25)
    for i in range(0, 5):
        print(f"{lista[0][i]:<25}{lista[1][i]:>25}")
    print('-='*25)

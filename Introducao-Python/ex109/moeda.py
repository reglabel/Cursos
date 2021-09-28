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

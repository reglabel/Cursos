def metade(valor=0):
    res = valor / 2
    return res


def dobro(valor=0):
    res = valor * 2
    return res


def aumentar(valor=0, taxa=0):
    res = ((taxa / 100.0) + 1.0) * valor
    return res


def diminuir(valor=0, taxa=0):
    res = (1.0 - (taxa / 100.0)) * valor
    return res


def moeda(valor=0, simbolo_moeda="R$"):
    valor_formatado = f"{simbolo_moeda}{valor:.2f}".replace('.', ',')
    return valor_formatado

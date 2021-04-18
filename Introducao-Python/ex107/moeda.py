def metade(valor):
    res = valor / 2
    return res


def dobro(valor):
    res = valor * 2
    return res


def aumentar(valor, taxa):
    res = ((taxa / 100.0) + 1.0) * valor
    return res


def diminuir(valor, taxa):
    res = (1.0 - (taxa / 100.0)) * valor
    return res

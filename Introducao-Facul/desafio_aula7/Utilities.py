import os
from .Produto import Produto
from .BarraDeChocolate import BarraDeChocolate


def limpar():
    os.system('cls')


def transformar_numero_float(mensagem_pergunta, mensagem_erro="Opção INVÁLIDA! Digite um número."):
    while True:
        try:
            valor = float(input(mensagem_pergunta))
            break
        except ValueError:
            print(mensagem_erro)
    return valor


def transformar_numero_int(mensagem_pergunta, mensagem_erro="Opção INVÁLIDA! Digite um número."):
    while True:
        try:
            valor = int(input(mensagem_pergunta))
            break
        except ValueError:
            print(mensagem_erro)
    return valor


def convertar_lista_de_lista_de_definicoes_em_lista_de_produtos(lista):
    nova_lista = []

    for item in lista:
        if len(item) == 3:
            produto_da_vez = Produto(item[0], item[1], item[2])
            nova_lista.append(produto_da_vez)
        elif len(item) == 6:
            produto_da_vez = BarraDeChocolate(item[0], item[1], item[2], item[3], item[4], item[5])
            nova_lista.append(produto_da_vez)

    return nova_lista

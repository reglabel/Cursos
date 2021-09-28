class Produto:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = 0

    def aumentar_quantidade(self, quantidade_a_somar):
        if quantidade_a_somar > 0:
            self.quantidade += quantidade_a_somar
            return 1
        else:
            return -1

    def diminuir_quantidade(self, quantidade_a_subtrair):
        if 0 < quantidade_a_subtrair <= self.quantidade:
            self.quantidade -= quantidade_a_subtrair
            return 1
        else:
            return -1

    def consultar_quantidade(self):
        return f"QUANTIDADE DE: {self.nome}\n\t{self.quantidade} UNI"

    def ficha_de_produto(self):
        return f"\t\n-= FICHA PRODUTO =-\nNOME: {self.nome}\n" \
               f"DESCRIÇÃO: {self.descricao}\n" \
               f"PREÇO: {self.preco}\n" \
               f"QUANTIDADE: {self.quantidade}"

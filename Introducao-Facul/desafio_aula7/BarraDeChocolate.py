from .Produto import Produto


class BarraDeChocolate(Produto):
    def __init__(self, nome, descricao, preco, marca, tamanho, concentracao_cacau):
        super().__init__(nome, descricao, preco)
        self.marca = marca
        self.tamanho = tamanho
        self.concentracao_cacau = concentracao_cacau
        self.tipo = "Indefinido"

    def atualizar_tipo(self):
        if self.concentracao_cacau >= 70:
            self.tipo = "Chocolate Amargo"
        elif 70 > self.concentracao_cacau >= 50:
            self.tipo = "Chocolate Meio Amargo"
        elif 46 >= self.concentracao_cacau >= 36:
            self.tipo = "Chocolate Ao Leite"

    def corrigir_concentracao_cacau(self, nova_concentracau_cacau):
        self.concentracao_cacau = nova_concentracau_cacau

    def consultar_concentracao_cacau(self):
        return self.concentracao_cacau

    def ficha_de_produto(self):
        return f"{super().ficha_de_produto()}\nMARCA: {self.marca}\nTAMANHO: {self.tamanho}\nCONCENTRAÇÃO CACAU:{self.concentracao_cacau}"

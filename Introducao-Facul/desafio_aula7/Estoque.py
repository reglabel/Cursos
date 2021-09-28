from desafio_aula7 import p
from .Utilities import convertar_lista_de_lista_de_definicoes_em_lista_de_produtos


class Estoque:
    def __init__(self, codigo_estoque):
        self.lista_produtos = convertar_lista_de_lista_de_definicoes_em_lista_de_produtos(p)
        self.codigo_estoque = codigo_estoque

    def listar_estoque(self, imprimir_produtos=True, procurar_produto=False, nome_produto_procurado=None,
                       receber_indice=True):
        if imprimir_produtos:
            print(f"\n\t\t-= LISTANDO ESTOQUE {self.codigo_estoque}=-")
        cont = 0
        for produto in self.lista_produtos:
            if imprimir_produtos:
                print(produto.ficha_de_produto())
            if procurar_produto:
                if not (nome_produto_procurado is None):
                    if produto.nome == nome_produto_procurado:
                        if receber_indice:
                            return cont
                        else:
                            return produto
                    else:
                        cont += 1
        if receber_indice:
            cont = -1
            return cont
        else:
            return None

    def remover_produto(self, nome_produto_a_excluir):
        indice_produto_a_excluir = self.listar_estoque(False, True, nome_produto_a_excluir)
        if indice_produto_a_excluir == -1:
            return f"Produto {nome_produto_a_excluir} não encontrado no estoque!"
        else:
            del (self.lista_produtos[indice_produto_a_excluir])
            return f"Produto Excluído Com Sucesso"

    def adicionar_produto(self, produto):
        self.lista_produtos.append(produto)

from desafio_aula7 import *

estoque = Estoque(100)

while True:
    print("\n\t-- ESTOQUE DE MERCADO --")
    print("\t\t---- MENU ----")
    print("1 - Cadastrar Perfil Produto")
    print("2 - Remover Perfil Cadastrado de Produto")
    print("3 - Registrar Recebimento de Produto")
    print("4 - Registrar Saída de Produto")
    print("5 - Listar Estoque")
    print("6 - Sair")

    opcao = transformar_numero_int("\nDIGITE SUA OPÇÃO: ")

    if opcao == 1:
        nome_produto = input("\nDIGITE O NOME DO PRODUTO: ").strip().upper()
        descricao_produto = input("DIGITE A DESCRIÇÃO DO PRODUTO: ").strip().upper()
        preco_produto = transformar_numero_float("DIGITE A PREÇO DE ENTRADA DO PRODUTO: ")
        produto = Produto(nome_produto, descricao_produto, preco_produto)
        estoque.adicionar_produto(produto)
        print("\nProduto Adicionado Com Sucesso")

    elif opcao == 2:
        estoque.listar_estoque()
        nome_produto = input("\nDIGITE O NOME DO PRODUTO QUE DESEJA REMOVER: ").strip().upper()
        print(estoque.remover_produto(nome_produto))

    elif opcao == 3:
        estoque.listar_estoque()
        nome_produto = input("\nDIGITE O NOME DO PRODUTO QUE RECEBERÁ NOVAS UNIDADES: ").strip().upper()
        quantidade_a_adicionar = transformar_numero_int(f"DIGITE A QUANTIDADE DE UNIDADES DE A ADICIONAR: ")
        produto = estoque.listar_estoque(False, True, nome_produto, False)
        if produto is None:
            print("\nProduto Não Encontrado no Estoque")
        else:
            result = produto.aumentar_quantidade(quantidade_a_adicionar)
            if result == 1:
                print("\nQuantidades Adicionadas Com Sucesso")
            else:
                print("\nValor Inválido Para Adição")

    elif opcao == 4:
        estoque.listar_estoque()
        nome_produto = input("\nDIGITE O NOME DO PRODUTO QUE PERDERÁ UNIDADES: ").strip().upper()
        quantidade_a_remover = transformar_numero_int(f"DIGITE A QUANTIDADE DE UNIDADES A REMOVER: ")
        produto = estoque.listar_estoque(False, True, nome_produto, False)
        if produto is None:
            print("\nProduto Não Encontrado no Estoque")
        else:
            result = produto.diminuir_quantidade(quantidade_a_remover)
            if result == 1:
                print("\nQuantidades Removidas Com Sucesso")
            else:
                print("\nValor Inválido Para Remoção")

    elif opcao == 5:
        estoque.listar_estoque()

    elif opcao == 6:
        limpar()
        print("\n\t\t-=-= ATÉ A PRÓXIMA =-=-")
        break

    else:
        print("\nOpção INVÁLIDA! Digite uma opção existente.")

    input("\nAperte 'ENTER' para continuar...")
    limpar()

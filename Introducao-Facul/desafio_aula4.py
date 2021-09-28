import os


def limpar():
    os.system('cls')


def transformar_numero(mensagem_pergunta, mensagem_erro="Opção INVÁLIDA! Digite um número."):
    while True:
        try:
            valor = int(input(mensagem_pergunta))
            break
        except ValueError:
            print(mensagem_erro)
    return valor


def percorrer_lista_com_dicionario(lista, deseja_imprimir=True, buscar_algo=False, item_buscado=""):
    achou = False
    cont = 0
    for i in lista:
        if deseja_imprimir:
            print(f"\n\tNOME: {i['nome']}\n\tQUANTIDADE: {i['quantidade']}\n\tDESCRIÇÃO: {i['descricao']}")
        elif buscar_algo:
            if item_buscado == i['nome']:
                # print(f"peguei o item {i['nome']} com o valor {cont}")
                achou = True
                break
            else:
                cont += 1
        else:
            print(i)
    if buscar_algo:
        return [achou, cont]


bd = []
while True:
    print("\n\t-- ESTOQUE DE MERCADO --")
    print("\t\t---- MENU ----")
    print("1 - Cadastrar Perfil Produto")
    print("2 - Remover Perfil Cadastrado de Produto")
    print("3 - Registrar Recebimento de Produto")
    print("4 - Registrar Saída de Produto")
    print("5 - Listar Estoque")
    print("6 - Sair")

    opcao = transformar_numero("\nDIGITE SUA OPÇÃO: ")

    if opcao == 1:
        limpar()
        # print("bd antes:")
        # print(bd)
        nome_produto = input("DIGITE O NOME DO PRODUTO: ").strip().upper()
        descricao_produto = input("DIGITE A DESCRIÇÃO DO PRODUTO: ").strip().upper()
        quantidade_produto = transformar_numero("DIGITE A QUANTIDADE DE ENTRADA DO PRODUTO: ")
        produto_da_vez = {'nome': nome_produto,
                          'descricao': descricao_produto,
                          'quantidade': quantidade_produto}
        bd.append(produto_da_vez)
        print("\nProduto Adicionado Com Sucesso")
        # print("bd depois:")
        # print(bd)

    elif opcao == 2:
        limpar()
        percorrer_lista_com_dicionario(bd)
        nome_produto = input("\nDIGITE O NOME DO PRODUTO QUE DESEJA REMOVER: ").strip().upper()
        analise = percorrer_lista_com_dicionario(bd, False, True, nome_produto)
        if analise[0]:
            # print("bd antes:")
            # print(bd)
            del(bd[analise[1]])
            # print("bd depois:")
            # print(bd)
            print("\nProduto Deletado Com Sucesso")
        else:
            print("\nProduto Não Encontrado no Estoque")

    elif opcao == 3:
        limpar()
        percorrer_lista_com_dicionario(bd, True)
        nome_produto = input("\nDIGITE O NOME DO PRODUTO QUE RECEBERÁ NOVAS UNIDADES: ").strip().upper()
        analise = percorrer_lista_com_dicionario(bd, False, True, nome_produto)
        if analise[0]:
            # print("bd antes:")
            # print(bd)
            quantidade_a_adicionar = transformar_numero(f"DIGITE A QUANTIDADE DE UNIDADES DE"
                                                        f" '{bd[analise[1]]['nome']}' A ADICIONAR: ")
            bd[analise[1]]['quantidade'] += quantidade_a_adicionar

            print("\nQuantidades Adicionadas Com Sucesso")
            # print("bd depois:")
            # print(bd)
        else:
            print("\nProduto Não Encontrado no Estoque")

    elif opcao == 4:
        limpar()
        percorrer_lista_com_dicionario(bd, True)
        nome_produto = input("\nDIGITE O NOME DO PRODUTO QUE PERDERÁ UNIDADES: ").strip().upper()
        analise = percorrer_lista_com_dicionario(bd, False, True, nome_produto)
        if analise[0]:
            # print("bd antes:")
            # print(bd)
            quantidade_a_retirar = transformar_numero(
                f"DIGITE A QUANTIDADE DE UNIDADES DE '{bd[analise[1]]['nome']}' A RETIRAR: ")
            bd[analise[1]]['quantidade'] -= quantidade_a_retirar

            print("\nQuantidades Retiradas Com Sucesso")
            # print("bd depois:")
            # print(bd)
        else:
            print("\nProduto Não Encontrado no Estoque")

    elif opcao == 5:
        limpar()
        print("\t\t---- ESTOQUE ----")
        percorrer_lista_com_dicionario(bd, True)

    elif opcao == 6:
        limpar()
        print("\t\t-=-= ATÉ A PRÓXIMA =-=-")
        break

    else:
        limpar()
        print("Opção INVÁLIDA! Digite uma opção existente.")

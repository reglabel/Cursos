from ex115.lib.arquivo import *
from ex115.lib.interface import *

arq = 'pessoasCadastradas.txt'
if arquivo_existe(arq):
    print(cores('roxo'), 'Arquivo encontrado com SUCESSO!', cores('limpa'))
else:
    print(cores('vermelho'), 'FALHA! Arquivo não encontrado!', cores('limpa'))
    criar_arquivo(arq)

while True:
    opcao = menu_automatico('Ver pessoas cadastradas', 'Adicionar nova pessoa', 'Sair do Sistema')
    if opcao == 1:
        ler_arquivo(arq)
    elif opcao == 2:
        cabecalho('NOVO CADASTRO', '-=', 'cinza', 48)
        nome = str(input('NOME: '))
        pontuacao = leia_int('PONTUAÇÃO: ')
        cadastrar(arq, nome, pontuacao)
    else:
        cabecalho('SAIR DO SISTEMA', '-=', 'vermelho', 48)
        print(cores('roxo'), "\tMuito obrigada por sua atenção!\n\tTenha um bom dia! :D", cores('limpa'))
        break

from ex115.lib.interface import *


def arquivo_existe(nome):
    try:
        teste = open(nome, 'rt')
        teste.close()
    except (FileNotFoundError, FileExistsError):
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        teste = open(nome, 'wt+')
        teste.close()
    except Exception as erro:
        print(cores('vermelho'), 'SOCORRO! Houve um ERRO na criação do arquivo!', cores('limpa'))
        print(f"A danada da causa foi {erro.__cause__}")
    else:
        print(cores('roxo'), f'EBA! Arquivo {nome} criado com SUCESSO!', cores('limpa'))


def ler_arquivo(nome):
    try:
        teste = open(nome, 'rt')
    except Exception as erro:
        print(cores('vermelho'), 'ERRO ao ler o arquivo!', cores('limpa'))
        print(f'A causa foi {erro.__cause__}.')
    else:
        cabecalho('PESSOAS CADASTRADAS', '-=', 'roxo', 48)
        for item in teste:
            dado = item.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'  {dado[0]:<31}{dado[1]:>5} PONTOS')
        teste.close()


def cadastrar(arq, nome='desconhecido', pontuacao=0):
    try:
        teste = open(arq, 'at')
    except Exception as erro:
        print(cores('vermelho'), 'ERRO na abertura do arquivo!', cores('limpa'))
        print(f'A causa foi {erro.__cause__}.')
    else:
        try:
            teste.write(f'{nome};{pontuacao}\n')
        except Exception as erro:
            print(cores('vermelho'), 'ERRO na escrita dos dados!', cores('limpa'))
            print(f'A causa foi {erro.__cause__}.')
        else:
            print(cores('roxo'), f'Registro de {nome} adicionado com SUCESSO!', cores('limpa'))
            teste.close()

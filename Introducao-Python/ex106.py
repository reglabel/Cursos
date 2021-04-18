cores = {"limpa": "\033[m", "cinza_e_azul": "\033[30;46m", "roxo_e_cinza": "\033[35;40m", "azul_e_verde": "\033[34;42m", "vermelho_e_branco": "\033[31;47m"}

def titulo(msg, cor=''):
	tamanho = len(msg) + 4
	print(cores[f'{cor}'])
	print("~" * tamanho)
	print(f"  {msg}  ")
	print("~" * tamanho)
	print(cores['limpa'])

def pyhelp():
	from time import sleep
	while True:
		sleep(0.2)
		titulo("SISTEMA DE AJUDA PyHelp", "cinza_e_azul")
		comando = input("Função ou biblioteca > ")
		if comando.upper() == 'FIM':
			titulo("ATÉ LOGO!", "roxo_e_cinza")
			break
		titulo(f"Acessando manul do comando '{comando}'", "azul_e_verde") 
		sleep(0.5)
		print(cores['vermelho_e_branco']) 
		help(comando)
		print(cores['limpa'])

pyhelp()


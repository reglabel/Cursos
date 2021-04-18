def leia_int(msg=''):
	"""-> Função que requisita um número e verifica se ele é inteiro, podendo utilizar-se de uma mensagem para isso.
	:param msg: valor opcional, mensagem pela qual o programa requisitara inserção de um número.
	:return: valor fornecido, se realmente for inteiro."""
	valor = input(msg)	
	while True:
		analise = valor.isnumeric()
		if analise:
			break
		else:
			valor = input(f"\033[31mERRO!Digite um número inteiro válido\033[m\n{msg}")
	return valor

n = leia_int("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")

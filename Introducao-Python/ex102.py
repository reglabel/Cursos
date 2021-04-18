def fatorial(numero,show=False):
	"""-> Função para calcular o fatorial de um número.
	Observação: números negativos serão convertidos para positivos. 
	:param numero: O número a ser calculado.
	:param show: (opcional) Mostrar ou não o processo de cálculo.
	:return: O valor do fatorial do número fornecido."""
	if numero < 0:
		numero *= -1
	resultado = 1
	for i in range(numero, 0, -1):
		resultado *= i
		if show:
			print(f"{i} x " if i > 1 else f"{i} = ", end="")
	return resultado	


print(fatorial(0, True))

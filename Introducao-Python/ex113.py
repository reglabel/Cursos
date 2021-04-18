def leiaInt(msg=''):
	while True:
		try:
			valor = int(input(msg))
		except KeyboardInterrupt:
			print(f"\033[31mO usuário preferiu não digitar esse número.\033[m")
			return 0
		except (ValueError, TypeError):
			print(f"\033[31mERRO!Digite um número inteiro válido\033[m")
			continue
		else:
			return valor


def leiaFloat(msg=''):
	while True:
		try:
			valor = float(input(msg))
		except KeyboardInterrupt:
			print(f"\033[31mO usuário preferiu não digitar esse número.\033[m")
			return 0
		except (ValueError, TypeError):
			print(f"\033[31mERRO!Digite um número inteiro válido\033[m")
			continue
		else:
			return valor

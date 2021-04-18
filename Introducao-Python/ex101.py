def voto(nascimento):
	"""-> Determina a obrigatoriedade (acima de 18 anos ou abaixo de 65), a opcionalidade (entre 16 e 18 anos ou a partir de 65) ou o impedimento de votar(menos de 16 anos), de acordo com a idade do indivíduo, calculada pelo anos de nascimento fornecido.

	:param nascimento: O ano de nascimento da pessoa.
	:return: Lista com a idade da pessoa e valor literal determinando sua condição em relação ao voto."""
	from datetime import date
	idade = date.today().year - nascimento
	if idade < 16:
		return [idade, "NÂO VOTA"]
	elif idade < 18 or idade >= 65:
		return [idade, "VOTO OPCIONAL"]
	else:
		return [idade, "VOTO OBRIGATÓRIO"]

ano = int(input("Em que ano você nasceu? ").strip())
print(f"Com {voto(ano)[0]} anos: {voto(ano)[1]}.")
print(voto(2010))
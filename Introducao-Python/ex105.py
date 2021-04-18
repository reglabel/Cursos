def notas(*valores, sit=False):
	"""-> Função para analisar notas e situações de vários alunos.
	:param valores: uma ou mais notas dos alunos (aceita várias).
	:param sit: valor opcional, indica se deve ou não adicionar situação da turma.
	:return: dicionario com várias informações sobre a turma."""
	relatorio = {'total': len(valores), 'maior': max(valores), 'menor': min(valores), 'media': sum(valores) / len(valores)}
	if sit:
		if relatorio['media'] < 5:
			relatorio['situacao'] = 'RUIM'
		elif relatorio['media'] < 7:
			relatorio['situacao'] = 'RAZOÁVEL'
		else:
			relatorio['situacao'] = 'BOA'
	return relatorio

resp = notas(5.5, sit=True)
print(resp)
help(notas)
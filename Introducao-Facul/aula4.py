# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LISTA - TEORIA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from statistics import mean

lista_vazia = []
lista_com_valores = [1, 2, 3]
print(lista_com_valores)
print(lista_com_valores[0])

# como editar algum valor da lista
lista_com_valores[0] = 4
print(lista_com_valores)

# como adicionar algum valor da lista
lista_com_valores.append(5)
lista_com_valores.insert(0, 10)
print(lista_com_valores)

# como excluir da lista
del (lista_com_valores[0])
print(lista_com_valores)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PRÁTICA 1 - LISTA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Criar lista vazia
lista = []
print(lista)

# Inserir 3 notas separadamente (9.5, 8.7, 5.5)
lista.append(9.5)
lista.append(8.7)
lista.append(5.5)

# Imprimir a lista
print(lista)

# Remover a segunda nota
del (lista[1])

# Adicionar uma nota 8.8 na posição 1 e adicionar a nota 9.7 no final
lista.insert(1, 8.8)
lista.append(9.7)

# Editar a última nota, trocar por 10
lista[(len(lista) - 1)] = 10

# Imprimir novamente
print(lista)

# Desafio = imprimir média
# Solução 1 - somar manualmente
soma1 = lista[0] + lista[1] + lista[2] + lista[3]
media1 = soma1 / len(lista)
# Solução 2 - laço de repetição
soma2 = 0
for i in range(len(lista)):
    soma2 += lista[i]
media2 = soma2 / len(lista)
print(media2)
# Solução 3 - com sum
media3 = sum(lista) / len(lista)
# Solução 4
media4 = mean(lista)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TUPLA - TEORIA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

tupla_vazia = ()
tupla_com_valores = (123, 456, 10, "abc")
print(tupla_com_valores)
print(tupla_com_valores[0])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PRÁTICA 2 - TUPLA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Criar tupla1 vazia
tupla1 = ()

# Criar tupla2 com os valores 1, 2, 3
tupla2 = (1, 2, 3)

# Alterar o primeiro valor tupla2 bota 10 -> TUPLA É IMUTÁVEL
# Adicionar o valor 1 na tupla1 -> TUPLA É IMUTÁVEL
# Excluir o valor 3 da tupla2 -> TUPLA É IMUTÁVEL

# Tupla não suporta alteração, adição ou exclusão

# Imprimir as duas tuplas
print(tupla1)
print(tupla2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DICIONÁRIO - TEORIA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dicionario_vazio = {}
dicionario_com_valores = {'nome': "Arthur", 'idade': 123}
print(dicionario_com_valores)
print(dicionario_com_valores['nome'])

# editar
dicionario_com_valores['nome'] = "Fabbio Borges"
print(dicionario_com_valores)

# adicionar
dicionario_com_valores['altura'] = 1.74
print(dicionario_com_valores)

# excluir
del (dicionario_com_valores['altura'])
print(dicionario_com_valores)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PRÁTICA 3 - DICIONÁRIO
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dicionario = {}
aluno1 = {
    'nome': "Junior",
    'idade': 19
}
print(aluno1)
aluno1['altura'] = 1.74
print(aluno1)

bd = []
print(bd)
bd.append(aluno1)

# Desafio: Código que vai simular banco de dados.
# Adaptar esse código para um exemplo real.
# Ex: carrinho de compras com produto, preço e quantidade (dict).

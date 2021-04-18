a = float(input('Primeiro valor: ').strip())
b = float(input('Segundo valor: ').strip())
c = float(input('Terceiro valor: ').strip())
n = [a, b, c]
n.sort()
print('O menor valor é {:.1f} e o maior é {:.1f}'.format(n[0], n[2]))

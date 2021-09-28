import matplotlib.pyplot

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

matplotlib.pyplot.plot(meses, valores)

matplotlib.pyplot.show()

meses2 = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
x1 = [1, 2, 3, 4, 5, 6]
x2 = [3, 2, 4, 7, 9, 10]

matplotlib.pyplot.plot(meses, x1, 'g--', meses, x2, 'bs')

matplotlib.pyplot.show()

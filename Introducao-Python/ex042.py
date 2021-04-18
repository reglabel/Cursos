print('ANALISADOR DE TRIÂNGULO')

primeiro_lado = float(input('Primeiro segmaento: ').strip())
segundo_lado = float(input('Segundo segmento: ').strip())
terceiro_lado = float(input('Terceiro segmento: ').strip())

soma = primeiro_lado + segundo_lado
diferenca = primeiro_lado - segundo_lado
abs(diferenca)

if soma > terceiro_lado > diferenca:
    print('Esses segmentos podem formar um triângulo.')
    if primeiro_lado == segundo_lado and segundo_lado == terceiro_lado:
        print("Esse triângulo é equilátero.")
    elif primeiro_lado == terceiro_lado or primeiro_lado == segundo_lado or terceiro_lado == segundo_lado:
        print("Esse triângulo é isósceles.")
    else:
        print("Esse triângulo é escaleno.")
else:
    print('Esses segmentos não podem formar um triângulo.')

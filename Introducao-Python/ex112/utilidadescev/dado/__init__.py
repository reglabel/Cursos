def leiadinheiro(msg):
    analisar = str(input(msg)).replace(" ", "")
    while not analisar.isdigit():
        if '.' in analisar:
            if (analisar.replace('.', '')).isdigit():
                break
        elif ',' in analisar:
            if (analisar.replace(',', '')).isdigit():
                analisar = analisar.replace(',', '.')
                break
        print(f"\033[0;31mERRO! '{analisar}' não é um valor monetário válido.\033[m")
        analisar = input("Tente novamente: ").replace(" ", "")
    analisar = float(analisar)
    return analisar

while True:
    tabuada = int(input("Você quer ver a tabuada de qual número? ").strip())
    if tabuada >= 0:
        print("-="*20)
        print(f"Esta é a tabuada de {tabuada}: ")
        for i in range(1, 11):
            print(f"{tabuada} x {i} = {tabuada * i}")
        print("-="*20)
    else:
        print("Programa ENCERRADO...")
        break

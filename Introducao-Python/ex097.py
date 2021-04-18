def escreva(msg):
    tamanho = int(len(msg) + 6)
    print("~" * tamanho)
    print(f"{str(msg):^{tamanho}}")
    print("~" * tamanho)


escreva('Olá, Mundo!')
escreva("Now this looks like a job for me, so everybody, just follow me, cause we need...")
escreva('Aprenda Python, que é sucesso!')

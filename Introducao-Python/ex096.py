def area(primeira_medida, segunda_medida):
    total = primeira_medida * segunda_medida
    print(f"A área do seu terreno {primeira_medida:.2f}m x {segunda_medida:.2f}m"
          f" é de {total:.2f}m².")


print("-=" * 30, f"\n{'ANÁLISE DE TERRENO':^60}\n", "-=" * 30)
largura = float(input("Qual a largura do terreno (em metros)? ").strip())
comprimento = float(input("Qual o comprimento do terreno (em metros)? ").strip())
area(largura, comprimento)

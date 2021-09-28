class Carro:
    def __init__(self, nome, tipo, peso, cor):
        self.nome = nome
        self.tipo = tipo
        self.peso = peso
        self.cor = cor
        self.status = "desligado"

    def ligar_carro(self):
        self.status = "ligado"

    def desligar_carro(self):
        self.status = "deligado"


celta = Carro("Celta", "Sedã", 800, "Branco")
print(f"Carro: {celta.nome}, Cor: {celta.cor}, Tipo: {celta.tipo}, Peso: {celta.peso}")
print(celta.status)
celta.ligar_carro()
print(celta.status)

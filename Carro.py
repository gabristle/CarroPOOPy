class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def apresentarCarro(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}\n")
    
#usei de exemplo os carros de fórmula 1
carro1 = Carro("Mercedes", "W14", 2023)
carro2 = Carro("Red Bull", "RB18", 2022)
carro3 = Carro("McLaren", "MP4/6", 1991)

carro1.apresentarCarro()
carro2.apresentarCarro()
carro3.apresentarCarro()
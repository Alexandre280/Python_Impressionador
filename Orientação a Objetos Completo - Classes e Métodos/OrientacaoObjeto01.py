class TV:

    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

tv_sala = TV()
tv_quarto = TV()

print(tv_sala.cor)
print(tv_quarto.canal)

tv_sala.mudar_canal('Globo')
print(tv_sala.canal)

tv_quarto.mudar_canal('YouTube')
print(tv_quarto.canal)


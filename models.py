class Entrada:
    def __init__(self, minimo_aleatorio, maximo_aleatorio, quantidade_aleatorio, tamanho_combinacao):
        self.minimo_aleatorio = minimo_aleatorio
        self.maximo_aleatorio = maximo_aleatorio
        self.quantidade_aleatorio = quantidade_aleatorio
        self.tamanho_combinacao = tamanho_combinacao

class Saida:
    def __init__(self, combinacoes, total_combinacoes, numero_gerados):
        self.combinacoes = combinacoes
        self.total_combinacoes = total_combinacoes
        self.numero_gerados = numero_gerados

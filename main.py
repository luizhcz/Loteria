from flask import Flask, request, jsonify
import random
from itertools import combinations

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

def create_app():
    app = Flask(__name__)

    @app.route('/geraloteria', methods=['POST'])
    def gera_loteria():
        data = request.get_json()
        entrada = Entrada(**data)

        numeros_aleatorios = gerar_numeros_aleatorios(entrada.minimo_aleatorio, entrada.maximo_aleatorio, entrada.quantidade_aleatorio)
        combinacoes = gerar_combinacoes(numeros_aleatorios, entrada.tamanho_combinacao)

        saida = Saida(
            combinacoes=list(map(list, combinacoes)),
            total_combinacoes=len(combinacoes),
            numero_gerados=numeros_aleatorios
        )
        
        return jsonify(saida.__dict__)

    def gerar_numeros_aleatorios(minimo, maximo, quantidade):
        return [random.randint(minimo, maximo) for _ in range(quantidade)]

    def gerar_combinacoes(numeros, tamanho_comb):
        return list(combinations(numeros, tamanho_comb))

    return app
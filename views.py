from flask import request, jsonify
from models import Entrada, Saida
from services import gerar_numeros_aleatorios, gerar_combinacoes

def configure_routes(app):

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

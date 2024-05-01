import random
from itertools import combinations

def gerar_numeros_aleatorios(minimo, maximo, quantidade):
    return [random.randint(minimo, maximo) for _ in range(quantidade)]

def gerar_combinacoes(numeros, tamanho_comb):
    return list(combinations(numeros, tamanho_comb))

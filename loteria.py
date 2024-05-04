import random
import itertools

class Loteria:
    def gerar_numero_aleat(self, minimo, maximo, quantidade):
        return [random.randint(minimo, maximo) for _ in range(quantidade)]

    def gerar_combinacoes(self, numeros, tamanho_comb):
        return list(itertools.combinations(numeros, tamanho_comb))

# Exemplo de uso
loteria = Loteria()

# Gerar 5 números aleatórios entre 1 e 50
numeros_aleatorios = loteria.gerar_numero_aleat(1, 50, 5)
print("Números Aleatórios:", numeros_aleatorios)

# Gerar todas as combinações possíveis de 3 números a partir dos números gerados
combinacoes = loteria.gerar_combinacoes(numeros_aleatorios, 3)
print("Combinacoes possíveis:", list(combinacoes))

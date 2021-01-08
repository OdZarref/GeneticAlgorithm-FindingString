from fuzzywuzzy import fuzz
from config import *
import random

inputPalavra = str(input('String: '))
inputFitness = int(input('Nível de Acurácia: '))
inputPalavraTamanho = len(inputPalavra)


class Membro:
    def __init__(self, inputPalavraTamanho):
        self.palavra = ''.join(random.choice(letras) for _ in range(inputPalavraTamanho))
        self.fitness = -1


def iniciarMembros():
    return [Membro(inputPalavraTamanho) for _ in range(20)]

def fitness(membros):
    for membro in membros:
        membro.fitness = fuzz.ratio(membro.palavra, inputPalavra)

    return membros

def selecao(membros):
    def mostrarIndividuos(membros):
        for membro in membros:
            print(f'String = {membro.palavra} | Fitness={membro.fitness}')

    membros = sorted(membros, key=lambda membro: membro.fitness, reverse=True)
    mostrarIndividuos(membros)
    membros = membros[:int(0.2 * len(membros))]

    return membros

def crossover(membros):
    descendencia = []

    for _ in range(int((populacao - len(membros)) / 2)):
        pai = random.choice(membros)
        mae = random.choice(membros)
        descendente1 = Membro(inputPalavraTamanho)
        descendente2 = Membro(inputPalavraTamanho)
        divisor = random.randint(0, inputPalavraTamanho)
        descendente1.palavra = pai.palavra[:divisor] + mae.palavra[divisor:]
        descendente2.palavra = mae.palavra[:divisor] + pai.palavra[divisor:]

        descendencia.append(descendente1)
        descendencia.append(descendente2)

    membros.extend(descendencia)

    return membros


def mutacao(membros):
    for membro in membros:
        for indice, _ in enumerate(membro.palavra):
            if random.uniform(0.0, 1.0) <= 0.1:
                membro.palavra = membro.palavra[:indice] + random.choice(letras) + membro.palavra[indice + 1:]

    return membros

def algoritmoGenetico():
    membros = iniciarMembros()

    for geracao in range(geracoes):
        print(f'Geração {geracao + 1}')
        membros = fitness(membros)
        membros = selecao(membros)
        membros = crossover(membros)
        membros = mutacao(membros)

        if any(membro.fitness >= inputFitness for membro in membros):
            print('Encontrado!')
            exit()

if __name__ == '__main__':
    algoritmoGenetico()

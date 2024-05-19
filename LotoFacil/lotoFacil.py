import pandas as pd
import numpy as np
import random
from collections import Counter

def ler_numeros_de_csv(arquivo_csv):
    df = pd.read_csv(arquivo_csv, delimiter=';')
    numeros_por_coluna = {coluna: df[coluna].tolist() for coluna in df.columns}
    return numeros_por_coluna

def analisar_numeros_por_tabela(numeros_por_coluna):
    contagem_total = Counter()
    for numeros in numeros_por_coluna.values():
        contagem_total.update(numeros)
    numero_mais_frequente = contagem_total.most_common(1)[0][0]
    return numero_mais_frequente

def gerar_numeros_baseados_em_analise(numero_mais_frequente):
    numeros_aleatorios = []
    while len(numeros_aleatorios) < 15:
        numero_aleatorio = random.choice(range(1, 26))
        if numero_aleatorio != numero_mais_frequente and numero_aleatorio not in numeros_aleatorios:
            numeros_aleatorios.append(numero_aleatorio)
    return numeros_aleatorios

if __name__ == "__main__":
    nome_arquivo = "LotoFacil/lotoFacil_resultados.csv"
    numeros_por_coluna = ler_numeros_de_csv(nome_arquivo)

    while True:
        numero_mais_frequente = analisar_numeros_por_tabela(numeros_por_coluna)
        numeros_aleatorios = gerar_numeros_baseados_em_analise(numero_mais_frequente)
        numeros_aleatorios.sort()

        print("Números gerados:", numeros_aleatorios)

        continuar = input("Deseja gerar mais números? (S/N): ")
        if continuar.lower() != 's':
            break

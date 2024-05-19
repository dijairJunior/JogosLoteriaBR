import pandas as pd
import random
from collections import Counter

def ler_numeros_de_csv(nome_arquivo):
    # Lendo o arquivo CSV usando pandas
    df = pd.read_csv(nome_arquivo, delimiter=';')
    
    # Ignorando a coluna 'Concurso' e extraindo apenas os números
    numeros_por_coluna = {col: df[col].tolist() for col in df.columns if col != 'Concurso'}
    
    return numeros_por_coluna

def analisar_numeros_por_coluna(numeros_por_coluna):
    numeros_mais_frequentes_por_coluna = {}
    for coluna, numeros in numeros_por_coluna.items():
        contagem = Counter(numeros)
        numero_mais_frequente = contagem.most_common(1)[0][0]
        numeros_mais_frequentes_por_coluna[coluna] = numero_mais_frequente
    return numeros_mais_frequentes_por_coluna

def gerar_numeros_baseados_em_analise(numeros_mais_frequentes_por_coluna):
    numeros_aleatorios = []
    while len(numeros_aleatorios) < 5:
        numero_aleatorio = random.choice(range(1, 81))  # Alterado o range para 1 a 80
        if numero_aleatorio not in numeros_aleatorios:
            numeros_aleatorios.append(numero_aleatorio)
    return numeros_aleatorios

if __name__ == "__main__":
    # Ler os dados do arquivo CSV
    nome_arquivo = "Quina/quina_resultados.csv"
    numeros_por_coluna = ler_numeros_de_csv(nome_arquivo)

    while True:
        # Analisar os números mais frequentes em cada coluna individualmente
        numeros_mais_frequentes_por_coluna = analisar_numeros_por_coluna(numeros_por_coluna)

        # Gerar os números aleatórios com base nas análises das colunas do CSV
        numeros_aleatorios = gerar_numeros_baseados_em_analise(numeros_mais_frequentes_por_coluna)

        # Ordenar os números gerados em ordem crescente
        numeros_aleatorios.sort()

        # Mostrar os números gerados em uma única sequência
        print("Números gerados:", numeros_aleatorios)

        continuar = input("Deseja gerar mais números? (S/N): ")
        if continuar.lower() != 's':
            break

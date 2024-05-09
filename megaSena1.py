import csv
import random
from collections import Counter

def ler_numeros_de_csv(nome_arquivo):
    numeros_por_coluna = {}
    with open(nome_arquivo, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo, delimiter=';')  # Especificando o delimitador como ';'
        cabecalho = next(leitor_csv)  # Ignorando a primeira linha que contém o cabeçalho
        for linha in leitor_csv:
            for coluna, valor in zip(cabecalho, linha):  # Iterando sobre o cabeçalho e os valores da linha simultaneamente
                if coluna not in numeros_por_coluna:
                    numeros_por_coluna[coluna] = []
                numeros_por_coluna[coluna].extend(map(int, valor.split(';')))  # Dividindo por ponto e vírgula
    return numeros_por_coluna

def analisar_numeros_por_coluna(numeros_por_coluna):
    numeros_mais_frequentes = {}
    for coluna, numeros in numeros_por_coluna.items():
        contagem = Counter(numeros)
        numero_mais_frequente = contagem.most_common(1)[0][0]
        numeros_mais_frequentes[coluna] = numero_mais_frequente
    return numeros_mais_frequentes

def gerar_numeros_baseados_em_analise(numeros_mais_frequentes):
    numeros_aleatorios = []
    for coluna in ["A", "B", "C", "D", "E", "F"]:
        if coluna in numeros_mais_frequentes:
            numero_mais_frequente = numeros_mais_frequentes[coluna]
            # Garantir que o número gerado não seja igual a nenhum dos números gerados anteriormente
            while True:
                numero_aleatorio = random.choice(numeros_por_coluna[coluna])
                if numero_aleatorio != numero_mais_frequente and numero_aleatorio not in numeros_gerados_anteriores:
                    numeros_aleatorios.append(numero_aleatorio)
                    break
        else:
            print(f"A coluna {coluna} não foi encontrada nos dados analisados.")
    return numeros_aleatorios

if __name__ == "__main__":
    # Ler os dados do arquivo CSV
    nome_arquivo = "numeros.csv"
    numeros_por_coluna = ler_numeros_de_csv(nome_arquivo)

    numeros_gerados_anteriores = []

    while True:
        # Analisar os números mais frequentes em cada coluna
        numeros_mais_frequentes = analisar_numeros_por_coluna(numeros_por_coluna)

        # Gerar os números aleatórios com base nas análises das colunas do CSV
        numeros_gerados = gerar_numeros_baseados_em_analise(numeros_mais_frequentes)
        print("Os números gerados são:", numeros_gerados)

        continuar = input("Deseja gerar mais números? (S/N): ")
        if continuar.lower() != 's':
            break

import csv
import random
from collections import Counter

def ler_numeros_de_csv(numeros):
    numeros_por_coluna = {}
    with open(numeros, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo, delimiter=';')  # Alterando o delimitador para ;
        cabecalho = next(leitor_csv)  # Ignorando a primeira linha que contém o cabeçalho
        for indice, linha in enumerate(leitor_csv, start=0):  # Começando o índice da linha de 1
            numeros_da_linha = linha  # Obtendo os números a partir da primeira coluna
            for coluna, valor in zip(cabecalho, numeros_da_linha):  # Iterando sobre o cabeçalho e os valores da linha simultaneamente
                if coluna not in numeros_por_coluna:
                    numeros_por_coluna[coluna] = []
                numeros_por_coluna[coluna].append(int(valor))
    return numeros_por_coluna


def analisar_numeros_por_tabela(numeros_por_coluna):
    contagem_total = Counter()
    for numeros in numeros_por_coluna.values():
        contagem_total.update(numeros)
    numero_mais_frequente = contagem_total.most_common(1)[0][0]
    return numero_mais_frequente

def gerar_numeros_baseados_em_analise(numero_mais_frequente):
    numeros_aleatorios = []
    while len(numeros_aleatorios) < 15:  # Gerar 15 números
        numero_aleatorio = random.choice(range(1, 26))  # Gerar um número aleatório entre 1 e 25
        if numero_aleatorio != numero_mais_frequente and numero_aleatorio not in numeros_aleatorios:
            numeros_aleatorios.append(numero_aleatorio)
    return numeros_aleatorios

if __name__ == "__main__":
    # Ler os dados do arquivo CSV
    nome_arquivo = "lotoFacil.csv"
    numeros_por_coluna = ler_numeros_de_csv(nome_arquivo)

    while True:
        # Analisar o número mais frequente em toda a tabela
        numero_mais_frequente = analisar_numeros_por_tabela(numeros_por_coluna)

        # Gerar os números aleatórios com base no número mais frequente da tabela
        numeros_aleatorios = gerar_numeros_baseados_em_analise(numero_mais_frequente)

        # Ordenar os números gerados em ordem crescente
        numeros_aleatorios.sort()

        # Mostrar os números gerados em uma única sequência
        print("Números gerados:", numeros_aleatorios)

        continuar = input("Deseja gerar mais números? (S/N): ")
        if continuar.lower() != 's':
            break
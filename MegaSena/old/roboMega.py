import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def ler_numeros_de_csv(nome_arquivo):
    df = pd.read_csv(nome_arquivo, delimiter=';')
    return df

def preparar_dados(df):
    X = []
    y = []

    for _, linha in df.iterrows():
        linha = linha.dropna().astype(int).tolist()
        y.append(linha.pop())  # Remove o último elemento da linha e adiciona em y
        X.append(linha)  # O que sobra na linha vai para X

    return np.array(X), np.array(y)

def treinar_modelo(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    return modelo

def gerar_numeros_com_modelo(modelo, df):
    X, _ = preparar_dados(df)  # Prepara os dados apenas para obter as características
    numeros_aleatorios = modelo.predict(X)
    sequencia = numeros_aleatorios[:6]  # Pega apenas os 6 primeiros números previstos
    return sequencia

if __name__ == "__main__":
    # Ler os dados do arquivo CSV
    nome_arquivo = "MegaSena/numeros.csv"
    df = ler_numeros_de_csv(nome_arquivo)
    
    X, y = preparar_dados(df)
    modelo = treinar_modelo(X, y)

    while True:
        # Gerar os números aleatórios com base no modelo treinado
        numeros_gerados = gerar_numeros_com_modelo(modelo, df)

        # Ordenar os números gerados em ordem crescente
        numeros_gerados.sort()

        print("Os números da MEGA SENA são:", numeros_gerados)

        continuar = input("Deseja gerar mais números? (S/N): ")
        if continuar.lower() != 's':
            break
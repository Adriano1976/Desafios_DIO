"""
O desafio consiste em criar um algoritmo que receba um conjunto de matrizes de confusão e 
retorne o índice, acurácia e precisão da matriz que apresenta o melhor desempenho, com base 
no cálculo dessas métricas. As matrizes de confusão são fornecidas na entrada, onde cada 
linha representa os valores de Verdadeiros Positivos (VP), Falsos Positivos (FP), Falsos 
Negativos (FN) e Verdadeiros Negativos (VN), respectivamente.

A acurácia é calculada pela fórmula (VP + VN) / (VP + FP + FN + VN), enquanto a precisão é 
calculada pela fórmula VP / (VP + FP). O algoritmo deve avaliar todas as matrizes de confusão 
fornecidas, calcular a acurácia e precisão para cada uma delas, e retornar o índice 
(começando em 1), acurácia e precisão (arredondada para duas casas decimais) da matriz 
com o melhor desempenho.

A entrada consiste em um número n, representando a quantidade de matrizes de confusão, 
seguido pelos valores que compõem essas matrizes, separados por vírgulas. A saída deve 
conter o índice, acurácia e precisão da matriz de melhor desempenho, no formato especificado.
"""


# Função para calcular métricas de desempenho com base em uma matriz de confusão
def calculate_metrics(matrix):
    # Extrai os valores da matriz e converte para inteiros
    tp, fp, fn, tn = map(int, matrix)
    
    # Calcula a acurácia e precisão com base nos valores da matriz
    accuracy = (tp + tn) / (tp + fp + fn + tn)
    precision = tp / (tp + fp)
    
    return accuracy, precision

# Função para encontrar o melhor desempenho entre várias matrizes
def best_performance(matrices):
    best_index = 0
    best_accuracy = 0
    best_precision = 0
    
    # Itera sobre as matrizes e calcula as métricas para encontrar o melhor desempenho
    for index, matrix in enumerate(matrices):
        accuracy, precision = calculate_metrics(matrix)
        
        # Atualiza o melhor desempenho se a acurácia for maior ou se forem iguais, verifica a precisão
        if accuracy > best_accuracy or (accuracy == best_accuracy and precision > best_precision):
            best_index = index
            best_accuracy = accuracy
            best_precision = precision
    
    return best_index, best_accuracy, best_precision

# Entrada do número de matrizes
n = int(input())
matrices = []

# Coleta as matrizes fornecidas pelo usuário
for _ in range(n):
    matrix = input().split(',')
    matrices.append(matrix)

# Encontra o melhor desempenho entre as matrizes fornecidas
best_index, best_accuracy, best_precision = best_performance(matrices)

# Saída formatada com o índice do melhor desempenho
print(f"Índice: {best_index + 1}")

# Formatação dos valores decimais de saída para acurácia e precisão
formatted_accuracy = "{:.2g}".format(best_accuracy) if best_accuracy % 1 else "{:.1g}.0".format(best_accuracy) 
formatted_precision = "{:.2g}".format(best_precision) if best_precision % 1 else "{:.1g}.0".format(best_precision)

# Saída formatada das métricas de desempenho
print(f"Acurácia: {formatted_accuracy}")
print(f"Precisão: {formatted_precision}")

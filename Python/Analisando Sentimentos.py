"""
O texto descreve um algoritmo simulado que realiza análise de sentimentos em um comentário 
fornecido pelo usuário. O programa divide o comentário em palavras individuais e conta o 
número de palavras positivas, negativas e neutras com base em uma lista pré-definida de 
palavras-chave. Em seguida, determina se o sentimento predominante do comentário é positivo, 
negativo ou neutro, comparando as contagens de palavras positivas e negativas. O usuário 
insere um comentário como entrada, e o programa exibe o sentimento desse comentário 
(Positivo, Negativo ou Neutro) como saída.
"""


# Importa o módulo re, que é a biblioteca de expressões regulares do Python. 
import re

def analyze_sentiment():
    # Entrada do usuário
    comentario = input()

    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())
    
    # Lista de palavras positivas, negativas e neutras
    positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    neutras = ["mas", "deixou", "apesar", "embora"]

    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    count_neutro = sum(palavra in neutras for palavra in palavras)

    # Verifica se há mais palavras positivas do que negativas no comentário e se não há palavras neutras. 
    # Se essa condição for verdadeira, o comentário é considerado positivo.
    if count_positivo > count_negativo and count_neutro == 0:
        return "Positivo"
    # Verifica se há mais palavras negativas do que positivas no comentário e se não há palavras neutras. 
    # Se essa condição for verdadeira, o comentário é considerado negativo.
    elif count_negativo > count_positivo and count_neutro == 0:
        return "Negativo"
    # Caso contrário, se houver um número igual de palavras positivas e negativas ou se houver palavras 
    # neutras, o comentário é considerado neutro.
    else:
        return "Neutro"

# Saída esperada
sentimento = analyze_sentiment()
print("Sentimento:", sentimento)


"""
Explicação do código:
- O programa importa o módulo re para trabalhar com expressões regulares.
- A função analyze_sentiment() é definida para analisar o sentimento do comentário fornecido pelo usuário.
- O usuário é solicitado a inserir um comentário usando a função input().
- O comentário é dividido em palavras individuais usando a função re.findall() e convertido para minúsculas usando lower().
- São definidas listas de palavras positivas, negativas e neutras.
- A contagem de palavras positivas, negativas e neutras é realizada usando a função sum() e uma expressão geradora.
- O sentimento do comentário é determinado com base nas contagens de palavras:
- Se houver mais palavras positivas do que negativas e não houver palavras neutras, o sentimento é considerado positivo.
- Se houver mais palavras negativas do que positivas e não houver palavras neutras, o sentimento é considerado negativo.
- Caso contrário, se houver um número igual de palavras positivas e negativas ou se houver palavras neutras, o sentimento 
é considerado neutro.
- O sentimento determinado é retornado pela função analyze_sentiment().
- Fora da função, o sentimento é armazenado em uma variável e exibido usando print().
"""
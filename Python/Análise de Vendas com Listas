"""
Você está trabalhando em um projeto de Power BI onde precisa analisar 
dados de vendas mensais de uma empresa. Em Power BI, os dados são 
frequentemente representados em tabelas, e você precisa calcular 
alguns indicadores básicos. Sua tarefa é calcular o total de vendas 
e a média mensal de vendas que serão usados para gerar relatórios e 
gráficos no Power BI, além de criar uma lista em Python para calcular 
o total de vendas e a sua média mensal.
"""

def analise_vendas(vendas):
    # Calcule o total de vendas e realize a média mensal
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas) if vendas else 0
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # Converta a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split(',')))
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))

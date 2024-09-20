"""
Você está gerando um relatório de vendas em Power BI e deseja identificar 
quais produtos foram mais vendidos durante um dia específico. Os dados 
dos produtos vendidos são frequentemente armazenados em listas. Sua tarefa 
é usar uma lista em Python para contar a frequência de cada produto e 
determinar o produto mais vendido, que será usado para destacar produtos 
populares no relatório do Power BI.
"""


def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        # Encontre o produto com a maior contagem
        if count > max_count:
            max_count = count
            max_produto = produto
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # Converta a entrada em uma lista de strings, removendo espaços extras
    produtos = [produto.strip() for produto in entrada.split(',')]
    
    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))
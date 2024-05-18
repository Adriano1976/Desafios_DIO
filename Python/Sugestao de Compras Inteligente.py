"""
O texto descreve um desafio em que você deve criar um programa que simula o auxílio de 
vendas de um site de catálogos de cogumelos usando inteligência artificial. O programa 
deve permitir que o usuário informe o nome de um cogumelo desejado e, com base nessa 
informação, sugerir até dois cogumelos adicionais da lista fornecida, cujos valores 
sejam iguais ou menores que o do cogumelo selecionado pelo cliente. A lista de cogumelos 
e seus respectivos valores é fornecida e já está ordenada por prioridade. Como entrada, 
o usuário fornece o nome do cogumelo desejado. Como saída, o programa exibe uma lista 
com no máximo duas sugestões de cogumelos mais baratos que o cogumelo selecionado, 
considerando a ordem da lista fornecida. Se não houver sugestões disponíveis, ou seja, 
se o cogumelo escolhido for o mais barato, o programa exibe uma mensagem indicando 
que não há sugestões.
"""


# Dicionário com os tipos de cogumelos e seus respectivos valores
catalogo = {
    "Shitake": 10,
    "Portobello": 8,
    "Shimeji": 6,
    "Champignon": 12,
    "Funghi": 16,
    "Porcini": 16
}

# Função para sugerir cogumelos com preços mais baixos com base em um cogumelo desejado.
def sugerir_cogumelos(cogumelo_desejado):
    if cogumelo_desejado in catalogo:
        valor_desejado = catalogo[cogumelo_desejado]
        sugestoes = []
        
        # Procura por cogumelos mais baratos no catálogo
        for cogumelo, valor in catalogo.items():
            if valor <= valor_desejado and cogumelo != cogumelo_desejado:
                sugestoes.append((cogumelo, valor))
                if len(sugestoes) == 2:
                    break
        
        if not sugestoes:
            # Se não houver sugestões, exiba a mensagem indicada no enunciado
            print("Desculpe, não há sugestões disponíveis.")
        else:
            for sugestao, valor_sugestao in sugestoes:
                print(f"{sugestao} - Valor: {valor_sugestao}")
    else:
        # Se o cogumelo desejado não estiver no catálogo, exiba uma mensagem de erro indicada no enunciado
        print(f"Cogumelo não encontrado no catálogo.")

# Entrada do usuário
cogumelo_desejado = input("Digite o nome do cogumelo desejado: ")

# Chamada da função para sugerir cogumelos
sugerir_cogumelos(cogumelo_desejado)

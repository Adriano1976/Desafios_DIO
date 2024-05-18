"""
O desafio consiste em desenvolver um programa que permita ao usuário inserir 
informações sobre até três equipamentos a serem cadastrados em uma rede de uma 
empresa. O programa criará uma lista para armazenar esses equipamentos e, em 
seguida, utilizará um loop para solicitar ao usuário a entrada dos nomes dos 
equipamentos. Após a inserção dos três equipamentos, o programa exibirá a lista 
completa, com cada equipamento listado com um prefixo de marcação (-) para 
melhor organização visual.
"""


# Cria uma lista vazia para armazenar os equipamentos
itens = []

# Loop para solicitar ao usuário inserir até três equipamentos
for _ in range(3):
    # Solicita o item ao usuário e armazena na variável "item"
    item = input("Insira o equipamento: ")
    # Adiciona o item à lista "itens"
    itens.append(item)

# Exibe a lista de equipamentos
print("Lista de Equipamentos:")
for item in itens:
    # Loop que percorre cada item na lista "itens" e exibe com um prefixo (-) de marcação
    print(f"- {item}")
""" 
    O texto descreve uma missão onde você precisa criar um modelo de machine learning 
capaz de classificar frutas em um pomar mágico, com base em três características: 
peso, textura (suave ou áspera) e cor (vermelha, laranja ou amarela). Cada tipo 
de fruta (maçã, laranja, morango e banana) tem limites específicos para essas 
características. O código receberá como entrada o peso da fruta (em gramas), a 
textura ("smooth" ou "rough") e a cor ("red", "orange" ou "yellow"), e deverá 
produzir uma saída indicando a classificação da fruta de acordo com as 
características fornecidas.
"""

def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 130 and textura == "rough" and cor == "red":
        return "A fruta é uma maçã!"
    elif peso >= 120 and textura == "smooth" and cor == "orange":
        return "A fruta é uma laranja!"
    elif peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
    elif peso >= 150 and textura == "rough" and cor == "yellow":
        return "A fruta é uma banana!"
    else:
        return "Não foi possível classificar a fruta."

# Entrada do usuário
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()

# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

# Saída da previsão
print(resultado)
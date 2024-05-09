"""
    O texto descreve um desafio em um reino mágico, onde você precisa criar um modelo de machine learning 
para prever a afinidade elemental única de cada feiticeiro, podendo ser Fogo, Água, Terra ou Ar. 
A predição será baseada em cinco atributos mágicos: intensidade do feitiço, presença de componente 
raro, fase lunar, idade do feiticeiro e afinidade com animais mágicos. Cada elemento tem critérios 
específicos relacionados a esses atributos. O código receberá como entrada a intensidade do feitiço, 
se possui componente raro, a fase lunar, a idade do feiticeiro e se tem afinidade com animais mágicos. 
Com base nessas entradas, o modelo deve produzir uma saída indicando a afinidade elemental prevista 
para o feiticeiro.
"""

def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):
    # Convertendo a resposta do componente raro e afinidade com animais para booleanos
    componente_raro = componente_raro.lower() == "sim"
    afinidade_animais = afinidade_animais.lower() == "sim"

    # Lógica de decisão para prever a afinidade elemental
    if intensidade >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100:
        return "A afinidade elemental do feiticeiro é com o elemento Fogo!"
    elif intensidade >= 7 and componente_raro and fase_lunar == "cheia" and idade_feiticeiro <= 100 and afinidade_animais:
        return "A afinidade elemental do feiticeiro é com o elemento Terra!"
    elif intensidade >= 7 and componente_raro and fase_lunar == "cheia" and idade_feiticeiro <= 100:
        return "A afinidade elemental do feiticeiro é com o elemento Água!"
    else:
        return "A afinidade elemental do feiticeiro é com o elemento Ar!"

# Entrada do usuário
intensidade_feitico = int(input())
componente_raro_feitico = input()
fase_lunar_feitico = input()
idade_feiticeiro = int(input())
afinidade_animais_feiticeiro = input()

# Fazendo a previsão
resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)

# Saída da previsão
print(resultado)


"""
Explicando o código - No código a cima, está sendo definida a função **prever_afinidade_elemental**, 
que recebe cinco parâmetros: **intensidade**, **componente_raro**, **fase_lunar**, **idade_feiticeiro** 
e **afinidade_animais**. Essa função determina a afinidade elemental de um feiticeiro com base em uma 
série de condições. Primeiro, converte as respostas dos parâmetros **componente_raro** e **afinidade_animais** 
para booleanos. Em seguida, utilizando lógica condicional, verifica se a intensidade do feitiço é alta o 
suficiente, se a fase lunar está em um estado específico e se a idade do feiticeiro atende a determinados 
critérios. Com base nessas condições, retorna uma mensagem indicando a afinidade elemental prevista. 
Após a definição da função, o código solicita ao usuário que forneça informações sobre o feitiço 
realizado, como intensidade, componente raro utilizado, fase lunar, idade do feiticeiro e se possui 
afinidade com animais. Em seguida, chama a função **prever_afinidade_elemental** com os dados fornecidos 
e exibe o resultado da previsão.
"""
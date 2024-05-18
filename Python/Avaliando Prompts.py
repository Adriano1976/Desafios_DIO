"""
O texto descreve um algoritmo que avalia se um prompt fornecido pelo usuário está adequado 
com base na presença de determinadas palavras-chave relevantes. O programa solicita ao usuário 
que insira um prompt e verifica se ele contém palavras-chave como "inteligência artificial", 
"sistemas de recomendação online", "exemplo de conversação", "explique conceitos" e "dicas de 
tecnologia". Se o prompt incluir pelo menos uma dessas palavras-chave, o programa informa que 
o prompt está adequado. Caso contrário, ele indica que o prompt não está adequado e sugere ao 
usuário incluir palavras-chave relevantes. Como entrada, o usuário fornece um prompt, e como 
saída, o programa exibe feedback informando se o prompt é adequado ou não, com uma sugestão 
para incluir palavras-chave relevantes, se necessário.
"""


# Entrada do usuário
prompt_usuario = input()

# Função para avaliar se o prompt está adequado
def avaliar_prompt(prompt):
    # Verifica se o prompt contém palavras-chave relevantes
    palavras_chave = ["inteligência artificial", "sistemas de recomendação online", "exemplos de conversação", "explique conceitos", "dicas de tecnologia" ]
    
    # Verifica se pelo menos uma palavra-chave está presente no prompt
    if any(palavra_chave in prompt.lower() for palavra_chave in palavras_chave):
        return "O prompt está adequado."
    else:
        return "O prompt não está adequado. Inclua palavras-chave relevantes."

# Avaliar o prompt do usuário
feedback_usuario = avaliar_prompt(prompt_usuario)

# Exibir feedback
print(feedback_usuario)


"""
Explicação do código acima:

1 - O programa solicita ao usuário que insira um prompt usando a função input().
2 - A função avaliar_prompt(prompt) é definida para verificar se o prompt contém palavras-chave relevantes.
3 - São definidas as palavras-chave relevantes em uma lista chamada palavras_chave.
4 - A função verifica se pelo menos uma palavra-chave está presente no prompt fornecido 
pelo usuário, convertendo o prompt e as palavras-chave para minúsculas para garantir a correspondência.
5 - Se o prompt contiver pelo menos uma palavra-chave relevante, a função retorna "O prompt está adequado.".
Caso contrário, retorna "O prompt não está adequado. Inclua palavras-chave relevantes."
6 - O feedback sobre a adequação do prompt é armazenado na variável feedback_usuario.
7 - O feedback é exibido para o usuário usando print().
"""
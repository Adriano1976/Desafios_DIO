"""
O texto descreve um desafio em que você deve fornecer breves descrições de boas práticas de 
refatoração de código em três áreas específicas: identificação clara de funções, separação 
da entrada de dados e uso de nomes descritivos para variáveis e funções. Cada descrição deve 
indicar como o código pode ser melhorado nesses aspectos, simulando prompts de pesquisa para 
IAs Generativas. Como entrada, você deve fornecer uma string de texto que represente um bom 
prompt de pesquisa. O programa então processará sua entrada e fornecerá uma sugestão de 
melhoria de refatoração correspondente àquela área, caso a entrada seja válida. Se a entrada 
não corresponder a nenhuma das três áreas especificadas, o programa informará que a opção 
é inválida.
"""


def identificar_funcoes(texto):
    # Retorna uma mensagem sobre separar funções em unidades coesas e com responsabilidades únicas.
    return "Separe funções em unidades coesas e com responsabilidades únicas."

def entrada_de_dados(texto):
    # TODO: Retorne uma mensagem sobre validar e normalizar as entradas para evitar inconsistências.
    return "Valide e normalize as entradas para evitar inconsistências."

def nomenclatura_significativa(texto):
    # TODO: Retorne uma mensagem sobre usar nomes descritivos para variáveis e funções.
    return "Use nomes descritivos para variáveis e funções."

def processar_entrada(texto):
    # Dicionário mapeando textos para funções
    opcoes = {
        "Dica de boas práticas de refatoração de código, nas funções.": identificar_funcoes,
        "Dica de boas práticas de refatoração de código, nas entrada de dados.": entrada_de_dados,
        "Dica de boas práticas de refatoração de código, nomenclaturas.": nomenclatura_significativa
    }

    # Verifica se o texto está presente nas opções
    if texto in opcoes:
        # Chama a função correspondente ao texto e retorna o resultado
        return opcoes[texto](texto)
    else:
        # TODO: Retorne uma mensagem de opção inválida se o texto não estiver nas opções
        return "Opção inválida."

def desafio():
    # Solicita uma entrada do usuário
    entrada = input("Digite uma dica de refatoração: ")
    # Processa a entrada e obtém a saída
    saida = processar_entrada(entrada)
    # Exibe a saída
    print(saida)

desafio()
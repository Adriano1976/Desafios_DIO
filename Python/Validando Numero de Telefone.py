"""
O desafio consiste em desenvolver uma função que valide se um número de telefone fornecido pelo 
cliente está no formato correto, que é (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9, 
respeitando os espaços entre os números. A função receberá uma string representando o número de 
telefone como entrada e deverá retornar uma mensagem indicando se o número é válido ou inválido. 
Exemplos de casos de entrada e saída esperados serão fornecidos para testar a função.
"""


import re

def validate_numero_telefone(phone_number):
    # Define um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX
    pattern = r'^\(\d{2}\)\s\d{1}\d{4}-\d{4}$'
    
    # A função 're.match()' verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'
phone_number = input()

# Chama a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazena o resultado retornado na variável 'result'
result = validate_numero_telefone(phone_number)

# Imprime o resultado
print(result)

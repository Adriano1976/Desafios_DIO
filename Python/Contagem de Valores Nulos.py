"""
Em análise de dados, é crucial identificar valores ausentes (nulos), pois eles afetam 
a integridade e qualidade dos dados. Dada uma lista contendo valores numéricos positivos 
e valores `None`, deve-se contar quantos desses valores são `None`. A entrada é uma lista 
de valores, por exemplo, `1, None, 2, None, 3, None`. A saída é um número inteiro que 
indica quantos valores nulos (`None`) estão presentes na lista. Para isso, use a função 
`count` do Python para contar os elementos `None`. Por exemplo, para a entrada 
`1, 2, None, 5, 6`, a saída será `1`.
"""

# Receber a lista do usuário
entrada = input()

# Converter a string de entrada em uma lista de valores
lista = [int(x.strip()) if x.strip().isdigit() else None for x in entrada.split(',')]

# Contar quantos elementos são None usando a função count
contador_nulos = lista.count(None)

# Exibir o resultado
print(contador_nulos)

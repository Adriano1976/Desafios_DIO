"""
O texto aborda a remoção de valores duplicados em uma lista de números. 
A tarefa é transformar a lista original, que pode conter duplicatas, em 
uma nova lista contendo apenas valores únicos. Para isso, deve-se converter 
a lista em um conjunto para eliminar as duplicatas e depois reconvertê-la 
em uma lista. Exemplos fornecidos ilustram o processo:

- Entrada: 1, 2, 2, 3, 4, 4, 5
- Saída: [1, 2, 3, 4, 5]

O código deve realizar a conversão dos elementos para inteiros, criar um conjunto 
para remover duplicatas e, em seguida, converter o conjunto de volta para uma lista.
"""


# Recebe a lista do usuário
entrada = input()
# Converte a string de entrada em uma lista de números
lista = [int(x.strip()) for x in entrada.split(',')]

# Remove duplicatas utilizando um conjunto e depois converte de volta para uma lista
lista_unica = list(set(lista))

# É Exibido a nova lista sem valores duplicados
print(lista_unica)

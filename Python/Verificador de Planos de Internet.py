"""
Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude 
seus clientes a escolherem o plano de internet ideal com base no consumo mensal 
de dados. A empresa solicita ao usuário que insira seu consumo médio mensal em 
GB (float). Em seguida, uma função chamada `recomendar_plano` recebe o consumo 
como entrada e, por meio de estruturas condicionais, verifica e retorna o plano 
adequado de acordo com os seguintes critérios: Plano Essencial Fibra - 50Mbps 
recomendado para consumo de até 10 GB, Plano Prata Fibra - 100Mbps para consumo 
entre 10 GB e 20 GB, e Plano Premium Fibra - 300Mbps para consumo acima de 20 GB.
"""

def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
""" O texto descreve um desafio onde você foi contratado pela empresa DIO Robots para 
programar um robô capaz de classificar números em negativo, positivo ou zero. Para isso, 
você deve criar uma função de classificação que receba um número como parâmetro e 
retorne a mensagem "negativo!" ou "positivo!" de acordo com sua categoria. O programa 
deve ser executado continuamente, permitindo que o usuário insira vários números, 
encerrado quando o usuário digitar zero. Após cada entrada, o robô deve classificar 
e exibir a mensagem correspondente. Ao final, o programa deve exibir a quantidade 
de números positivos, negativos e zeros inseridos. """

# Função para classificar um número como positivo, negativo ou zero
def classificar_numero(numero):
    if numero > 0:
        return "positivo!"
    elif numero < 0:
        return "negativo!"

def main():
    positivos = 0
    negativos = 0
    
    while True:
        numero = int(input())
        
        if numero == 0:
            break  # Encerra o loop se o usuário digitar 0.
        
        classificacao = classificar_numero(numero)
        if classificacao == "positivo!":
            positivos += 1
        elif classificacao == "negativo!":
            negativos += 1
        
        # Imprime a classificação do número
        print(classificacao)
    
    # Imprime a quantidade de números positivos e negativos inseridos
    print(f"{positivos} números positivos, {negativos} números negativos")

if __name__ == "__main__":
    main()
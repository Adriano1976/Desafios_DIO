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
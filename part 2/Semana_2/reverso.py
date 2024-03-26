def main():
    # Solicita ao usuário que insira a quantidade de números a serem lidos
    n = int(input("Digite a quantidade de números a serem lidos: "))
    
    # Cria uma lista vazia para armazenar os números
    numeros = []
    # Loop para ler os números e armazená-los na lista
    for _ in range(n):
        numero = int(input("Digite um número inteiro: "))  # Lê um número inteiro do usuário
        numeros.append(numero)  # Adiciona o número à lista 'numeros'
    
    # Imprime os valores em ordem inversa
    print("Valores em ordem inversa:")
    for i in range(n - 1, -1, -1):  # Loop de trás para frente, começando do último elemento até o primeiro
        print(numeros[i])  # Imprime o número na posição 'i' da lista 'numeros'

if __name__ == "__main__":
    main()  # Chama a função principal

def minimo(lista):
    # Inicializa o valor mínimo com o primeiro elemento da lista
    min_valor = lista[0]
    
    # Percorre a lista para encontrar o valor mínimo
    for i in range(1, len(lista)):
        if lista[i] < min_valor:
            min_valor = lista[i]
    
    return min_valor

def main():
    # Lê o número inteiro positivo n
    n = int(input("Digite a quantidade de números a serem lidos: "))
    
    # Inicializa uma lista vazia para armazenar os números
    numeros = []
    
    # Lê os n valores inteiros e armazena-os na lista 'numeros'
    for _ in range(n):
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
    
    # Chama a função minimo para obter o valor mínimo da lista
    valor_minimo = minimo(numeros)
    
    # Imprime o valor mínimo
    print("O valor mínimo é:", valor_minimo)

if __name__ == "__main__":
    main()

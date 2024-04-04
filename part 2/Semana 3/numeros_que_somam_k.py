def contar_pares_com_soma_k(string_v, k):
    # Convertendo a string de números em uma lista de inteiros
    vetor = list(map(int, string_v.split()))

    # Dicionário para armazenar o número de ocorrências de cada elemento do vetor
    ocorrencias = {}

    # Contagem das ocorrências de cada elemento do vetor
    for num in vetor:
        if num in ocorrencias:
            ocorrencias[num] += 1
        else:
            ocorrencias[num] = 1

    # Inicializando o contador de pares
    contador_pares = 0

    # Iterando sobre os elementos do vetor
    for num in vetor:
        complemento = k - num
        # Se o complemento existe no vetor e não é o próprio número
        if complemento in ocorrencias and (complemento != num or ocorrencias[num] > 1):
            # Adicionando o número de pares possíveis
            contador_pares += ocorrencias[complemento]

    # Dividindo por 2, pois cada par foi contado duas vezes
    contador_pares //= 2

    return contador_pares

# Exemplo de uso
string_v = input("Digite a sequência de números separados por espaços: ")
k = int(input("Digite o valor de k: "))
print( contar_pares_com_soma_k(string_v, k))

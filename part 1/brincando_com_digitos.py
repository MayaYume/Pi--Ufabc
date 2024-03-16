# Função para calcular a soma dos dígitos e determinar a letra correspondente
def calcular_soma_e_letra(numero):
    if numero % 2 == 0:  # Se o número for par
        soma_digitos = (numero // 10) % 10 + numero % 10
    else:  # Se o número for ímpar
        soma_digitos = (numero // 10000) + (numero // 1000 % 10) + (numero // 100 % 10)

    letra_resultante = "A" if soma_digitos < 6 else ("B" if 6 <= soma_digitos < 12 else "C")
    
    return soma_digitos, letra_resultante

# Entrada de dados
numero = int(input())

# Calcular a soma dos dígitos e determinar a letra correspondente
soma_resultante, letra_resultante = calcular_soma_e_letra(numero)

# Saída formatada
print(soma_resultante)
print(letra_resultante)

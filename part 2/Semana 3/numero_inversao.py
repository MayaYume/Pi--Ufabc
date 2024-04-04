def contar_inversoes(n, valores):
    inversoes = 0
    for i in range(1, n):
        if valores[i] < valores[i - 1]:
            inversoes += 1
    return inversoes

# Lê o número de valores
n = int(input())

# Lê os valores
valores = [int(input()) for _ in range(n)]

# Calcula o número de inversões
num_inversoes = contar_inversoes(n, valores)

# Imprime o número de inversões seguido da sequência lida
print(num_inversoes)
for valor in valores:
    print(valor)

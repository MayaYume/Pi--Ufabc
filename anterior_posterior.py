# Definição da função que retorna os três números anteriores a partir de um número dado
def numeros_anteriores(numero):
    a = numero - 1
    b = numero - 2
    c = numero - 3
    return a, b, c

# Definição da função que retorna os três números posteriores a partir de um número dado
def numeros_posteriores(numero):
    a = numero + 1
    b = numero + 2
    c = numero + 3
    return a, b, c

# Leitura de um número inteiro fornecido pelo usuário
numero = int(input("Digite um número inteiro: "))

# Leitura da ação desejada pelo usuário ("Anteriores" ou "Posteriores")
acao = input("Digite a ação desejada (Anteriores ou Posteriores): ")

# Verificação da ação desejada e impressão dos números resultantes em ordem crescente
if acao == "Anteriores":
    a, b, c = numeros_anteriores(numero)
    print(c, b, a)
elif acao == "Posteriores":
    a, b, c = numeros_posteriores(numero)
    print(a, b, c)
else:
    print("Ação inválida. Digite 'Anteriores' ou 'Posteriores'.")



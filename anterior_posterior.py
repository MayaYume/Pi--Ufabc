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
numero = int(input())

# Leitura da ação desejada pelo usuário ("Anteriores" ou "Posteriores")
acao = input()

# Verificação da ação desejada e impressão dos números resultantes em ordem crescente
if acao == "Anteriores":
    a_ant, b_ant, c_ant = numeros_anteriores(numero)
    print(f"{c_ant}, {b_ant}, {a_ant}")
elif acao == "Posteriores":
    a_post, b_post, c_post = numeros_posteriores(numero)
    print(f"{a_post}, {b_post}, {c_post}")
else:
    print("Ação inválida. Digite 'Anteriores' ou 'Posteriores'.")

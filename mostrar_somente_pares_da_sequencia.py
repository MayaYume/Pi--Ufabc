# Definir a função imprimir_pares_ate_n que imprime todos os números pares até o valor n
def imprimir_pares_ate_n(n):
    i = 2  # Inicializar i com 2, pois queremos começar com o primeiro número par
    while i <= n:  # Continuar o loop enquanto i for menor ou igual a n
        print(i)   # Imprimir o número par atual
        i += 2    # Incrementar i em 2 para obter o próximo número par

# Solicitar a entrada do usuário para o valor de n
n = int(input())

# Chamar a função para imprimir os números pares até n
imprimir_pares_ate_n(n)

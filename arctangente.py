def arctan(x):
    soma = 0
    sinal = 1
    
    # Loop para calcular a série de Taylor para arco tangente
    for i in range(1, 201, 2):
        termo = sinal * (x**i) / i  # Cada termo da série de Taylor
        soma += termo
        sinal *= -1  # Alternar o sinal para cada termo ímpar
    return soma

# Solicita ao usuário para inserir um valor para x
x = float(input("Digite o valor de x: "))

# Chama a função arctan para calcular o arco tangente e imprime o resultado
resultado = arctan(x)
print(f'O arco tangente de {x} é aproximadamente {resultado:.3f}')

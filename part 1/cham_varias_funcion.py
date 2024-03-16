# Importa o módulo math para usar funções matemáticas.
import math

# Definição da função 'a' que recebe dois parâmetros, incrementa o primeiro em 1 e retorna o produto dos dois.
def a(x: int, y: int) -> int:
    x = x + 1
    return x * y

# Definição da função 'b' que recebe um parâmetro, chama a função 'a' e imprime valores.
def b(z: int) -> int:
    # Chama a função 'a' com os parâmetros 'z' e 'z', armazena o resultado em 'prod'.
    prod = a(z, z)
    # Imprime os valores de 'z' e 'prod'.
    print(z, prod)
    # Retorna o valor de 'prod'.
    return prod

# Definição da função 'c' que recebe três parâmetros, calcula uma soma e chama a função 'b' elevando o resultado ao quadrado.
def c(x: int, y: int, z: int) -> int:
    # Calcula a soma de 'x', 'y' e 'z'.
    total = x + y + z
    # Chama a função 'b' com o resultado da soma e eleva o resultado ao quadrado.
    quadr = b(total) ** 2
    # Retorna o valor resultante.
    return quadr

# Bloco de código principal
# Define duas variáveis 'x' e 'y'.
x = 1
y = x + 1

# Chama a função 'c' com os argumentos 'x', 'y + 3' e 'x + y', e imprime o resultado.
print(c(x, y + 3, x + y))

import math

def calcular_raizes(a, b, c):
    # Calcula o discriminante
    delta = b**2 - 4*a*c

    # Verifica as condições e imprime as raízes
    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A raiz é {raiz:.2f}")
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print(f"As raízes são {x1:.2f} e {x2:.2f}")

# Obtém os coeficientes da equação do usuário
a = float(input())
b = float(input())
c = float(input())

# Calcula e imprime as raízes
calcular_raizes(a, b, c)

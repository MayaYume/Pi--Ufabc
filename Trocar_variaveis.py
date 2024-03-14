# Importa o módulo math para usar funções matemáticas.
import math

# Definição da função 'troca' que recebe dois parâmetros e retorna uma tupla com os valores trocados.
def troca(x: int, y: int) -> (int, int):
    # Retorna uma tupla com os valores de 'y' e 'x', invertendo a ordem.
    return y, x

# Definição da função 'main'.
def main():
    # Solicita ao usuário inserir um valor e converte para inteiro.
    x = int(input("Digite um valor para x: "))
    y = int(input("Digite um valor para y: "))
    
    # Chama a função 'troca' passando 'x' e 'y', e atribui os valores de retorno de volta a 'x' e 'y'.
    x, y = troca(x, y)
    print(x, y)
# Chama a função 'main' para iniciar a execução do programa.
main()

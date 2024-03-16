def numero_maior(x, y, z, n):
    # Verifica se x é o maior número
    if(x>y and x>z and x>n):
        return x
    # Verifica se n é o maior número
    elif(n>x and n>z and n>y):
        return n
    # Verifica se y é o maior número
    elif(y>x and y>z and y>n):
        return y
    # Se nenhum dos casos acima for verdadeiro, z é o maior número
    else:
        return z

def main():
    # Solicita ao usuário que insira os quatro números
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    z = float(input("Digite o terceiro número: "))
    n = float(input("Digite o quarto número: "))

    # Chama a função numero_maior para encontrar o maior número
    maior = numero_maior(x, y, z, n)
    # Imprime o maior número encontrado
    print("O maior valor é", maior)

main()

main()




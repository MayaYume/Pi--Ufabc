def tabuleiro(dimensao):
    # Loop externo para iterar sobre as linhas do tabuleiro
    for i in range(dimensao):
        # Loop interno para iterar sobre as colunas do tabuleiro
        for j in range(dimensao):
            # Se a soma dos índices for par, a casa é branca, senão é preta
            if (i + j) % 2 == 0:
                print("o", end="")
            else:
                print("*", end="")
        # Muda a linha para a próxima linha do tabuleiro
        print()

def main():
    # Solicita ao usuário a dimensão do tabuleiro
    dimensao = int(input("Digite a dimensão do tabuleiro: "))
    
    # Garante que a dimensão seja maior ou igual a 1
    if dimensao < 1:
        print("A dimensão do tabuleiro deve ser maior ou igual a 1.")
    else:
        # Chama a função para imprimir o tabuleiro
        tabuleiro(dimensao)

# Chama a função principal
main()

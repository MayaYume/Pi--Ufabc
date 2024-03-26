def verifica_palindromo(palavra):
    # Converte a palavra para minúsculas para facilitar a comparação
    palavra = palavra.lower()
    # Remove os espaços em branco da palavra
    palavra = palavra.replace(" ", "")
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    # Verifica se a palavra original é igual à palavra invertida
    if palavra == palavra_invertida:
        return True
    else:
        return False

# Função para entrada e saída
def main():
    palavra = input()
    if verifica_palindromo(palavra):
        print("É palíndromo")
    else:
        print("Não é palíndromo")

if __name__ == "__main__":
    main()

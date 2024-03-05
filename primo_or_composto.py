# Define a função eh_primo que verifica se um número é primo
def eh_primo(n):
    # Verifica se o número é menor ou igual a 1, pois números menores que 2 não são primos
    if n <= 1:
        return False
    
    # Itera de 2 até a raiz quadrada de n + 1, pois não é necessário verificar além desse ponto
    for i in range(2, int(n**0.5) + 1):
        # Se n for divisível por algum número no intervalo, então não é primo
        if n % i == 0:
            return False
    
    # Se não encontrou nenhum divisor no intervalo, o número é primo
    return True

# Entrada do usuário: solicita um número inteiro positivo
n = int(input())
# Verifica se o número é primo ou composto usando a função eh_primo e imprime o resultado
if eh_primo(n):
    print("Primo")
else:
    print("Composto")

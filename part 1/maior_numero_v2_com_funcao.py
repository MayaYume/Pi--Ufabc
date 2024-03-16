# Definindo uma função para verificar qual numero é maior
def verificar_maior(n, numeros):
    maior = numeros[0]
    # Itera sobre a sequência de números
    for i in range(1, n):
        # Verifica se o número atual é menor ou igual ao anterior
        if numeros[i] > maior:
# Tomara o numero maior como resultado da variavel maior 
            maior =  numeros[i]
    
    return maior

#funcao principal 
def main():
    
# Solicita ao usuário o valor de n
   n = int(input())
   # Cria uma lista vazia para armazenar os números
   numeros = []
   
# Loop para solicitar os n números inteiros distintos
   for i in range(n):
    numero = int(input())  # Solicita o número ao usuário
    numeros.append(numero)  # Adiciona o número à lista de números
# Encontra o maior número na sequência usando a função encontrar_maior
   maior_numero = verificar_maior(n, numeros)

# Imprime o maior número encontrado
   print("Maior número na sequência:", maior_numero)
   
#chamando a funcao
main()

# Inicializa um dicionário vazio para armazenar a contagem de cada dígito
contagem = {}

# Solicita ao usuário que insira um número inteiro e o converte para um inteiro
numero = int(input())

# Loop para processar cada dígito do número
while numero > 0:
    # Obtém o último dígito do número
    algarismo = numero % 10
    
    # Verifica se o dígito já está presente no dicionário de contagem
    if algarismo in contagem:
        # Se o dígito já estiver presente, incrementa a contagem desse dígito no dicionário
        contagem[algarismo] += 1
    else:
        # Se o dígito não estiver presente, cria uma entrada para ele no dicionário com contagem igual a 1
        contagem[algarismo] = 1
    
    # Remove o último dígito do número
    numero = numero // 10

# Calcula a soma de todas as contagens dos dígitos
soma = sum(contagem.values())

# Imprime a soma total das contagens
print(f"{soma}")

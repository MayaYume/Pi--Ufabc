# Função para abreviar um nome completo
def abreviar_nome(nome_completo):
    # Dividir o nome completo em partes separadas
    partes_nome = nome_completo.split()
    abreviacao = ""
    # Iterar sobre cada parte do nome
    for parte in partes_nome:
        # Adicionar a primeira letra de cada parte seguida de um ponto à abreviação
        abreviacao += parte[0] + "."
    # Retornar a abreviação
    return abreviacao

# Ler o nome completo do teclado
nome_completo = input()
# Imprimir a abreviação
print(abreviar_nome(nome_completo))

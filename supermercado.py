total_compra = 0  # Inicializa o total da compra
total_volumes = 0  # Inicializa o total de volumes

# Loop para receber a quantidade e o preço unitário de cada item
while True:
    quantidade = int(input("Digite a quantidade comprada (ou 0 para finalizar): "))
    
    # Verifica se a quantidade é 0 para finalizar a compra
    if quantidade == 0:
        break
    
    preco_unitario = float(input("Digite o preço unitário: "))
    
    # Calcula o subtotal do item e adiciona ao total da compra
    subtotal = quantidade * preco_unitario
    total_compra += subtotal
    
    # Adiciona a quantidade comprada ao total de volumes
    total_volumes += quantidade

# Imprime o total da compra e a quantidade de volumes comprados
print(f"Total da compra: R${total_compra:.2f}")
print(f"Quantidade de volumes comprados: {total_volumes}")

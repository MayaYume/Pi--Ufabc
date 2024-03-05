total_compra = 0  # Inicializa o total da compra
total_volumes = 0  # Inicializa o total de volumes

# Inicializa a variável para receber a quantidade
quantidade = int(input())

# Loop para receber a quantidade e o preço unitário de cada item
while quantidade != 0:
    preco_unitario = float(input())

    # Calcula o subtotal do item e adiciona ao total da compra
    subtotal = quantidade * preco_unitario
    total_compra += subtotal

    # Adiciona a quantidade comprada ao total de volumes
    total_volumes += quantidade

    # Recebe a próxima quantidade para verificar se é zero e finalizar o loop
    quantidade = int(input())

if total_volumes == 1:
    print(f"Foi comprado {total_volumes} item, totalizando R${total_compra:.2f}")
elif total_volumes > 1:
    print(f"Foram comprados {total_volumes} itens, totalizando R${total_compra:.2f}")

total_compra = 0  # Inicializa o total da compra
total_volumes = 0  # Inicializa o total de volumes

# Loop para receber a quantidade e o preço unitário de cada item
while True:
    quantidade = int(input())
    
    # Verifica se a quantidade é 0 para finalizar a compra
    if quantidade == 0:
        break
    else:
    
       preco_unitario = float(input())
    
    # Calcula o subtotal do item e adiciona ao total da compra
       subtotal = quantidade * preco_unitario
       total_compra += subtotal
    
    # Adiciona a quantidade comprada ao total de volumes
       total_volumes += quantidade

if (total_volumes == 1):
        print(f"Foi comprado {total_volumes} item, totalizando R${total_compra:.2f}")
elif(total_volumes > 1): 
        print(f"Foram comprados {total_volumes} itens, totalizando R${total_compra:.2f}")

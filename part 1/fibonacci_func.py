import math

def calcular_fibonacci(i: int) -> int:
    r5 = math.sqrt(5)
    t1 = ((1 + r5) / 2) ** i
    t2 = ((1 - r5) / 2) ** i
    return math.floor((t1 - t2) / r5)

def main():
    while True:
        i = int(input("Digite o número (ou um valor negativo para sair): "))
        
        if i < 0:
            print("Saindo do programa.")
            break

        resultado = calcular_fibonacci(i)
        print(f"O resultado para {i} é: {resultado}")

# Chamando a função para repetir o cálculo
main()

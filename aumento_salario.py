def salario(salario_inicial, anos_trabalhados):
    # Calcula o reajuste baseado no salário inicial
    if salario_inicial <= 1500.00:
        reajuste = salario_inicial + (salario_inicial * 0.20)  # Aumento de 20% para salários abaixo de R$ 1500.00
    elif salario_inicial < 2000.00:
        reajuste = salario_inicial + (salario_inicial * 0.15)  # Aumento de 15% para salários entre R$ 1500.00 e R$ 2000.00
    elif salario_inicial < 6000.00:
        reajuste = salario_inicial + (salario_inicial * 0.10)  # Aumento de 10% para salários entre R$ 2000.00 e R$ 6000.00
    else:
        reajuste = salario_inicial  # Não há aumento para salários acima de R$ 6000.00

    # Adiciona o bônus baseado nos anos trabalhados
    if  anos_trabalhados < 1:
        reajuste+=0
        
    elif anos_trabalhados >= 1 and anos_trabalhados <= 3:
        reajuste += 100.00  # Bônus de R$ 100.00 para 1 a 3 anos de trabalho
    elif anos_trabalhados >= 4 and anos_trabalhados <= 6:
        reajuste += 200.00  # Bônus de R$ 200.00 para 4 a 6 anos de trabalho
    elif anos_trabalhados >= 7 and anos_trabalhados <= 10:
        reajuste += 300.00  # Bônus de R$ 300.00 para 7 a 10 anos de trabalho
    else:
        reajuste += 500.00  # Bônus de R$ 500.00 para mais de 10 anos de trabalho

    return reajuste

def main():
    # Solicita o salário inicial e anos trabalhados ao usuário
    salario_inicial = float(input())
    anos_trabalhados = int(input())

    # Chama a função salario() para calcular o novo salário
    novo_salario = salario(salario_inicial, anos_trabalhados)

    # Verifica se houve aumento e exibe o novo salário ou uma mensagem
    if novo_salario > salario_inicial:
        print(f"O novo salário é R${novo_salario:.2f}")
    else:
        print("Não houve aumento")

if __name__ == "__main__":
    main()

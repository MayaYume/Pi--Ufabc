def verifica_soma_subtacao(a: int, b: int, c:int) -> bool:
    #verificação de ser verdadeiro
    if(a + b == c or b+a ==c or a - b== c or b-a ==c):
        sinal = "Verdadeiro"
    else:
        sinal ="Falso"
    
    return sinal

def main():
    # Solicita o salário inicial e anos trabalhados ao usuário
    a = int(input())
    b = int(input())
    c = int(input())

    # Chama a função salario() para calcular o novo salário
    sinal = verifica_soma_subtacao(a, b, c)
    print(sinal)


if __name__ == "__main__":
    main()

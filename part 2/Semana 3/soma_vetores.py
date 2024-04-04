def soma_vetores (string_x, string_y):
    # Dividindo as strings em listas de nÃºmeros
    vetor_x = list(map(int, string_x.split()))
    vetor_y = list(map(int, string_y.split()))
    
    # Verificando se os vetores têm o mesmo tamanho 
    if len(vetor_x) != len (vetor_y):
        return "os vetores não têm o mesmo tamanho"
    
    #calculando a soma dos vetores 
    vetor_soma =[xi + yi for xi, yi in zip(vetor_x, vetor_y)]
    
    # Convertendo o vetor soma de volta para uma string
    resultado =' '.join(map(str, vetor_soma))
    return resultado

def main():
    #lendo a string de cada entrada
    x = input()
    y = input()
# Chamando a função e imprimindo o resultado
    print( soma_vetores(x, y))
    
#chamando o main
if __name__ == "__main__":
    main()

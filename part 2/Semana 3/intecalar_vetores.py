def intercalar_vetores (string_x: str, string_y: str)->[int]:
    # Dividindo as strings em listas de nÃºmeros
    vetor_x = list(map(int, string_x.split()))
    vetor_y = list(map(int, string_y.split()))
    
# Criando uma lista vazia para armazenar o vetor resultante    
    vetor_resultante = []    
    
    # Índices para percorrer os vetores x e y
    idx_x = 0
    idx_y = 0
# Percorrendo ambos os vetores enquanto houver elementos em ambos    resultado =''.join(map(str, vetor_soma))
    while idx_x < len(vetor_x) and idx_y < len(vetor_y):
        # Se o elemento atual de x for menor ou igual ao elemento atual de y
        # Adiciona o elemento de x ao vetor resultante e avança o índice de x
        if vetor_x[idx_x] <= vetor_y[idx_y]:
            vetor_resultante.append(vetor_x[idx_x])
            idx_x += 1

        # Caso contrário, adiciona o elemento de y ao vetor resultante e avança o índice de y
        else:
            vetor_resultante.append(vetor_y[idx_y])
            idx_y += 1

  # Se houver elementos restantes em x, adiciona-os ao vetor resultante

    vetor_resultante.extend(vetor_x[idx_x:])
  # Se houver elementos restantes em y, adiciona-os ao vetor resultante
    vetor_resultante.extend(vetor_y[idx_y:])
  # Convertendo o vetor resultante de volta para uma string

    resultado =' '.join(map(str, vetor_resultante))
  
    return resultado
  

def main():
    #lendo a string de cada entrada
    x = input()
    y = input()
# Chamando a função e imprimindo o resultado
    print("Vetor resultante da intercalação", intercalar_vetores(x, y))
    
#chamando o main
if __name__ == "__main__":
    main()

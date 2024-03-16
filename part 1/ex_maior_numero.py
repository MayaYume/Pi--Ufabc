import math
#input para primeiro número
n1 = int(input(" "))
#input para segundo número
n2 = int(input(""))

#função de verificação de qual numero é maior
def verifica_maior(n1, n2):
    # se(if) n1 for maior, mostrar ele 
    if n1 > n2:
        print(n1)
    # se não (else), mostrar n2
    else:
        print(n2)

# Chama a função passando as notas como argumentos
verifica_maior(n1, n2)

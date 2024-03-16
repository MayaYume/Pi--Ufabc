import math
#input para primeira nota
nota1 = int(input("Digite a nota da primeira prova: "))
#input para segunda nota
nota2 = int(input("Digite a nota da segunda prova: "))

#função de verificação de aprovação
def verifica_aprovacao(nota1, nota2):
    m = (nota1 + nota2) / 2
    # se(if) for maior ou igual a 5 aprovado(a)
    if m >= 5:
        print("Aprovado(a) com a média:", m)
    # se não (else) reprovado(a)
    else:
        print("Reprovado(a) com a média:", m)

# Chama a função passando as notas como argumentos
verifica_aprovacao(nota1, nota2)

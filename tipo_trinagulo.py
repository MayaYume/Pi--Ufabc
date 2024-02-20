def verifica_triangulo(a, b, c):
    if a > 0 and b > 0 and c > 0:
     
       if a == b == c:
          print("Triângulo EQUILÁTERO")
       elif a == b or a == c or b == c:
          print("Triângulo ISÓSCELES")
       else:
          print("Triângulo ESCALENO")
    else:
       print("As medidas dos lados NÃO formam um triângulo")
   


a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b: "))
c = int(input("Digite o valor do lado c: "))

verifica_triangulo(a, b, c)

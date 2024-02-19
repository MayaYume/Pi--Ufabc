def converter_fracao_mista(numerador, denominador):
    if denominador == 0:
        print("ERRO")
    else:
        parte_inteira = numerador // denominador
        novo_numerador = numerador % denominador
        print(f"{parte_inteira}({novo_numerador}/{denominador})")

# Obtém a fração própria do usuário
numerador = int(input())
denominador = int(input())

# Converte e imprime a fração mista
converter_fracao_mista(numerador, denominador)


def classificar_IDH(idh):
    if idh > 0.80:
        return "muito alto"
    elif 0.70 <= idh <= 0.80:
        return "alto"
    elif 0.55 <= idh < 0.70:
        return "médio"
    else:
        return "baixo"

def main():
    # Solicita ao usuário o valor de n
    n = int(input())

    # Lista para armazenar os países e seus respectivos IDHs
    paises = []

    # Loop para solicitar os n pares de string e número
    for i in range(n):
        nome_pais = input()
        idh = float(input())
        paises.append((nome_pais, idh))

    # Imprime a classificação para cada país
    for pais, idh in paises:
        classificacao = classificar_IDH(idh)
        print(f"{pais} tem IDH {classificacao}")

# Chamando a função principal
main()

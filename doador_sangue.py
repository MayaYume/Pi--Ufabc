def verificar_compatibilidade(idade, peso, tipo_sanguineo_doador, fator_rh_doador, tipo_sanguineo_receptor, fator_rh_receptor):
    # Verifica se a idade está dentro do intervalo válido e se o peso é adequado para doação
    if idade < 16 or idade > 69 or peso < 50:
        return "Doador não satisfaz requisitos mínimos"

    else:
        # Verifica se o fator RH do doador é compatível com o do receptor
        if fator_rh_doador == fator_rh_receptor or fator_rh_receptor == "+" or tipo_sanguineo_receptor== "A":
            # Verifica os diferentes tipos sanguíneos e suas compatibilidades
            if (tipo_sanguineo_doador == "A" and tipo_sanguineo_receptor == "A") or (tipo_sanguineo_doador == "O" and tipo_sanguineo_receptor == "A"):
                return "Tipos sanguíneos compatíveis"
            elif (tipo_sanguineo_doador == "B" and tipo_sanguineo_receptor == "B") or (tipo_sanguineo_doador == "O" and tipo_sanguineo_receptor == "B"):
                return "Tipos sanguíneos compatíveis"
            elif (tipo_sanguineo_doador == "A" and tipo_sanguineo_receptor == "AB") or (tipo_sanguineo_doador == "B" and tipo_sanguineo_receptor == "AB") or (tipo_sanguineo_doador == "O" and tipo_sanguineo_receptor == "AB"):
                return "Tipos sanguíneos compatíveis"
            elif tipo_sanguineo_doador == "O" and tipo_sanguineo_receptor == "O":
                return "Tipos sanguíneos compatíveis"
            else:
                return "Tipos sanguíneos incompatíveis"
        else:
            return "Tipos sanguíneos incompatíveis"


def main():
    # Lê os dados do usuário+++
    idade = int(input())
    peso = float(input())
    tipo_sanguineo_doador = input().upper()
    fator_rh_doador = input()
    tipo_sanguineo_receptor = input().upper()
    fator_rh_receptor = input()

    # Chama a função verificar_compatibilidade e exibe o resultado
    resultado = verificar_compatibilidade(idade, peso, tipo_sanguineo_doador, fator_rh_doador, tipo_sanguineo_receptor, fator_rh_receptor)
    print(resultado)

if __name__ == "__main__":
    main()

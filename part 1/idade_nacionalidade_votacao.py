from datetime import datetime

# Função para calcular a idade com base no ano de nascimento
def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade
    
# Função para determinar as mensagens com base na nacionalidade e idade
def verificar_nacionalidade_e_idade(idade, nacionalidade):
    print(f"Você tem {idade} anos")

    if nacionalidade == "brasileira":
        if idade >= 16:
            print("Já pode votar")
        if idade >= 18:
            print("Já pode solicitar a Carteira de Habilitação")
    else:
        print("Verifique as regras do país onde você vota e/ou pretende tirar carteira de habilitação")

# Entrada de dados
ano_nascimento = int(input(""))
nacionalidade = input("").lower()

# Calcular a idade e verificar mensagens
idade = calcular_idade(ano_nascimento)
verificar_nacionalidade_e_idade(idade, nacionalidade)

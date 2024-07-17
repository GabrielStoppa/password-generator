import random as rd

# Gera a senha
def gerar_senha(char, num_characters, opcao):
    senha = []
    if opcao == 3:
        # Letra minúscula
        senha.append(rd.choice('abcdefghijklmnopqrstuvwxyz'))
        # Letra maiúscula
        senha.append(rd.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        # Números
        senha.append(rd.choice('0123456789'))
        # Caracteres especiais
        senha.append(rd.choice('#$%&+-*='))

        # Preencher o restante da senha com caracteres aleatórios da lista completa
        for _ in range(num_characters - 4):
            senha.append(rd.choice(char))
    else:
        # Gerar senha com caracteres aleatórios da lista fornecida
        senha = [str(rd.choice(char)) for _ in range(num_characters)]

    # Embaralhar a senha para não deixar os caracteres fixos nas primeiras posições
    rd.shuffle(senha)

    return ''.join(senha)

# Seleciona o tipo da senha e o comprimento
continuar = True
while continuar:
    char = []
    opcao = int(input("Qual o tipo de senha que você deseja? (Numerica(1), Alfabetica(2), Completa(3)) "))

    if opcao == 1:
        print("\nOpção 1 Selecionada")
        char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    elif opcao == 2:
        print("\nOpção 2 Selecionada")
        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç']
    elif opcao == 3:
        print("\nOpção 3 Selecionada")
        char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '#', '$', '%', '&', '+',
                '-', '.', '*', '=', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    else:
        print("Nenhuma Opção selecionada")
        continue

    num_characters = int(input("Qual o comprimento da sua senha? "))

    # Garantir que o comprimento da senha seja suficiente para a opção "Completa(3)"
    if opcao == 3 and num_characters < 4:
        print("Para a opção Completa, o comprimento da senha deve ser de pelo menos 4 caracteres.")
    else:
        senha_gerada = gerar_senha(char, num_characters, opcao)
        print(f"Sua senha gerada é \"{senha_gerada}\"")

    # Pergunta se gostaria de fazer uma nova senha
    continuar_resposta = input("\nDeseja gerar uma nova senha? (S)im ou (N)ão ").upper()
    if continuar_resposta != "S":
        continuar = False

# Finaliza o projeto
print("Saindo....Programa finalizado com sucesso!")
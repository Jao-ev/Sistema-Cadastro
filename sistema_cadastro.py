# sistema_cadastro.py

usuarios = {}

def menu():
    print("\n--- Menu ---")
    print("1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Remover usuário")
    print("4. Sair")

def adicionar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    if email in usuarios:
        print("Usuário com este e-mail já existe.")
    else:
        usuarios[email] = nome
        print("Usuário adicionado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("\n--- Lista de Usuários ---")
        for email, nome in usuarios.items():
            print(f"Nome: {nome}, Email: {email}")

def remover_usuario():
    email = input("Digite o e-mail do usuário a ser removido: ")
    if email in usuarios:
        del usuarios[email]
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            remover_usuario()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

from menu import exibir_menu

def acesso():
    usuarios = {"admin": "123", "user": "456"}
    tentativas = 3

    while tentativas > 0:
        print("Bem vindo ao Sistema de Login!")
        usuario = input("Digite o seu Usuário: ")
        senha = input("Digite sua Senha: ")
        if usuario in usuarios and usuarios[usuario] == senha:
            print("Login bem-sucedido!")
            exibir_menu()
            return
        else:
            tentativas -= 1
            print(f"Credenciais inválidas. Tentativas restantes: {tentativas}")

    print("Acesso negado.")
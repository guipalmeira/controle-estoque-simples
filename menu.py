from estoque import cadastrar_produto, listar_produtos_por_fornecedor, remover_produto

def exibir_menu():
    while True:
        print("\n======= MENU ======= \nBem vindo ao MENU")
        print("1 - Cadastrar Produto")
        print("2 - Ver Estoque por Fornecedor")
        print("3 - Remover Produto")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Bem vindo ao Cadastro de Produtos\n")
            nome = input("Produto: ")
            qtde = int(input("Quantidade: "))
            valor = float(input("Valor: "))
            fornecedor = input("Fornecedor: ")
            cadastrar_produto(nome, qtde, valor, fornecedor)
        elif opcao == "2":
            print("Bem vindo ao Estoque\n")
            fornecedor = input("Nome do Fornecedor: ")
            produtos = listar_produtos_por_fornecedor(fornecedor)
            for prod in produtos:
                print(f"{prod[0]} - {prod[1]} unidades - R${prod[2]}")
        elif opcao == "3":
            print("Bem vindo a Remoção de produtos\n")
            nome = input("Nome do produto para remover: ")
            remover_produto(nome)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
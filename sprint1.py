usuarios = []
opcao = 0

while (opcao != '4'):
    #Opções que vão aparecer para o usuário escolher
    print("MENU")
    print("1. Cadastro de novo usuário")
    print("2. Solicitar serviço")
    print("3. Mostrar os usuários cadastrados")
    print("4. Sair")
    opcao = input("Escolha uma opção:")

    #Coleta de dados para cadastro
    if opcao == '1':
        nome = input("Digite seu nome de usuário: ")
        email = input("Digite seu email: ")
        senha = input("Crie uma senha: ")
        endereco = input("Digite seu endereço: ")
        usuarios.append({'nome': nome, 'email': email, 'senha': senha, 'endereco': endereco, 'servicos': []})
        print("Usuário cadastrado com sucesso!")
    # Coleta de dados para o serviço que o usuário irá pedir
    elif opcao == '2':
        nome_usuario_servico = input("Digite o nome do usuário que está cadastrando o serviço: ")
        for usuario in usuarios:
            if usuario['nome'] == nome_usuario_servico:
                id_servico = input("Digite o ID do serviço: ")
                localizacao = input("Digite a localização do serviço: ")
                tipo_servico = input("Digite o tipo do serviço: ")
                descricao = input("Digite a descrição do serviço: ")
                categoria = input("Digite a categoria do serviço: ")

                usuario['servicos'].append({'id_servico': id_servico, 'localizacao': localizacao, 'tipo_servico': tipo_servico, 'descricao': descricao, 'categoria': categoria})
                print("Serviço cadastrado com sucesso!")
                break
        #Caso o usuário que pedir o serviço não esteja cadastrado, printar:
        else:
            print("Usuário não encontrado. Por favor, cadastre o usuário antes de cadastrar o serviço.")
    #Opção para ver usúarios cadastrados e seus respectivos serviços
    elif opcao == '3':
        if usuarios:
            print("LISTA DE USUÁRIOS CADASTRADOS:")
            for usuario in usuarios:
                print(f"Nome: {usuario['nome']}, Email: {usuario['email']}, Endereço: {usuario['endereco']}")
                if usuario['servicos']:
                    print("Serviços solicitados:")
                    for servico in usuario['servicos']:
                        print(f"Tipo de serviço: {servico['tipo_servico']}")
                        print(f"Descrição: {servico['descricao']}")
                        print(f"Categoria: {servico['categoria']}")
                        print(f"Localização: {servico['localizacao']}")
        #Caso o usuário não esteja cadastrado, printar:
        else:
            print("Usuário não cadastrado.")
    #Opção sair: finalizar o programa
    elif opcao == '4':
        print(f"Programa finalizado")
        break
    else:
        print("Opção inválida")


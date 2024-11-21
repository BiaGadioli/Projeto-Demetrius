clientes = {
    "Maria das Neves": True,
    "Joana D'arc": True,
    "Fabiano de Melo": True,
    "Victor Luiz": True,
    "Beatriz Gadioli": True,
    "Luz": True
}

vendedores = {
    "Natalia": "123",
    "João": "123",
    "Ana": "123",
    "Vitoria": "123",
    "Bianca": "123",
}

produtos = {
    "banana": {"Nome": "Banana", "Quantidade": 54, "Unidade": "Por Cacho", "Preço": 4.00},
    "laranja": {"Nome": "Laranja", "Quantidade": 90, "Unidade": "Por Kg", "Preço": 8.00},
    "morango": {"Nome": "Morango", "Quantidade": 50, "Unidade": "Por Kg", "Preço": 24.00},
    "uva": {"Nome": "Uva", "Quantidade": 37, "Unidade": "Por Cacho", "Preço": 13.50},
    "maçã": {"Nome": "Maçã", "Quantidade": 78, "Unidade": "Por Kg", "Preço": 15.00},
    "kiwi": {"Nome": "Kiwi", "Quantidade": 20, "Unidade": "Por Kg", "Preço": 35.00},
    "maracujá": {"Nome": "Maracujá", "Quantidade": 51, "Unidade": "Por Kg", "Preço": 10.00},
    "cereja": {"Nome": "Cereja", "Quantidade": 28, "Unidade": "Por Kg", "Preço": 80.00},
    "framboesa": {"Nome": "Framboesa", "Quantidade": 67, "Unidade": "Por Kg", "Preço": 50.00},
    "manga": {"Nome": "Manga", "Quantidade": 57, "Unidade": "Por Kg", "Preço": 12.50}
}

relatorio_vendas = []

def verificar_login():
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua Senha: ")

    if usuario in vendedores:
        if vendedores[usuario] == senha:
            print("Login bem-sucedido!")
            cliente = input("Digite o nome do cliente: ")
            if cliente in clientes:
                print(f"Cliente {cliente} encontrado!")
                acessar_estoque(cliente, usuario) 
            else:
                print("Cliente não encontrado!")
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado!")

def acessar_estoque(cliente, vendedor):
    carrinho = [] 
    total = 0  
    print("\nAcesso ao estoque de frutas:")
    while True:
        print("\nEscolha uma fruta para comprar (ou digite 0 para finalizar a compra):")
        
        for i, (produto, dados) in enumerate(produtos.items(), 1):
            print(f"{i}. {dados['Nome']} - R${dados['Preço']:.2f} (Quantidade: {dados['Quantidade']})")
        
        escolha = int(input("\nDigite o número da fruta que deseja comprar: "))
        
        if escolha == 0:
            break  
        
        if 1 <= escolha <= len(produtos):
            produto_selecionado = list(produtos.values())[escolha - 1]
            print(f"\nVocê escolheu: {produto_selecionado['Nome']}")
            quantidade = int(input(f"Digite a quantidade que deseja comprar (Quantidade disponível: {produto_selecionado['Quantidade']}): "))
            
            if quantidade <= produto_selecionado["Quantidade"]:
                produto_selecionado["Quantidade"] -= quantidade
                carrinho.append((produto_selecionado['Nome'], quantidade, produto_selecionado['Preço']))
                total += produto_selecionado['Preço'] * quantidade
                print(f"{quantidade} {produto_selecionado['Nome']}(s) foram adicionados ao carrinho!")
                print(f"Estoque atualizado: {produto_selecionado['Quantidade']} {produto_selecionado['Nome']}(s) restantes.")
            else:
                print("Quantidade solicitada não disponível no estoque.")
        else:
            print("Escolha inválida!")

    imposto = total * 0.25
    total_com_imposto = total + imposto

    comissao = total_com_imposto * 0.05

    if carrinho:
        print("\nResumo da compra:")
        for item in carrinho:
            nome_produto, quantidade, preco = item
            print(f"{nome_produto} - {quantidade} unidade(s) - R${preco * quantidade:.2f}")
        
        print(f"\nTotal da compra: R${total:.2f}")
        print(f"Imposto (25%): R${imposto:.2f}")
        print(f"Total com imposto: R${total_com_imposto:.2f}")
        print(f"Comissão para o vendedor: R${comissao:.2f}")
    else:
        print("\nNenhum produto foi comprado.")
    
    print("Obrigado por comprar conosco!")

    relatorio_vendas.append({
        "Cliente": cliente,
        "Total": total_com_imposto,
        "Imposto": imposto,
        "Comissão Vendedor": comissao
    })

    novo_vendedor = input("\nDeseja realizar login com outro vendedor? (S/N): ").strip().lower()
    if novo_vendedor == "s":
        verificar_login()

    visualizar_relatorio = input("\nDeseja ver o relatório de vendas? (S/N): ").strip().lower()
    if visualizar_relatorio == "s":
        exibir_relatorio()

def exibir_relatorio():
    if relatorio_vendas:
        print("\nRelatório de Vendas Realizadas:")
        for venda in relatorio_vendas:
            print(f"\nCliente: {venda['Cliente']}")
            print(f"Total da venda: R${venda['Total']:.2f}")
            print(f"Imposto (25%): R${venda['Imposto']:.2f}")
            print(f"Comissão para o vendedor: R${venda['Comissão Vendedor']:.2f}")
    else:
        print("\nNenhuma venda foi realizada ainda.")

verificar_login()
global linhas_selecionadas
linhas_selecionadas = []
global carrinho
carrinho = []

def menu ():
    print("Oque deseja fazer agora?\n"
         "Fazer uma nova busca [1]\n"
         "Adicionar ao carrinho  [2]\n"
         "Checar Carrinho  [3]\n"
         "Finalizar compra [4]\n")

    desicao = int(input())
    if desicao == 1:
        busca()
    elif desicao == 2:
        adicionar_ao_carrinho()

def adicionar_ao_carrinho():
    print("Qual produto deseja adicionar ao carrinho")
    produto_selecionado = str(input())

    for i in linhas_selecionadas:
        i = i.strip("\n").split(",")
        if produto_selecionado == i[4]:
            carrinho.append(i)
            print("Produto adicionado ao carrinho!")
            menu()

def busca_lista (busca):
    with open("produtos - produtos.csv","r") as lista_produtos:
        next(lista_produtos)
        linha_arquivo = lista_produtos.readlines()


        for linha in linha_arquivo:
            nome, categoria,preco,quantidade,codproduto = linha.strip("\n").split(",")
            nome = nome.lower()
            categoria = categoria.lower()

            if busca.lower() in nome or busca == codproduto or busca == categoria:
                    linhas_selecionadas.append(linha)

        print("Codigo| Produto| Preco")
        for indx,selecao in enumerate(linhas_selecionadas[:5]):
            nome, categoria, preco, quantidade, codproduto= selecao.strip("\n").split(",")
            print(codproduto, nome, preco)

        menu()

busca = input("Digite sua chave de busca: ")
busca_lista(busca)











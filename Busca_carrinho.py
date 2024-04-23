global linhas_selecionadas
linhas_selecionadas = []
global carrinho
carrinho = []
global condicao_parada
condicao_parada = False


def checar_carrinho():
    total = 0
    print("Carinho:")
    print("Código| Produto| Preço ")
    for prod in carrinho:
        nome, categoria, preco, quantidade, cod_produto = prod
        total = total + preco
        print(f"{cod_produto} {nome} {categoria} {preco}")
        menu()
def menu ():
    condicao_parada = False
    print("Oque deseja fazer agora?\n"
          "Fazer uma nova busca [1]\n"
          "Adicionar ao carrinho [2]\n"
          "Finalizar compra [3]")
    if len(carrinho) > 0:
        print("Checar Carrinho  [4]\n")
    desicao = int(input())
    if desicao == 1:
        busca = input("Digite sua chave de busca: ")
        busca_lista(busca)
    elif desicao == 2:
        while condicao_parada == False:
            if condicao_parada == True:
                break
            condicao_parada = adicionar_ao_carrinho()
    elif desicao == 4:
        checar_carrinho()

def adicionar_ao_carrinho():
    print("Qual produto deseja adicionar ao carrinho?")
    produto_selecionado = str(input())

    for i in linhas_selecionadas:
        i = i.strip("\n").split(",")
        if produto_selecionado == i[4]:
            carrinho.append(i)
            print("Produto adicionado ao carrinho!")
            menu()
            return True
        else:
            print("Item fora da lista de procura")
            return False

def busca_lista (busca):
    linhas_selecionadas = []
    with open("produtos - produtos.csv","r") as lista_produtos:
        next(lista_produtos)
        linha_arquivo = lista_produtos.readlines()


        for linha in linha_arquivo:
            nome, categoria,preco,quantidade,cod_produto = linha.strip("\n").split(",")
            nome = nome.lower()
            categoria = categoria.lower()

            if busca.lower() in nome or busca == cod_produto or busca.lower() in categoria:
                    linhas_selecionadas.append(linha)

        print("Codigo| Produto| Preco")
        for indx,selecao in enumerate(linhas_selecionadas[:5]):
            nome, categoria, preco, quantidade, cod_produto= selecao.strip("\n").split(",")
            print(cod_produto, nome, preco)

        menu()

busca = input("Digite sua chave de busca: ")
busca_lista(busca)











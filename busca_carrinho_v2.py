import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
linhas_selecionadas = []
carrinho = []
condicao_parada = False
condicao_fim = False

def conversor_moeda(p):
    preco_format = locale.currency(p, grouping=True, symbol=False)
    return preco_format

def checar_carrinho():
    total = 0
    quantidade_itens = 0
    print("Carinho:")
    print("Código| Produto| Categoria| Preço ")
    for prod in carrinho:
        nome, categoria, preco, quantidade, cod_produto = prod.strip("\n").split(",")
        total = total + float(preco)
        preco = float(preco)
        quantidade_itens += 1
        print(f"{cod_produto} {nome} {categoria} R${conversor_moeda(preco)}")
    print(f"Quantidade de itens : {quantidade_itens}")
    print(f"Total do carrinho: R${conversor_moeda(total)}")

    return

def adicionar_ao_carrinho():
    print("Qual produto deseja adicionar ao carrinho? ")
    produto_selecionado = str(input())
    for i in linhas_atuais:
        nome, categoria, preco, quantidade, cod_produto = i.strip("\n").split(",")
        if produto_selecionado == cod_produto:
            carrinho.append(i)
            print("Produto adicionado ao carrinho!")
            return carrinho

    print("Item fora da lista de procura")
    return False

def retirar_do_carrinho():
    checar_carrinho()
    print("Qual produto deseja retirar do carrinho? ")
    prod_selecionado = str(input())
    for indx, i in enumerate(carrinho):
        nome, categoria, preco, quantidade, cod_produto = i.strip("\n").split(",")
        if prod_selecionado == cod_produto:
            carrinho.remove(carrinho[indx])
            print("Produto retirado do carrinho!")
            return True

    print("Item nao esta no carrinho!")
    return False

def busca_lista (busca):
    with open("produtos - produtos.csv","r", encoding='utf-8') as lista_produtos:
        next(lista_produtos)
        linha_arquivo = lista_produtos.readlines()
        linhas_selecionadas = []

        for linha in linha_arquivo:
            nome, categoria,preco,quantidade,cod_produto = linha.strip("\n").split(",")
            nome = nome.lower()
            categoria = categoria.lower()

            if busca.lower() in nome or busca.upper() == cod_produto or busca.lower() in categoria:
                    linhas_selecionadas.append(linha)

        print("Codigo| Produto| Preco")
        for indx,selecao in enumerate(linhas_selecionadas[:5]):
            nome, categoria, preco, quantidade, cod_produto= selecao.strip("\n").split(",")
            preco = float(preco)
            print(f"{cod_produto} {nome} R${conversor_moeda(preco)}")

        return linhas_selecionadas

while condicao_fim == False:
    print("===============================================")
    print("Menu de Opções:                               |")
    print("Fazer uma busca [1]                           |")
    print("Adicionar ao carrinho [2]                     |")
    print("Finalizar compra [3]                          |")
    if len(carrinho) > 0:
        print("Checar Carrinho [4]                           |")
        print("Retirar item do carrinho [5]                  |")
    print("===============================================")
    desicao = int(input())
    if desicao == 1:
        busca = input("Digite sua chave de busca: ")
        linhas_atuais = busca_lista(busca)
    elif desicao == 2:
        condicao_parada = False
        while condicao_parada == False:
            condicao_parada = adicionar_ao_carrinho()
    elif desicao == 3:
        condicao_fim = True
    elif desicao == 4:
        checar_carrinho()
    elif desicao == 5:
        condicao_parada = False
        while condicao_parada == False:
            condicao_parada = retirar_do_carrinho()
checar_carrinho()
print("Compra finalizada.")

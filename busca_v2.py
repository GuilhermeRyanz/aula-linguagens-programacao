busca = input()
linhas = []

with open("produtos - produtos.csv","r") as lista_produtos:
    next(lista_produtos)
    linha_arquivo = lista_produtos.readlines()

    for indx,linha in enumerate(linha_arquivo):
        if indx == 1 or indx == 3:
            continue
        linha = linha.strip('\n').split(",")
        linhas.append(linha)

    for linha2 in linhas:
       nome = linha2[0]
       categoria = linha2[1]
       valor = linha2[2]
       quantidade = linha2[3]
       codproduto = linha2[4]

       if busca.lower() in nome or busca == codproduto or busca == categoria:
            print(codproduto, nome, valor)
    # for linha in linha_arquivo:
    #     nome, categoria,valor,quantidade,codproduto = linha.strip("\n").split(",")
    #     nome = nome.lower()
    #     categoria = categoria.lower()
    #
    #     if busca.lower() in nome or busca == codproduto or busca == categoria:
    #             print(codproduto, nome, valor)
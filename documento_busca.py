from datetime import datetime

busca = input()
busca_nome, busca_sobrenome = busca.split(' ')
busca_nome = busca_nome.lower()
busca_sobrenome = busca_sobrenome.lower()

with open('alunos.csv', "r") as arquivo:
    next(arquivo)
    lista_linha = arquivo.readlines()

    for linha in lista_linha:
        nome_chamada, data_nacimento, matricula = linha.strip('\n').split(',')

        nome, sobrenome, numero = nome_chamada.split(' ')
        
        if (nome.lower() == busca_nome and sobrenome.lower() == busca_sobrenome):
            data_nacimento = datetime.strptime(data_nacimento, '%d/%m/%Y')
            data_atual = datetime.now()
            idade = data_atual.year - data_nacimento.year
            print("NOME", nome_chamada, "IDADE", idade)
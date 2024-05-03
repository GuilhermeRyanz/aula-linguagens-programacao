from verificar_alunos import nova_entrada, verificar_porcentagem_alunos, verificacao_personalisada
entrada_menu = 1
while entrada_menu != 0:

    print("Menu principal: ")
    print("Funcoes de gerente:")
    print("Verificar alunos por turno: [1] ")

    entrada_menu = int(input())

    if entrada_menu == 1:

        entrada = 0

        while entrada != 4:

            print("nova entrada de dados [1]")
            print("verificar porcentagem atual [2]")
            print("verificacao personalizada [3]")
            print("Sair [4]")
            entrada = int(input())

            if entrada == 1:
                nova_entrada()
            elif entrada == 2:
                verificar_porcentagem_alunos()
            elif entrada == 3:
                verificacao_personalisada()

            elif entrada == 4:
                print("saindo")

            else:
                print("entrada invalida")



nova_entrada()
verificar_porcentagem_alunos()
def verificar_vencedor(linhas):

    if linhas[0][0] == linhas[0][1] == linhas[0][2] == linhas[0][0] == linhas[1][0] == linhas[1][1] == linhas[1][2] ==linhas[2][0] == linhas[2][1] == linhas[2][2] == " ":
        print("nao nada no jogo da veia")

    elif linhas[0][0] == "X" and linhas[0][1] == "X" and linhas[0][2] == "X":
        print("O X GANHOU")
        return True
    elif linhas[1][0] == "X" and linhas[1][1] == "X" and linhas[1][2] == "X":
        print("O X GANHOU")
        return True
    elif linhas[2][0] == "X" and linhas[2][1] == "X" and linhas[2][2] == "X":
        print("O X GANHOU")
        return True

    elif linhas[0][0] == "X" and linhas[1][0] == "X" and linhas[2][0] == "X":
        print("O X GANHOU")
        return True
    elif linhas[0][1] == "X" and linhas[1][1] == "X" and linhas[2][1] == "X":
        print("O X GANHOU")
        return True
    elif linhas[0][2] == "X" and linhas[1][2] == "X" and linhas[2][2] == "X":
        print("O X GANHOU")
        return True

    elif linhas[0][0] == "X" and linhas[1][1] == "X" and linhas[2][2] == "X":
        print("O X GANHOU")
        return True
    elif linhas[2][0] == "X" and linhas[1][1] == "X" and linhas[0][2] == "X":
        print("O X GANHOU")
        return True

    elif linhas[0][0] == "O" and linhas[0][1] == "O" and linhas[0][2] == "O":
        print("O O GANHOU")
        return True
    elif linhas[1][0] == "O" and linhas[1][1] == "O" and linhas[1][2] == "O":
        print("O O GANHOU")
        return True
    elif linhas[2][0] == "O" and linhas[2][1] == "O" and linhas[2][2] == "O":
        print("O O GANHOU")
        return True

    elif linhas[0][0] == "O" and linhas[1][0] == "O" and linhas[2][0] == "O":
        print("O O GANHOU")
        return True
    elif linhas[0][1] == "O" and linhas[1][1] == "O" and linhas[2][1] == "O":
        print("O O GANHOU")
        return True
    elif linhas[0][2] == "O" and linhas[1][2] == "O" and linhas[2][2] == "O":
        print("O O GANHOU")
        return True

    elif linhas[0][0] == "O" and linhas[1][1] == "O" and linhas[2][2] == "O":
        print("O O GANHOU")
        return True
    elif linhas[2][0] == "O" and linhas[1][1] == "O" and linhas[0][2] == "O":
        print("O O GANHOU")
        return True

    elif linhas[0][0] == " " or linhas[0][1] == " " or linhas[0][2] == " " or linhas[1][0] == " " or linhas[1][1] == " " or linhas[1][2] or linhas [2][0] == " " or linhas[2][1] == " " or linhas[2][2] == " ":
        print("O jogo ainda não foi finalizado! ")

    else:
        print("Empate")


def verificar_vencedor_1():
    with open ("jogo_da_veia.txt", "r") as jogo:
        lista_linhas = jogo.readlines()
        linhas = []

    for indx,linha in enumerate(lista_linhas):
        if indx == 1 or indx == 3:
            continue
        linha = linha.strip('\n').split("|")
        linhas.append(linha)

    if verificar_vencedor(linhas) == True:
        return True
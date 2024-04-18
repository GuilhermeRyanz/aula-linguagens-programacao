print("="*28)
print("Bem vindo ao Jogo da veia  |")
print("="*28)

global verificacao
verificacao = 0

def alter_doc(tabuleriro):
    with open("jogo_da_veia.txt", "w") as jogo_doc:
        jogo_doc.write(f"{tabuleiro_1[0][0]}|{tabuleriro[0][1]}|{tabuleriro[0][2]}\n-----\n{tabuleiro_1[1][0]}|{tabuleriro[1][1]}|{tabuleriro[1][2]}\n-----\n{tabuleiro_1[2][0]}|{tabuleriro[2][1]}|{tabuleriro[2][2]}")

global tabuleiro_1
tabuleiro_1 = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def imprimir_tabuleiro(tabuleiro):
    print(F"{tabuleiro_1[0][0]}|{tabuleiro_1[0][1]}|{tabuleiro_1[0][2]}\n"
          F"-----\n"
          F"{tabuleiro_1[1][0]}|{tabuleiro_1[1][1]}|{tabuleiro_1[1][2]}\n"
          F"-----\n"
          F"{tabuleiro_1[2][0]}|{tabuleiro_1[2][1]}|{tabuleiro_1[2][2]}\n")
def marcar_posicao(jogador,linha,coluna):
    if tabuleiro_1[linha][coluna] != "X" and tabuleiro_1[linha][coluna] != "O":
        tabuleiro_1[linha][coluna] = jogador
        alter_doc(tabuleiro_1)
        return tabuleiro_1
    else:
        print("entrada invalida")
        jogada_x_l, jogada_x_c = input(f"É a vez do jogador {jogador}, em qual posição você deseja jogar?\n").split()
        jogada_x_c = int(jogada_x_c)
        jogada_x_l = int(jogada_x_l)
        marcar_posicao("X", jogada_x_l, jogada_x_c)

imprimir_tabuleiro(tabuleiro_1)

jogada_x_l, jogada_x_c = input("É a vez do jogador X, em qual posição você deseja jogar?\n").split()
jogada_x_c = int(jogada_x_c)
jogada_x_l = int(jogada_x_l)
marcar_posicao("X",jogada_x_l,jogada_x_c)

imprimir_tabuleiro(tabuleiro_1)

jogada_O_l, jogada_O_c = input("É a vez do jogador O, em qual posição você deseja jogar?\n").split()
jogada_O_c = int(jogada_O_c)
jogada_O_l = int(jogada_O_l)
marcar_posicao("O",jogada_O_l,jogada_O_c)

imprimir_tabuleiro(tabuleiro_1)

jogada_x_l, jogada_x_c = input("É a vez do jogador X, em qual posição você deseja jogar?\n").split()
jogada_x_c = int(jogada_x_c)
jogada_x_l = int(jogada_x_l)
marcar_posicao("X",jogada_x_l,jogada_x_c)

imprimir_tabuleiro(tabuleiro_1)

jogada_O_l, jogada_O_c = input("É a vez do jogador O, em qual posição você deseja jogar?\n").split()
jogada_O_c = int(jogada_O_c)
jogada_O_l = int(jogada_O_l)
marcar_posicao("O",jogada_O_l,jogada_O_c)

imprimir_tabuleiro(tabuleiro_1)

jogada_x_l, jogada_x_c = input("É a vez do jogador X, em qual posição você deseja jogar?\n").split()
jogada_x_c = int(jogada_x_c)
jogada_x_l = int(jogada_x_l)
marcar_posicao("X",jogada_x_l,jogada_x_c)

imprimir_tabuleiro(tabuleiro_1)

jogada_O_l, jogada_O_c = input("É a vez do jogador O, em qual posição você deseja jogar?\n").split()
jogada_O_c = int(jogada_O_c)
jogada_O_l = int(jogada_O_l)
marcar_posicao("O",jogada_O_l,jogada_O_c)

imprimir_tabuleiro(tabuleiro_1)

jogada_x_l, jogada_x_c = input("É a vez do jogador X, em qual posição você deseja jogar?\n").split()
jogada_x_c = int(jogada_x_c)
jogada_x_l = int(jogada_x_l)
marcar_posicao("X",jogada_x_l,jogada_x_c)

imprimir_tabuleiro(tabuleiro_1)

jogada_O_l, jogada_O_c = input("É a vez do jogador O, em qual posição você deseja jogar?\n").split()
jogada_O_c = int(jogada_O_c)
jogada_O_l = int(jogada_O_l)
marcar_posicao("O",jogada_O_l,jogada_O_c)

imprimir_tabuleiro(tabuleiro_1)

jogada_x_l, jogada_x_c = input("É a vez do jogador X, em qual posição você deseja jogar?\n").split()
jogada_x_c = int(jogada_x_c)
jogada_x_l = int(jogada_x_l)
marcar_posicao("X",jogada_x_l,jogada_x_c)

imprimir_tabuleiro(tabuleiro_1)




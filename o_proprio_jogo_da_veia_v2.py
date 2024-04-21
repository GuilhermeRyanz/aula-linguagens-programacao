import os
import sys
from quem_ganhou_o_jogo_da_veia_v2 import verificar_vencedor_1, verificar_vencedor
print("="*28)
print("Bem vindo ao Jogo da veia  |")
print("="*28)

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
        if verificar_vencedor_1() == True:
            print("Fim de jogo")

    else:
        print("entrada invalida")
        jogada_x_l, jogada_x_c = input(f"É a vez do jogador {jogador}, em qual posição você deseja jogar?\n").split()
        jogada_x_c = int(jogada_x_c)
        jogada_x_l = int(jogada_x_l)
        marcar_posicao(jogador, jogada_x_l, jogada_x_c)
        if verificar_vencedor_1() == True:
            print("Fim de jogo")
            sys.exit()

imprimir_tabuleiro(tabuleiro_1)

for vez in range(0,9):

    if vez%2 != 0:
        joador = "O"
    else:
        joador = "X"

    jogada_x_l, jogada_x_c = input(F"É a vez do jogador {joador}, em qual posição você deseja jogar?\n").split()
    jogada_x_c = int(jogada_x_c)
    jogada_x_l = int(jogada_x_l)
    marcar_posicao(joador,jogada_x_l,jogada_x_c)

    imprimir_tabuleiro(tabuleiro_1)

    if verificar_vencedor_1() == True:
        print("Fim de jogo")
        sys.exit()



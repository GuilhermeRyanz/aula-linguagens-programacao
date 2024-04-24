import os
import sys
from quem_ganhou_o_jogo_da_veia_v2 import verificar_vencedor_1, verificar_vencedor
print("="*28)
print("Bem vindo ao Jogo da veia  |")
print("="*28)
global fim_jogo
fim_jogo = False
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
        if verificar_vencedor_1() == True:
            imprimir_tabuleiro(tabuleiro_1)
            fim_jogo == True
            print("Fim de jogo")
            sys.exit()
        return True
    else:
        print("entrada invalida!")
        return False

for vez in range(0,9):
    imprimir_tabuleiro(tabuleiro_1)
    condicao_marcar = False
    if vez%2 != 0:
        jogador = "O"
    else:
        jogador = "X"

    while condicao_marcar != True:
        jogada_l, jogada_c = input(F"É a vez do jogador {jogador}, em qual posição você deseja jogar?\n").split()
        jogada_c = int(jogada_c)
        jogada_l = int(jogada_l)
        condicao_marcar = marcar_posicao(jogador, jogada_l, jogada_c)

    if fim_jogo == True:
        print("Fim de jogo")
        sys.exit()

imprimir_tabuleiro(tabuleiro_1)


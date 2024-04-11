nome = str(input())
posicao = int(input())

letra_selecionada = nome[posicao]

if letra_selecionada == "r" or letra_selecionada == "R":
    letra_selecionada = "s"
    print(nome[:posicao] + letra_selecionada + nome[posicao+1:])
elif letra_selecionada == "m" or letra_selecionada == "M":
    letra_selecionada = "n"
    print(nome[:posicao] + letra_selecionada + nome[posicao + 1:])
else:
    print(nome[:posicao] + "" + nome[posicao + 1:])

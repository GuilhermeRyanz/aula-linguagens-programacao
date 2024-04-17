c = "texto"
with open("ttt.txt", "w") as arquvio:
    nome = input()
    while nome != 'sair':
        arquvio.write(nome + "\n")
        arquvio.write(c + "\n")
        nome = input()
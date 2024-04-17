from datetime import datetime
with open("Exercicio.txt", "w") as exercicio:
    nome = "GUILHERME RYAN FURTADO DOS SANTOS\n"
    data_de_hoje = datetime.now().strftime('%d/%m/%Y')
    localizacao = "MANAUS_AM\n"
    idade = 22
    bairro = "LAGO AZUL\n"
    exercicio.write(nome)
    exercicio.write(data_de_hoje)
    exercicio.write("\t")
    exercicio.write(localizacao)
    exercicio.write(str(idade))
    exercicio.write("\t")
    exercicio.write(localizacao)
    nome, nota = str(input()).split(" ")
    while  nome != "sair" and nota != "sair":
        exercicio.write(nome + "," + nota + "\n")
        nome, nota = str(input()).split(" ")
        

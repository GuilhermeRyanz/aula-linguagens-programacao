def menu():
    print("Caralho")

selecao = 0

while selecao != 5:
    menu()
    selecao = int(input())
    if selecao == 1:
        busca()
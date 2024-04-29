n = int(input())
contagens_3 =  [[0]*4 for I in range(n)]

contador = 1
for l in range(len(contagens_3)):
    for c in range(len(contagens_3[l])):
        contagens_3[l][c] = contador
        contador += 1

contador_2 = 0
for indx ,linha in enumerate(contagens_3):
    print(f"{linha[0]} {linha[1]} {linha[2]} PUM")


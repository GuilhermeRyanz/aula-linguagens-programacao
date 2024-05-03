from datetime import datetime
print("cadastro e verificacao de frequencia")
entrada = 0


def nova_entrada(turno_manha, turno_tarde, turno_noite, data_1):
    with open("alunos_academia.csv","a") as arquivos_alunos:

        verificar_1 = False
        while verificar_1 == False:
            try:
                if turno_manha > 0:
                    verificar_1 = True
            except:
                print("Entrada invalida Apenas numeros inteiro positivos permitidos.")
                verificar_1 = False


        verificar_2 = False
        while verificar_2 == False:
            try:
                if turno_tarde > 0:
                    verificar_2 = True
            except:
                print("Entrada invalida Apenas numeros inteiro positivos permitidos,")
                verificar_2 = False

        verificar_3 = False
        while verificar_3 == False:
            try:
                if turno_noite > 0:
                    verificar_3 = True
            except:
                print("Entrada invalida Apenas numeros inteiro positivos permitidos.")
                verificar_3 = False

        verificar_4 = False
        while verificar_4 == False:
            try:
                data = data_1
                data = datetime.strptime(data, "%d/%m/%Y")
                data = datetime.strftime(data, format="%d/%m/%Y")
                verificar_4 = True
            except:
                print("entrada invalida")
                verificar_4 = False


        arquivos_alunos.write(f"{str(turno_manha)},{str(turno_tarde)},{str(turno_noite)},{data}\n")

        return

def verificar_porcentagem_alunos():
    resultados = ""
    total_t1 = 0
    total_t2 = 0
    total_t3 = 0

    with open("alunos_academia.csv","r") as arquivos_alunos:
        next(arquivos_alunos)
        linhas_alunos = arquivos_alunos.readlines()

        for linha in linhas_alunos:
            t1 , t2 , t3, data = linha.strip("\n").split(",")
            t1 = int(t1)
            t2 = int(t2)
            t3 = int(t3)

            total_t1 += t1
            total_t2 += t2
            total_t3 += t3

    soma = total_t3 + total_t2 + total_t1

    porcent_1 = total_t1/soma * 100
    porcent_2 = total_t2/soma * 100
    porcent_3 = total_t3/soma * 100

    # print("------------------------------------------------------")
    # print("Prcentagem de alunos por turno: ")
    # print(f"Porcentagem de alunos no turno da manha: {porcent_1:.2f}%")
    # print(f"Porcentagem de alunos no turno da tarde: {porcent_2:.2f}%")
    # print(f"Porcentagem de alunos no turno da noite: {porcent_3:.2f}%")
    # print("------------------------------------------------------")

    resultados += "Prcentagem de alunos por turno: \n"
    resultados += f"Porcentagem de alunos no turno da manha: {porcent_1:.2f}%\n"
    resultados += f"Porcentagem de alunos no turno da tarde: {porcent_2:.2f}%\n"
    resultados += f"Porcentagem de alunos no turno da noite: {porcent_3:.2f}%\n"

    return resultados

def verificacao_personalisada():

    total_t1 = 0
    total_t2 = 0
    total_t3 = 0

    verificacao_1 = False

    while verificacao_1 == False:
        try:
            busca = str(input("Digide a data de busca: "))

            with open("alunos_academia.csv", "r") as arquivos_alunos:
                next(arquivos_alunos)
                linhas_alunos = arquivos_alunos.readlines()

                for linha in linhas_alunos:
                    t1, t2, t3, data = linha.strip("\n").split(",")
                    if busca == data[3:]:
                        t1 = int(t1)
                        t2 = int(t2)
                        t3 = int(t3)

                        total_t1 += t1
                        total_t2 += t2
                        total_t3 += t3

                soma = total_t3 + total_t2 + total_t1

                porcent_1 = total_t1 / soma * 100
                porcent_2 = total_t2 / soma * 100
                porcent_3 = total_t3 / soma * 100

                print("------------------------------------------------------")
                print("Prcentagem de alunos por turno")
                print(f"Porcentagem de alunos no turno da manha: {porcent_1:.2f}%")
                print(f"Porcentagem de alunos no turno da tarde: {porcent_2:.2f}%")
                print(f"Porcentagem de alunos no turno da noite: {porcent_3:.2f}%")
                print("------------------------------------------------------")
                verificacao_1 = True

        except:
            print("Entrada invalida! ")
            verificacao_1 = False


# while entrada !=  4:
#
#     print("nova entrada de dados [1]")
#     print("verificar porcentagem atual [2]")
#     print("verificacao personalizada [3]")
#     print("Sair [4]")
#     entrada = int(input())
#
#     if entrada == 1:
#         nova_entrada()
#     elif entrada == 2:
#         verificar_porcentagem_alunos()
#     elif entrada == 3:
#         verificacao_personalisada()
#
#     elif entrada == 4:
#         print("saindo")
#
#     else:
#         print("entrada invalida")
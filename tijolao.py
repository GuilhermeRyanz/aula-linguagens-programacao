codigo_prontos = []
tamanho = len(codigo_prontos)

t2 = "abc1"
t3 = "def3"
t4 = "ghi4"
t5 = "jkl5"
t6 = "mno6"
t7 = "pqrs7"
t8 = "tuv8"
t9 = "wxyz9"

def traduzir_tijolao(letra,lista,numero):
    codigo = []
    n = numero
    t = lista
    if letra == " ":
        codigo.append("0")

    if letra in t.upper():
        for indx, letra2 in enumerate(t):
            if letra2.upper() == letra:
                codigo.append("#")
                codigo.append(n *(indx+1))
    if letra.lower() in t.lower() and tamanho > 0 and codigo_prontos[tamanho-1].lower() in t.lower():
        for indx, letra2 in enumerate(t):
            if letra2.lower() == letra.lower():
                codigo.append("*")
                codigo.append(n *(indx+1))

    elif letra in t:
        for indx,letra2 in enumerate(t):
            if letra2 == letra:
                codigo.append(n *(indx+1))

    codigo = "".join(codigo)
    codigo_prontos.append(codigo)
    return codigo_prontos

numero_de_casos = int(input())
for i in range(numero_de_casos):
    codigo = []
    palavra = input()
    for indx,letra in enumerate(palavra):
        if letra.upper() in t2.upper():
            numero = "2"
            traduzir_tijolao(letra,t2,numero)


print("".join(codigo_prontos))
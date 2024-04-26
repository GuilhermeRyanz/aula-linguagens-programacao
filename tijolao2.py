t2 = "abc1"
t3 = "def3"
t4 = "ghi4"
t5 = "jkl5"
t6 = "mno6"
t7 = "pqrs7"
t8 = "tuv8"
t9 = "wxyz9"

codigo_prontos = []

numero_de_casos = int(input())
for i in range(numero_de_casos):
    codigo = []
    palavra = input()
    for indx,letra in enumerate(palavra):

        if letra.lower() in t2.lower():
            numero = "2"
        elif letra.lower() in t3.lower():
            numero = "3"
        elif letra.lower() in t4.lower():
            numero = "4"
        elif letra.lower() in t5.lower():
            numero = "5"
        elif letra.lower() in t6.lower():
            numero = "6"
        elif letra.lower() in t7.lower():
            numero = "7"
        elif letra.lower() in t8.lower():
            numero = "8"
        elif letra.lower() in t9.lower():
            numero = "9"

        if letra == " ":
            codigo.append("0")
        if letra.isupper():
            codigo.append("#")
        if letra.lower() == palavra[indx-1].lower():
            codigo.append("*")

        if letra.lower() in t2:
            for indx, letra2 in enumerate(t2):
                if letra.lower() == letra2:
                    codigo.append(numero*(indx+1))
print(codigo)
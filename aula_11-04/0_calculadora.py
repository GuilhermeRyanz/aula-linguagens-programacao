
def soma(v1, v2):
    return v1 + v2


def subtracao(v1, v2):
    return v1 - v2


def multiplicacao(v1, v2):
    return v1 * v2


def divisao(v1, v2):
    return v1  / v2

valor1 = float(input())
operador = input()
valor2 = float(input())

while valor1 != -1 and valor2 != -1:

    if operador == '+':
       print(soma(valor1,valor2))
    elif operador == '-':
        print(subtracao(valor2,valor1))
    elif operador == "*":
        print(multiplicacao(valor2,valor1))
    elif operador == "/":
        print(divisao(valor1,valor2))

    valor1 = float(input())
    operador = input()
    valor2 = float(input())
    
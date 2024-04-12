# O código abaixo tem alguns problemas e está incompleto! 
# Altere o código abaixo para que ele atue como uma calculadora
# O usuário deve digitar um valor, um operador e outro valor
# seu programa deverá imprimir na tela o resultado da operação
# Faça com que o seu programa funcione até que o usuário digite -1

valor1 = float(input())
operador = input()
valor2 = float(input())

while valor1 != -1 and valor2 != -1:

    if operador == '+':
        resultado = valor1 + valor2
    elif operador == '-':
        resultado = valor1 - valor2
    elif operador == "*":
        resultado = valor1 * valor2
    elif operador == "/":
        resultado = valor1 / valor2

    print(resultado)

    valor1 = float(input())
    operador = input()
    valor2 = float(input())
    
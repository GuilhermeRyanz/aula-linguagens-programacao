# O código abaixo é uma tentativa de criar um verificador de palíndromos.
# Palíndromos são palavras ou frases que são iguais quando lidas de trás para frente.
# No entanto, o código está incompleto e contém erros.
# Complete e corrija o código para que ele funcione corretamente.
# O usuário deve digitar uma palavra ou frase, e o programa deve imprimir se é um palíndromo ou não.
# Ignore espaços, pontuações e diferenças entre maiúsculas e minúsculas.

texto = input("Digite um texto: ")
texto = texto.upper()
texto_junto = texto.join("")
verificacaço = True

texto_invertido = texto_junto[::-1]

for i in range(len(texto_junto)):
    if texto_junto[i] != texto_invertido[i]:
        verificacaço = False

if verificacaço == True:
    print("é palindromo")
else:
    print("Não é palindromo")
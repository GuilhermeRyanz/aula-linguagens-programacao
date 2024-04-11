notas = []
soma  = 0
contador = 1
entrada = 0

while entrada != -1:
    entrada = float(input(F"Digite o {contador} ^ valor "))
    if entrada == -1:
        break
    notas.append(entrada)
    contador = contador + 1

print(notas)

media = sum(notas)/len(notas)

if media >= 7:
    print("O aluno foi aprovado ")
    print(f"{media:.2f}")

else:
    print("Aluno reprovado, Burrao!")
    print(f"{media:.2f}")
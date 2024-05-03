import sys
ent = int(input())
if ent < 1 or ent > 10**4:
    sys.exit(0)

entrada = input().split()

if len(entrada) > ent:
    sys.exit(0)

for i in entrada:
    if int(i) > (2**23-1) or int(i) < -2**31:
        sys.exit(0)

sequencia = []
contador = 1
for i,valor in enumerate(entrada):
    if i == 0:
        continue
    elif i == len(entrada) - 1:
        if valor == entrada[i-1]:
            contador += 1
            sequencia.append(contador)

    elif valor == entrada[i-1]:
        contador +=1

    elif valor != entrada[i-1]:
        sequencia.append(contador)
        contador = 1

sequencia = sorted(sequencia,reverse=True)

print(sequencia[0])

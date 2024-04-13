def tamanhoPalavra(palavra):

    contador = 0
    for carac in palavra:
        contador += 1
    
    return contador

print(len("Guilherme"))
print(tamanhoPalavra("Guilherme"))
entrada = int(input())

if entrada > 0 and entrada < 13:
    print("Criança")
elif entrada >= 13 and entrada < 18:
    print("Adolecente")
elif entrada >= 18 and entrada < 60:
    print("Adulto")
elif entrada >= 60:
    print("Idoso")
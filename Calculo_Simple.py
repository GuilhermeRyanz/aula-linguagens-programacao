entrada_1 = input()
cod , num, valor_uni = entrada_1.split()
entrada_2 = input()
cod2, num2, valor_uni2 = entrada_2.split()

cod = int(cod)
cod2 = int(cod)

num = int(num)
num2 = int(num2)

valor_uni = float(valor_uni)
valor_uni2 = float(valor_uni2)

tota = (num * valor_uni) + (num2 * valor_uni2)

print(f"VALOR A PAGAR: R$ {tota:.2f}")

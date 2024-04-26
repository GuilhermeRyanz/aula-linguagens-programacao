nome = input()
salario = float(input())
total_vendas = float(input())

comissao = total_vendas*15/100

total = comissao+salario

print(f"TOTAL = R$ {total:.2f}")
valor_conta = float(input("Valor da conta: R$ "))

percentual_gorjeta = float(input("Percentual de gorjeta (ex: 10, 15 ou 20): "))


gorjeta = valor_conta * (percentual_gorjeta / 100)

total = valor_conta + gorjeta


print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total: R$ {total:.2f}")
valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite o valor final: "))

soma = 0

for num in range(valor_inicial, valor_final + 1):
    soma += num

print(f"A soma de todos os números inteiros entre {valor_inicial} e {valor_final} é: {soma}")


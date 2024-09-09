N = int(input("Digite a quantidade de números: "))

maior_numero = None
posicao_maior = None

for i in range(1, N + 1):
    valor = int(input(f"Digite o {i}º valor: "))
    
    if maior_numero is None or valor > maior_numero:
        maior_numero = valor
        posicao_maior = i

print(f"O maior número é {maior_numero} e foi o {posicao_maior}º valor inserido.")
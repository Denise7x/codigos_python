soma_peso = 0
soma_idade = 0

for i in range(1, 6):
    print(f"\nJogador {i}:")
    peso = float(input("Digite o peso do jogador (em kg): "))
    idade = int(input("Digite a idade do jogador: "))
    
    soma_peso += peso
    soma_idade += idade

peso_medio = soma_peso / 5
idade_media = soma_idade / 5

print(f"\nPeso médio do time: {peso_medio:.2f} kg")
print(f"Idade média dos jogadores: {idade_media:.2f} anos")

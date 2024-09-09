idades = 0

for contador in range(5):
    idade = int(input(f"Digite a idade da pessoa {contador + 1}: "))
    if idade>=18:
        idades+=1

print(f"Quantidade de pessoas com 18 anos ou mais: {idades}")

        
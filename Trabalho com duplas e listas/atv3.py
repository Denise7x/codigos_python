numero = []
vetor = []
for valor in range(1,7):
    
    while True: 
        valor = int(input("Informe o valor numérico: "))
        numero.append(valor)

        break

print("Lista de valores", numero)

while True:
        num1 = posicao1 = int(input("Escolha um valor da lista: "))
        num2 = posicao2 = int(input("Escolha outra valor da lista: "))
        
        print(f"Operações com os valores {posicao1} e {posicao2}:")

        print(f"Soma: {num1} + {num2} = {num1 + num2}")

        print(f"Subtração: {num1} - {num2} = {num1 - num2}")
        
        print(f"Produto: {num1} * {num2} = {num1 * num2}")

        break

entrada1 = input("Digite os números inteiros da primeira lista, separados por espaço: ")
lista1 = list(map(int, entrada1.split()))

entrada2 = input("Digite os números inteiros da segunda lista, separados por espaço: ")
lista2 = list(map(int, entrada2.split()))


numeros_comuns = []
for numero in lista1:
    if numero in lista2 and numero not in numeros_comuns:
        numeros_comuns.append(numero)

numeros_comuns.sort()

print("Números comuns em ordem crescente:", numeros_comuns)

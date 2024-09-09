numero = int(input("Digite um numéro inteiro: "))

print(f"Os divisores de {numero} são:")
for contador in range(1, numero + 1):
    if numero % contador==0:
        print(contador)

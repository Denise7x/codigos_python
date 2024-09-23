numero = []
for valor in range(1,6):
    
    while True: 
        valor = int(input("Informe o valor numérico: "))
        numero.append(valor)

        break
    
print("Lista completa", numero)

divisiveis_por_3 = [num for num in numero if num % 3 == 0]
print("Números divisíveis por 3:", divisiveis_por_3)
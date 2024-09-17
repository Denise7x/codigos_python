
while True: 
    valor = int(input("Informe o valor inteiro: "))  
    if valor < 0: 
        print('Programa encerrado')
        break

    if valor > 100:
        print("Limite excedido.")  

    elif valor > 10:
        quadrado = valor ** 2
        print(f"O quadrado de {valor} é {quadrado}.")
    
    elif valor > 5:
        cubo = valor ** 3
        print(f"O cubo de {valor} é {cubo}.")
    
    else:
        print("O valor digitado não atende aos critérios.")    
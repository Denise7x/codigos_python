valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))

if valorB == 0:
    print("Divisão por zero não é permitida.")
else:
   
    if valorA % valorB == 0:
        print(f"O valor de A é divisível por B.")
    else:
        print(f"O valor de A não é divisível por B.")
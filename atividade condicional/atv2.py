nome = input("Informe seu nome: ")
sexo = input("\nInforme o seu sexo, se for feminino digite F, caso seja masculino digite M: \n")
estado = input("informe o seu estado civil em letras maiusculas: ")

if estado == "CASADA":
    tempo = input("\nInforme o tempo de casado/o: ")
    print(f"{nome} você é casada/o a: {tempo}")
else:
    print(f"{nome}, obrigado e até a proxima ")
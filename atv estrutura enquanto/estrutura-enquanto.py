#1 forma de utilizar while - semelhante ao FOR

contador = 1

while contador <=5:
    print(contador)
    contador = contador + 1 #é o mesmo contador +=1

#2 forma de utilizar enquanto - loop condicional nomal
valor = 0

while valor >= 0:
    valor = int (input("Informa um valor qualquer (digite um valor negativo para terminar: )"))
    print(f"você digitou {valor}")

#3 forma de utilizar o enquanto - semelhante a estrutura faça...enquanto
while True: 
    senha = input("Informe sua senha: ")    

    if senha == "123":
        print("Parabéns, senha correta")
        break # forma de encerrar o loop 
    else:
        print("Senhas não conferem, tente novamente")
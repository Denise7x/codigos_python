animais = ["Cachorr", "Gato","Ovelha"]
print(type(animais))#exbindo o tipo de variável

print(animais)

#Exibindo todos os itens da lista
print("."*50)
for itens in animais:
    print(itens)

#1 Etapa: Atualizar dados
print("."*50)
animais[0] = "Coelhos"
print(animais)

#2 Etapa: Inserir dados
print("."*50)
#Forma 1 - usando append
animais.appand("Cavalo")#irá inserir um novo item no final da l
print(animais)

#2ª forma - usando insert 
animais.insert(1, "Pásaro") #O insert precisa de 2 valores, o 1º será o índice que desejo inserir o valor . O 2º é o conteúdo que quero inserir na lista (inserir em qualquer lugar)
print(animais)

#3ª Etapa - Excluir dados 
print("-"*50)
#Forma 1 - usando pop()
animais.pop() #Remove o último item de lista 
print(animais)

#Forma 2- usando pop() com índice 
animais.pop(0) # Serve para escolher qual índice da lita será excluído 
print(animais)

#Forma 3 - Usando remove 
animais.remove("Ovelha")#Irá remover o item pelo seu conteúdo
print(animais)

ano = int(input("Digite um ano: "))

if ano % 400 == 0:
     resultado = print(f"O ano {ano} é bissexto.")

elif ano % 4 == 0 and ano % 100 != 0:
        resultado = print(f"O ano {ano} é bissexto.")

else: print(f"O ano {ano} não é bissexto.")  
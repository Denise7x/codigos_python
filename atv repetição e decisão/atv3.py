import time
def contador(segundos): 
    
    for jj in range (segundos,0,-1):
        print(jj)
        time.sleep(1)


segundos = int(input("Informe a quantidade de segundos: "))

print(contador(segundos))

    
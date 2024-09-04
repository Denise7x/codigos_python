A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

def ordenar_tres_valores(A, B, C):
    if A > B:
        A, B = B, A
    if A > C:
        A, C = C, A
    if B > C:
        B, C = C, B
    print(f"Valores em ordem ascendente: {A}, {B}, {C}")
    
ordenar_tres_valores(A,B,C)
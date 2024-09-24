notas = []
total_notas = 0
contador_notas = 0

while True:
    nota = float(input("Digite a nota do aluno (ou 0 para terminar): "))
    if nota == 0:
        break
    notas += [nota]  
    total_notas += nota
    contador_notas += 1

if contador_notas == 0:
    print("Nenhuma nota foi registrada.")
else:
    media = total_notas / contador_notas
    print(f"Média das notas: {media:.2f}")
    
    alunos_acima_media = 0
    for nota in notas:
        if nota > 7:
            alunos_acima_media += 1
    
    print(f"Quantidade de alunos com notas acima de 7: {alunos_acima_media}")

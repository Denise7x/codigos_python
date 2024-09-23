def calcular_calorias(atividade, tempo):
    if atividade == "caminhada":
        return tempo * 5
    elif atividade == "corrida":
        return tempo * 10
    elif atividade == "ciclismo":
        return tempo * 8
   
atividade = input("Digite qual atividade você pratica (caminhada, corrida, ciclismo): ")
tempo = int(input("Digite o tempo em minutos: "))

calorias = calcular_calorias(atividade, tempo)

print(f"Você queimou {calorias} calorias durante a atividade de {atividade}.")


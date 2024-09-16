horas = float(input("Digite a quantidade de horas trabalhadas: "))
valorH = float(input("Digite o valor por hora: R$"))

if horas < 40:
  salario = horas * 0.50

print(f"Você recebeu um bônus de 50% e seu salário é de {valorH}")  
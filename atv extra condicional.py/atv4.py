salario = int(input ("Informe o salário do funcionário: R$" ))

if salario <= 1900:
    imposto = 0

elif salario <= 2800:
    imposto = salario * 0.075


elif salario <= 3700:
    imposto = salario * 0.15

else: imposto = salario * 0.225

print(f"O imposto de renda para um salário de R$ {salario:.2f} é R$ {imposto:.2f}.")
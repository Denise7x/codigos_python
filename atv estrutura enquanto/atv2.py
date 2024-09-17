from datetime import datetime
ano_atual = datetime.now().year

while True:
    try:
        ano_nascimento = int(input("Informe o seu ano de nascimento: "))
        idade = ano_atual - ano_nascimento
        
        if idade >= 18:
            print("Inscrição realizada com sucesso!")
            break
        else:
            print("Você precisa ter 18 anos ou mais para se inscrever. Tente novamente.")
    
    except ValueError:
        print("Entrada inválida. Por favor, informe um ano válido.")
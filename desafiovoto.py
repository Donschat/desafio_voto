import datetime

def voto():
    if idade >= 18:
        print(f'Com {idade} anos seu voto é obrigatório')
    elif idade < 18 and idade >= 16:
        print(f'Com {idade} anos seu voto não é obrigatório')
    elif idade > 65:
        print(f'Com {idade} anos seu voto é opcional')
    else:
        print(f'Com {idade} anos você não pode votar')


hoje = datetime.date.today().year
nasc = int(input('Digite a sua data de nascimento: '))
idade = (hoje - nasc)
voto()
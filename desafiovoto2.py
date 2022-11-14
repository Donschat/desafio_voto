def voto(idade):
    if idade>=18:
        print('você tem que votar')
    elif 16 <= idade < 18:
        print('você não é obrigado a votar')
    else:
        print('você não pode votar')

voto(int(input('digite aqui a sua idade: ')))

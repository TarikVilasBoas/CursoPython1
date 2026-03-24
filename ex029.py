veloc = float(input('Qual a velocidade do carro? '))

if veloc <= 80:
    print('velocidade permitida!')
else:
    mult = float(veloc-80)*7
    print('Acima da velocidade permitida!')
    print('Multa no valor de R${:.2f}'.format(mult))

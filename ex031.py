km = int(input('Quantos Km tem sua viagem? '))

if km <= 200:
    calc = float(km * 0.50)
else:
    calc = float(km*0.45)
print('O valor de sua passagem sera R${:.2f}'.format(calc))
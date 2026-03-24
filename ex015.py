

d = int(input('Quantos dias ficou alugado? '))
km = float(input('Quantos km foram rodados? '))

dsum = d * 60
kmsum = km * 0.15

print('O valor do aluguel é de R${:.2f}'.format(dsum+kmsum))
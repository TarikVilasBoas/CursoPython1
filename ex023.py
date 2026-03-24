'''num = input('Digite um numero: ')

print('Unidade: ',num[3])
print('Dezena: ',num[2])
print('Centena: ',num[1])
print('Milhar: ',num[0])'''

#correção

num = int(input('Digite o numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analizando o numero {}'.format(num))


print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))






print('Digite 3 retas:')

r1 = float(input('R1: '))
r2 = float(input('R2: '))
r3 = float(input('R3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possivel formar um triangulo!')
else:
    print('Não é possivel formar o triangulo!')

if r1 == r2 and r1 == r3 and r2 == r3:
    print('Equilatero')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Isosceles')
else:
    print('Escaleno')
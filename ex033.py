n1= int(input('Primeiro: '))
n2= int(input('Segundo: '))
n3= int(input('Terceiro: '))

if n1 >= n2 and n1 >= n3:
    print('O numero maior é {}'.format(n1))
elif n2 >= n1 and n2 >= n3:
    print('O numero maior é {}'.format(n2))
else:
    print('O numero maior é {}'.format(n3))

if n1 <= n2 and n1 <= n3:
    print('O numero menor é {}'.format(n1))
elif n2 <= n1 and n2 <= n3:
    print('Menor numero é {}'.format(n2))
else:
    print('O menor numero é o {}'.format(n3))

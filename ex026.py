frase = str(input('Digite uma frase: ').strip().upper())

print('Letra A aparece {} vezes na frase'.format(frase.count('A')))
print('Primeira letra A apareceu na posição: {}'.format(frase.find('A')))
print('Posição ultimo A: {}'.format(frase.rfind('A')))


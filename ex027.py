nome = str(input('Digite o nome: ')).strip()

print('Primeiro nome: {}'.format(nome.split()[0]))
print('Ultimo nome: {}'.format(nome.split()[-1]))
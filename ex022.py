frase = str(input('Digite um nome: ')).strip() #remove espaços no inicio e fim

print('Seu nome com letras maiusculas: ',frase.upper())
print('Seu nome com letras minusculas: ',frase.lower())
print('Seu nome tem ao todo {} Letras'.format(len(frase.replace(' ',''))))
name = frase.split()[0]
print('Seu primeiro nome é {} e tem {} letras'.format(frase.split()[0], len(name)))


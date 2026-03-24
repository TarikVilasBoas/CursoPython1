

thing = input('Write anything: ')

print('The primitive type is: ',type(thing))
print('So tem espaços? {}'.format(thing.isspace()))
print('É um numero? {}'.format(thing.isnumeric()))
print('É alfabetico? {}' .format(thing.isalpha()))
print('È Alfanumerico? {}'.format(thing.isalnum()))
print('É maiuscula? {}'.format(thing.isupper()))
print('É minuscula? {}'.format(thing.islower()))
print('É Capitalizada? {}'.format(thing.istitle()))


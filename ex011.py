

a = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))

area = a * l
tint = area / 2

print('Sua parede tem {}x{} de dimensoes que soma uma área de {:.3f}m2'.format(a,l,area))
print('Para pintar é nescessario {}Lt de tinta'.format(tint))
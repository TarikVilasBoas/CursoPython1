import random
from time import sleep

w = random.randint(0,5)
print('--**--' * 20)
print('Vou pensar em um numero de 0 a 5... Tente adivinhar! ')
print('--**--'*20)
n = int(input('Qual numero pensei? '))
print('Processando...')
sleep(2)

if w == n :
    print('Voce acertou')
else :
    print('Errado, pensei no numero {} e voce digitou {}'.format(w,n))


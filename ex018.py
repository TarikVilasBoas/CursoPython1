import math
angulo = float(input('Digite o grau: '))

rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print('O angulo de {} graus tem o seno de {:.2f} \n O cosseno {:.2f} \n e tangente {:.2f}'.format(angulo,seno,cosseno,tangente))
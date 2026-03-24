from datetime import date
ano = int(input('Qual o ano quer analisar? Use 0 para o ano atual. '))

if ano == 0:
    ano = date.today().year   #pega o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano Bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
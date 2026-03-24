salary = float(input('Qual seu salario atual? '))
base = float(1250.0)
if salary > base:
    total = salary +(salary / 100 * 10)
    print('O seu salario tera um aumento de 10% e sera ajustado para R${:.2f}'.format(total))
else:
    total = salary +(salary / 100 * 15)
    print('Seu salario tera ajuste de 15% e passara a ser R${:.2f}'.format(total))




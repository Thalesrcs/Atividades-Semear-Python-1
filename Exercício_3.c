casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? ')) 
anos = int(input('Em quantos anos será o pagamento? '))

if (casa / (anos * 12)) > (salario * 0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo aceito!')

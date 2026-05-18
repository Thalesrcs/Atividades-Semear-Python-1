dias = float(input('Quantos dias? '))
km = float(input('Quantos km? '))
preco = (dias * 60) + (km * 0.15)
print('O preço a pagar é de R${:.2f}'.format(preco))

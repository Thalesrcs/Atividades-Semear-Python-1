num = int(input('Qual o valor a ser sacado (número inteiro)? '))
um = num % 10 
cinquenta = num // 50
vinte = (num - (cinquenta * 50)) // 20
dez = (num - ((cinquenta * 50) + (vinte * 20))) // 10

print(cinquenta, 'notas de 50')
print(vinte, 'notas de 20')
print(dez, 'notas de 10')
print(um, 'notas de 1')

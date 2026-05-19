soma = 0
for i in range(0, 5, 1):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma = soma + num
print('A soma dos pares é: ', soma)

def maior(num, m):
    vmaior = num[0]
    for i in range(1, m):
        if num[i] > vmaior:
            vmaior = num[i]
    return vmaior

quant = int(input('Qual a quantidade de valores? '))
vet = []
for i in range(1, quant + 1, 1):
    vet.append(int(input('valor: ')))
print('O maior valor é: ', maior(vet, quant))
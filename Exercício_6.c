razão = int(input('Qual a razão da PA: '))
inicio = int(input('Qual o termo inicial? '))
for  i in range(inicio, razão * 10 + inicio, razão):
    print(i)
else:
    resposta = str(input('Você deseja obter mais valores? '))
if resposta == 'sim':
    quantos = int(input('Quantos? '))
    for i in range(razão * 10 + inicio, razão * (10 + quantos) + inicio, razão):
        print(i)

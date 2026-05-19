soma = 0
velhonome = 'a'
velho = 0
novas = 0


for i in range(0, 4, 1):
    nome = str(input('Qual o nome? '))
    idade = int(input('Qual a idade ? '))
    sexo = str(input('Qual o sexo (M ou F)? '))
    soma = soma + idade
    if sexo == 'M':
        if idade > velho:
            velhonome = nome
            velho = idade
    else:
        if idade < 20:
            novas = novas + 1
print('A média de idade é: ', soma / 4)
print(velhonome, 'é o homem mais velho')
print('Existem', novas,'mulheres com menos de 20 anos')
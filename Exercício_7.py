mulheresnovas = 0
homens = 0
mais = 0
resposta = 'sim'

while resposta != 'nao':
        idade = int(input('Qual a idade? '))
        sexo = str(input('Qual o sexo (M ou F)?'))
        if idade > 18:
            mais = mais + 1
        if sexo == 'M':
            homens = homens + 1
        if sexo == 'F':
            if idade < 20:
                mulheresnovas = mulheresnovas + 1
        resposta = str(input('Quer continuar? '))
print(mais, 'pessoas tem mais de 18 anos')
print(homens, 'homens foram cadastrados')
print(mulheresnovas, 'mulheres tem menos de 20 anos')

l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))
if (l1 + l2) > l3 & (l2 + l3) > l1 & (l1 + l3) > l2:
    if l1 != l2 != l3:
        print('O triângulo é escaleno!')
    elif l1 == l2 & l2 != l3 || l1 == l3 & l3 != l2 || l2 == l3 & l2 != l1:
        print('O triângulo é isósceles!')
    elif l1 == l2 == l3:
        print('O triângulo é equilátero!')
else: 
    print('Não é possível formar triângulo!')

def eh_palindromo_tabela(frase):
    frase = frase.lower()
    frase_limpa = frase.replace(" ", "")
    frase_invertida = ""
    indice = len(frase_limpa) - 1
    
    while indice >= 0:
        frase_invertida += frase_limpa[indice]
        indice -= 1
        
    return frase_limpa == frase_invertida

texto = input("Digite uma frase: ")

if eh_palindromo_tabela(texto):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
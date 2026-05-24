lista = []
lista.append(int(input("V1: ")))
lista.append(int(input("V2: ")))
lista.append(int(input("V3: ")))
lista.append(int(input("V4: ")))
lista.append(int(input("V5: ")))
print("O valor máximo foi:", max(lista),"e sua posição é:", lista.index(max(lista)))
print("O valor mínimo foi:", min(lista),"e sua posição é:", lista.index(min(lista)))
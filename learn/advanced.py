############# list comprehension #############
x = [1, 2, 3, 4, 5]

"""
y = []
for i in x:
    y.append(i**2)
"""
y = [i**2 for i in x] #tudo em uma só linha

print(x)
print(y)

z = [i for i in x if i % 2 == 1] #somente numeros impares
print (z)


############# enumerate #############
lista = ["Andre", "Mari", "Gabriel"]

for i, nome in enumerate(lista):
    print("indice:", i, "- valor:", nome)

    
############# map #############
def dobro(x):
    return x*2

print(dobro(3))

valor = [1, 2, 3, 4, 5]
valor_dobrado = map(dobro, valor) #mapeia a lista e aplica a função em cada item
valor_dobrado = list(valor_dobrado) #transforma o map em lista
print (valor_dobrado)

    
############# reduce #############
from functools import reduce

def soma(x, y):
    return x + y

lista1 = [1, 3, 5, 8, 10, 20]

somados = reduce(soma, lista1) #aplica a funçãode froma cumulativa item a item
print(somados)

    
############# zip #############
lista_a = [1, 2, 3, 4, 5]
lista_b = ["abacate", "bola", "cachorro", "dado", "elefante"]
lista_c = ["R$ 5.00","R$ 42.00", "R$ 580.00", "R$ 3.00", "R$ 5940.00",  ]

for numero, nome, valor in zip (lista_a, lista_b, lista_c):
    print (numero, nome, valor)
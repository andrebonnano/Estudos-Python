# -*- coding: utf-8 -*-

# Comentários do código
print("Hello world - Olá mundo")

"""
Comentários
em
blocos
"""

############### Operadores ###############
# soma
print(2+2)

# subtração
print(5-2)

# multiplicação
print(2*2)

# exponencial
print(3**2)

# modulo
print(10%3)


############### Variáveis ###############
mensagem = "Olá mundo"
print(mensagem)

var1 = 1  #inteiro
var2 = 1.1  #float
var3 = "texto"  #string
var4 = False  #boolean

matrix1 = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
print (matrix1[0][0])

############### Operadores relacionais ###############
x = 2
y = 3
soma = x + y

print( x == y)
print( x != y)
print( x > y)
print( x < y)
print( x <= y)


############### Operadores lógicos ###############
print ( x > y and soma > x)
print ( x > y or soma > x)


############### Condicionais ###############
if x > y:
    print("X é maior")
elif x == y:
    print("São iguais")
else:
    print("Y é maior")


############### Repetições ###############
count = 5
while x < count:
    x += 1
    print (x)

lista = [1, "teste", 3, 12.8, "---------------"] #matriz
for i in lista:
    print (i)

for i in range (10, 20, 2):  #(start, stop, step)
    print (i)
    
    
############### Strings ###############
a = "Andre"
b = "Bonnano"
nome = a + " " + b
print(nome)

tamanho = len(nome) #quantidade de caracteres
print(tamanho)
print (nome[0] + nome[6])
print (nome[0:3])  #(inicio, fim)

primeiroNome = nome.split(" ")[0]
sobrenome = nome.split(" ")[1]
print(primeiroNome)
print(sobrenome)

print(nome.lower())
print(nome.upper())
print(nome.strip()) #remove espaços e enters no final da string
print(nome.split(" "))

nomeCompleto = "André Parente e Silva Bonnano"
print(nomeCompleto.find("Silva"))
print(nomeCompleto.replace(" e ", " E "))

    
############### Functions ###############
def NomeDaFuncao(parametros):
    comandos = "comandos"
    return "Retorno da função"
    
def Soma (a, b):
    result = a + b
    return result

print(Soma(3, 6))

    
############### Files ###############
arquivo = open("arquivo.txt", "r")

linhas = arquivo.readlines()

for linha in linhas:
    print (linha)

newFile = open("arquivo2.txt", "w")
newFile.write("Este e o novo arquivo\n")
newFile.close()


############### Lists ###############
minha_lista = ["banana", "laranja", "melancia"]
minha_lista2 = ["mamao", "abacaxi", "laranja"]
minha_lista3 = [1, 3, 5, "12", True, "texto"]
minha_lista_4 = [124, 345, 5, 72, 46, 6, 7, 3, 1 ,0]

print(minha_lista[1])

tamanho = len(minha_lista3)
print(tamanho)

minha_lista.append("limao")
print (minha_lista)

if "abacaxi" in minha_lista2:
    print("Abacaxi esta na lista")
else:
    print("Está faltando o abacaxi")
    
del(minha_lista3[3:5])
print(minha_lista3)

minha_lista_4.sort()
print (minha_lista_4)

for item in minha_lista2:
    if not item in minha_lista:
        minha_lista.append(item)
   
minha_lista.sort() 
print (minha_lista)


############### Dictionary ###############

meus_dados = {"nome":"Andre", "sobrenome":"Bonnano", "celular":"(11)96621-1221"}
print(meus_dados["nome"])

for chave in meus_dados:
    print(chave + " - " + meus_dados[chave])


############### Numeros aleatórios ###############
import random

numero = random.randint(0, 100)
print(numero)

lista1 = [3, 67, 32, 89]
numero2 = random.choice(lista1)
print(numero2)


############### Exceptions - try ###############
a = 2
b = 0
try:
    print(a/b)
except:
    print("Não é permitido divisão por zero")
    
print (a/a)
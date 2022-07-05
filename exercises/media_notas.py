#variaveis iniciais
notas = []
n = 0
media = 0

#entradas
qtd_notas = int(input("Quantas notas você deseja inserir? "))

while n < qtd_notas:
    nota = int(input("nota " + str(n + 1) + ": "))
    notas.append(nota)
    n += 1

for x in notas:
    media += x

media = media / qtd_notas

if media >= 6:
    print("Parabéns, você está aprovado com média " + str(media) + "!")
else:
    print("Sua média é de " + str(media) + ", infelizmente não é o suficiente.")
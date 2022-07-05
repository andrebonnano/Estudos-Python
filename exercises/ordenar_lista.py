#variaveis iniciais
itens = []
n = 0

#entradas
qtd_itens = int(input("Quantos itens você deseja inserir? "))

while n < qtd_itens:
    item = int(input("item " + str(n + 1) + ": "))
    itens.append(item)
    n += 1

itens.sort()
print(itens)   
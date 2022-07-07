print("VISUALIZAÇÃO DE DADOS COM PYTHON")

## Graficos
print("================== Graficos ==================")

import matplotlib.pyplot as plt


## Grafico de linha
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 5, 3, 4, 1]
#titulos
plt.title("Grafico de linhas em python")
plt.xlabel("linha horizontal")
plt.ylabel("linha vertical")
#montagem
plt.plot(x, y)
#exibição
plt.show()


## Grafico de barras
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 5, 3, 4, 1]
#titulos
titulo = "Gráfico de barras"
eixoX = "Eixo X"
eixoY = "Eixo Y"
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)
#montagem
plt.bar(x,y) #aqui define que é grafico de barra
#exibição
plt.show()


## Grafico de barras - comparando dados
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]
x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]
#titulos
titulo = "Gráfico de barras 2"
eixoX = "Eixo X"
eixoY = "Eixo Y"
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)
#montagem
plt.bar(x1,y1, label = "grupo1")
plt.bar(x2,y2, label = "grupo2")
plt.legend()
#exibição
plt.show()


## Grafico de barras - comparando dados
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]
z1 = [200, 50, 1000, 330, 100]
#titulos
titulo = "Scatterplot - Gráfico de pontos"
eixoX = "Eixo X"
eixoY = "Eixo Y"
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)
#montagem
plt.scatter(x1, y1, label = "meus pontos", color="red", marker=".", s=z1)
plt.plot(x1, y1, label = "linha", color="#cecece", linestyle="--")
plt.legend()
#exibição
plt.savefig("grafico4.png", dpi=300)
plt.savefig("grafico4.pdf")
plt.show()
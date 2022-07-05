n1 = int(input("Digite o primeiro numero do cálculo: "))
op = input("Digite o operador matemático ( + - * / % **): ")
n2 = int(input("Digite o segundo numero do cálculo: "))

def switch(case):
    if op == "-":
        return n1 - n2
    elif op == "+":
        return n1 + n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2
    elif op == "%":
        return n1 % n2
    elif op == "**":
        return n1 ** n2

result = switch(op)
print(result)

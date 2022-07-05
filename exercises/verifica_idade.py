data_nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2022 - data_nascimento

if idade >= 18:
    print("Parabéns, você já tem " + str(idade) + ", é maior de idade e pode tirar habilitação!")
else:
    print("Infelizmente você ainda tem " + str(idade) + " anos e não pode tirar habilitação")
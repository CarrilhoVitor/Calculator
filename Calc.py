n1 = float(input("Digite um Número: "))
n2 = float(input("Digite outro Número: "))
operation = input("Escolha a operação *, /, + ou - ")
result = 0

if operation == "*":
    result = n1 * n2
    print("O resultado é: ", result)
elif operation == "/":
    result = n1 / n2
    print("O resultado é: ", result)
elif operation == "+":
    result = n1 + n2
    print("O resultado é: ", result)
else:
    result = n1 - n2 
    print("O resultado é: ", result)

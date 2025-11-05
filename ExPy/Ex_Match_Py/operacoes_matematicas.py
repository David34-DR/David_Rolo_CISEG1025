
operacao = input("Digite a operção desejada: ")
print("1 - Soma")
print("2 - Subtraçao")
print("3 - Multiplicação")
print("4 - Divisão")
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

match operacao:
    case "1":
        print(num1 + num2)
    case "2":
        print(num1 - num2)
    case "3":
        print(num1 * num2)
    case "4":
        print(num1 / num2)
    case _:
        print("Operaçao invalida")
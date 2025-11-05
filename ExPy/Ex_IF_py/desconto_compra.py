
nome = input("Digite o seu nome: ")
valor = int(input("Digite o valor da sua compra: "))
des = 0
tot = 0

if valor < 200:
    des = valor * 10/100
    tot = valor - des
    print("Nome: ",nome)
    print("Compra: ",valor)
    print("Desconto: ",des)
    print("Total: ",tot)
elif valor >= 200 or valor <= 500:
    des = valor * 15/100
    tot = valor - des
    print("Nome: ",nome)
    print("Compra: ",valor)
    print("Desconto: ",des)
    print("Total: ",tot)
elif valor > 500:
    des = valor * 20/100
    tot = valor - des
    print("Nome: ",nome)
    print("Compra: ",valor)
    print("Desconto: ",des)
    print("Total: ",tot)

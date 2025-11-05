
nome = input("Nome: ")
idade = int(input("Digite a sua idade: "))
tipo = input("Cargo: ")

if idade < 18:
    print("Utilizador menor de idade")
elif tipo == "admin":
    print("Administrador")
else:
    print("Utilizador comum")

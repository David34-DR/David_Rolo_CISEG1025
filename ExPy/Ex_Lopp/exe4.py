numero = int(input("Digite um número inteiro: "))

divisores = 0

for teste in range(1, numero + 1):
    if numero % teste == 0:
        divisores += 1

if divisores == 2:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

num = int(input("Digite um número inteiro para ver quantos divisores tem: "))

divisores = 0
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1
print(f"O número {num} tem {divisores} divisores.")
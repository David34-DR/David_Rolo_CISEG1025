
pares = 0
impares = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1} número: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
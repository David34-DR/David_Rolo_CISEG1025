total = 0
contador = 0

while contador < 30:
    entrada = input(f"Digite o número: {contador + 1}de 30: ")
    
    if not entrada.isdigit():
        print("Entrada inválida! Digite um número inteiro.")
        continue 
    num = int(entrada)
    
    if num < 1 or num > 50:
        print("Número fora do intervalo de 1 a 50. Tente novamente.")
    elif num % 2 != 0:
        print("Número ímpar. Digite um número par.")
    else:
        total += num
        contador += 1

media = total / 30
print(f"A média e: {media}")

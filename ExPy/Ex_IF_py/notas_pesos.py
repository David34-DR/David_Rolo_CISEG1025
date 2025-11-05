
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))

peso1 = 2
peso2 = 3
peso3 = 5

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

print(f"Média: {media}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
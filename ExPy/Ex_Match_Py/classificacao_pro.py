
categoria = input("Digite a categoria: ")
preço = int(input("Digite agora o preço: "))

if categoria == "eletronico" and preço > 1000:
    print("Produto de luxo")
elif categoria == "eletronico" and preço <= 1000:
    print("Produto comum")
elif categoria == "alimento":
    print("Produto alimentar")
else:
    print("Categoria desconhecida")
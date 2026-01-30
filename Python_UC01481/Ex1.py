
nome = input("Introduz o teu nome completo: ")

def maiuscula(c):
    return 65 <= ord(c) <= 90   # A-Z

def minuscula(c):
    return 97 <= ord(c) <= 122  # a-z

def espaco(c):
    return ord(c) == 32    

for i in range(len(nome)):
    c = nome[i]
    codigo = ord(c)
    
    if not (maiuscula(c) or minuscula(c) or espaco(c)):
        print("Nome inválido: contém caracteres não permitidos.")
        exit()
  
    if i == 0:
        if not maiuscula(c):
            print("Nome inválido: primeira letra deve ser maiúscula.")
            exit()
   
    if i > 0 and nome[i-1] == " ":
        if not maiuscula(c):
            print("Nome inválido: letra após espaço deve ser maiúscula.")
            exit()

    if i > 0 and nome[i-1] != " ":
        if maiuscula(c):
            print("Nome inválido: uso incorreto de maiúsculas.")
            exit()

print("Nome válido!")
#aaa

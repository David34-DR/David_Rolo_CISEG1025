
nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]

def comparar_ascii(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2):
        if ord(s1[i]) < ord(s2[i]):
            return -1
        elif ord(s1[i]) > ord(s2[i]):
            return 1
        i += 1

    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1
    else:
        return 0

def ordenar_nomes(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            nome1 = lista[j].split(" ")
            nome2 = lista[j+1].split(" ")

            primeiro1 = nome1[0]
            apelido1 = nome1[1]

            primeiro2 = nome2[0]
            apelido2 = nome2[1]

            cmp_primeiro = comparar_ascii(primeiro1, primeiro2)

            trocar = False

            if cmp_primeiro > 0:
                trocar = True
            elif cmp_primeiro == 0:

                cmp_apelido = comparar_ascii(apelido1, apelido2)
                if cmp_apelido > 0:
                    trocar = True

            if trocar:
                lista[j], lista[j+1] = lista[j+1], lista[j]

ordenar_nomes(nomes)

print("Lista ordenada:")
for nome in nomes:
    print(nome)
#aaaaaaaa
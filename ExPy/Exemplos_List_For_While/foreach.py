
listanum=[1,6,3,9,4,8,3,5]

# foeach com variavel nas posiçoes todas da lista
for posicaolista in listanum:
    print(posicaolista)


print("tamanho total da lista",len(listanum))

# foreach para indexar ou criar numeros de qualquer range
for i in range(len(listanum)):
    print(listanum[i])

print("range a começar 1 e acabar em 19")

for i in range(1,20):
    print(i)

print("range a pular de 3 em 3")

for i in range(1,20,3):
    print(i)
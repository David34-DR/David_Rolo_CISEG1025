
listanum=[1,6,3,9,4,8,3]
# index = 0,1,2,3,4,5,6

flag=True

i=0 # itenerador ( numero do index )

print("tamanho total da lista",len(listanum))

while i<len(listanum):
    print("elemento : ", listanum[i] , "posiçao index", i)
    i+=1

it=1
while it<=20:
    print(it) 
    it+=1

it=1
while it<=20:
    print(it) 
    if it==10:
        break
    it+=1

it=0
while it<=20:
    it+=1
    if it==10:
        continue
    print(it) 

conta=0
while flag:
    conta+=1
    if conta==20:
        flag=False
    print("conta=", conta , "flag =",flag)
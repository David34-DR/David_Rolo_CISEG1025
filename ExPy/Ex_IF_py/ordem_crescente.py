
num1 = int(input("Digite o 1 numero: "))
num2 = int(input("Digite o 2 numero: "))
num3 = int(input("Digite o 3 numero: "))

if num1 > num2 and num2 > num3:
    print("Crescente: ", num3, num2, num1)
    print("Decrescente: ",num1, num2, num3)
elif num1 > num3 and num3 > num2:
     print("Crescente: ", num2, num3, num1)
     print("Decrescente: " ,num1, num3, num2)
elif num2 > num1 and num1 > num3:
      print("Crescente: " ,num3, num1, num2)
      print("Decrescente: " , num2, num1, num3)
elif num2 > num3 and num3 > num1:
      print("Crescente: " , num1, num3, num2)
      print("Decrescente: " , num2, num3, num1)
elif num3 > num2 and num2 > num1:
      print("Crescente: " , num1, num2, num3)
      print("Decrescente: " , num3, num2, num1)
elif num3 > num1 and num1 > num2:
      print("Crescente: " , num2, num1, num3)
      print("Decrescente: " ,num3, num1, num2) 
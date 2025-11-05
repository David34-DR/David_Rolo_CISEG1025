
saldo = int(input("Digite o saldo do seu banco: "))
cheque = int(input("Digite a quantia do cheque: "))
total = 0

if saldo >= cheque:
    total = saldo - cheque
    print("Cheque descontado!! Saldo:", total)
else:
    print("Nao e possivel descontar saldo insufeciente")
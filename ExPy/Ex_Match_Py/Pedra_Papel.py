
jogador1 = input("Digite o que quer: ")
jogador2 = input("Digite o que quer: ")

match (jogador1,jogador2):
    case ("pedra","tesoura"):
        print("Jogador 1 ganhou")
    case ("tesoura","pedra"):
        print("Jogador 2 ganhou")
    case ("tesoura","papel"):
        print("Jogador 1 ganhou")
    case ("papel","tesoura"):
        print("Jogador 2 ganhou")
    case ("papel","pedra"):
        print("Jogador 1 ganhou")
    case ("pedra","papel"):
        print("Jogador 2 ganhou")
    case _:
        print("Empate")
    

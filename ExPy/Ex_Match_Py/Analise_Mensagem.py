
mensagem = input("Digite uma mensagem: ")

match mensagem:
    case "ola" | "bom dia":
        print("Saudação")
    case _ if mensagem.endswith("?"):
        print("Pergunta")
    case _ if "adeus" in mensagem or "tchau" in mensagem:
        print("Despedida")
    case _:
        print("Mensagem Normal")
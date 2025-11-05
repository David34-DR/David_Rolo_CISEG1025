
metodo = input("Metodo: ")
conteudo = input("Conteudo: ")

match metodo:
    case "GET":
        print("Requisição GET recebida")
    case "POST":
        if metodo == "POST" and conteudo == "":
         print("Requisição POST sem dados")
        else:
         print("Requisição POST com dados validos")
    case _:
      print("Metodo nao suportado")
        
        
       



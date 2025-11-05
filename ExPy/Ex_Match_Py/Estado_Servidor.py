
status = input("Status: ")
tempo_resposta = int(input("Digite o tempo resposta: "))

if status == "ok" and tempo_resposta <= 200:
    print("Servidor ativo")
elif status == "ok" and tempo_resposta >= 200:
    print("Servidor lento")
elif status == "erro":
    print("Servidor indisponível")
else:
    print("Estado desconhecido")
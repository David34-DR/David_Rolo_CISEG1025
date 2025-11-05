
seg_t = int(input("Digite os segundos: "))

horas = seg_t // 3600
resto = seg_t % 3600
min = resto //60
seg = resto %60

print(horas, "horas", min,"minuto",seg,"segundos")

notas = []

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i+1} (0 a 20): "))
    
    notas.append(nota)

media = sum(notas) / len(notas)

acima_da_media = 0
for nota in notas:
    if nota >= media:
        acima_da_media += 1

print(f"\nMédia da turma: {media}")
print(f"Número de alunos com nota igual ou acima da média: {acima_da_media}")
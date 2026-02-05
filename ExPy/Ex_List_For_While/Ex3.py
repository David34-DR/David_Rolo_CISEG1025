
notas = []

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i+1} (0 a 20): "))
    
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"\nMédia dos alunos: {media}")

print("Bárbara Helena Preto Brandino \n RA:1051392421024 \n Curso: DSM")
print()
maior_nota = 0
notas = []

# Coleta as notas dos alunos
for contador in range(1, 6):
    nota = float(input(f"Digite a nota do aluno {contador}: "))
    notas.append(nota)  # Adiciona a nota à lista
    if nota > maior_nota:
        maior_nota = nota  # Atualiza a maior nota se necessário

# Exibe as notas e a maior nota
print("As notas dos alunos foram:", notas)
print("A maior nota da turma é:", maior_nota)




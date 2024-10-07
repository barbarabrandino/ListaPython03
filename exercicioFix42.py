print("Bárbara Helena Preto Brandino \n RA:1051392421024 \n Curso: DSM")
print()
contador = 1
maior_nota = 0
nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
nota5 = 0
while contador <= 5:
    nota = float(input(f"Digite a nota do aluno : {contador}"))
    if contador == 1:
        nota1 = nota
    elif contador == 2:
        nota2 = nota
    elif contador == 3:
        nota3 = nota
    elif contador == 4:
        nota4 = nota
    elif contador == 5:
        nota5 = nota
    if nota > maior_nota:
        maior_nota = nota
    contador += 1
print("As notas dos alunos foram:", nota1, nota2, nota3, nota4, nota5)
print("A maior nota da turma é:", maior_nota)



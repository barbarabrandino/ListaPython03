print("Bárbara Helena Preto Brandino \n RA:1051392421024 \n Curso: DSM")
print()

# Senha para acesso do professor
senha_professor = "fatec2024"  

# Autenticação do professor
senha_informada = input("Digite a senha do professor: ")

if senha_informada == senha_professor:
    # Acesso permitido, solicitar dados do aluno
    nome = input("Digite o nome do aluno: ")
    
    # Solicita as notas das avaliações
    nota1 = float(input("Digite a nota da primeira avaliação: "))
    nota2 = float(input("Digite a nota da segunda avaliação: "))
    
    # Calcula a média de aproveitamento
    media = (nota1 + nota2) / 2
    
    # Determina o conceito do aluno com base na média
    if media >= 9:
        conceito = "A"
    elif media >= 7.5:
        conceito = "B"
    elif media >= 6:
        conceito = "C"
    elif media >= 4:
        conceito = "D"
    else:
        conceito = "E"

    # Exibe o resultado
    print("\nNome do aluno:", nome)
    print("Média de aproveitamento:", media) 
    print("Conceito:", conceito)
else:
    # Acesso negado
    print("Acesso negado. Senha incorreta.")

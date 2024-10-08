print("Bárbara Helena Preto Brandino \n RA:1051392421024 \n Curso: DSM")
print()
# Habilitar o teclado para que o usuário possa colocar o nome
nome=str(input("Digite seu nome:"))
# Habilitar o teclado para que o usuário possa digitar o sálario "velho"
salario= float(input("Digite seu salário em R$:"))
# Definir a função de calcular o acrescimo
def calcular_acrescimo (salario):
    if salario <= 1500:
        acrescimo= 0.20
    elif salario >1500 < 2500:
        acrescimo= 0.10
    else:
       acrescimo= 0
       # Calcula o novo salário
    novo_sal= (salario * acrescimo)+ salario
    return novo_sal
novo_sal=calcular_acrescimo(salario) 
# Exibe o resultado
print("O seu novo salário em R$ é:", novo_sal)




print("Bárbara Helena Preto Brandino \n RA:1051392421024 \n Curso: DSM")
print()
nome=str(input("Digite seu nome:"))
salario= float(input("Digite seu salário em R$:"))
def calcular_acrescimo (salario):
    if salario <= 1500:
        acrescimo= 0.20
    elif salario >1500 < 2500:
        acrescimo= 0.10
    else:
       acrescimo= 0
    novo_sal= (salario * acrescimo)+ salario
    return novo_sal
novo_sal=calcular_acrescimo(salario) 
print("O seu novo salário em R$ é:", novo_sal)




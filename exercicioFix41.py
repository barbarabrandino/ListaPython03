print("Bárbara Helena Preto Brandino \n RA:1051392421024 \n Curso: DSM")
print()
# Função para calcular o fatorial de um número inteiro
def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial
# Habilita o tecelado para que p usuári possar escrever um número inteiro
numero = int(input("Digite um número inteiro positivo: "))
if numero >= 0:
    resultado = calcular_fatorial(numero)
    print("O fatorial de", numero ,"é",resultado)
else:
    print("Por favor, digite um número inteiro positivo.")

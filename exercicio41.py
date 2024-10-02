print("Bárbara Helena Preto Brandino \n RA:1051392421024 \n Curso: DSM")
print()
num=int(input("Digite um número inteiro positivo para descobrir seu fatorial:"))
def fatorial(n):
    resultado=1 
    for i in range(1,n+1):
        resultado*=i
        return resultado
    if num < 0:
        print("Por favor digite outro número que seja inteiro e positivo!")
    else:
     print("O fatorial é", resultado)
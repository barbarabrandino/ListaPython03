print("Bárbara Helena Preto Brandino \n RA:1051392421024 \n Curso: DSM")
print()
# Solicita dados do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))
sexo = input("Digite seu sexo (masculino/feminino): ").lower()

# Calcula o  IMC
imc = peso / (altura ** 2)

# Calcula o peso ideal
if sexo == 'masculino':
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

# Verifica se está no peso ideal
if abs(peso - peso_ideal) <= 5:  
    peso_status = "no seu peso ideal"
elif peso < peso_ideal:
    peso_status = "abaixo do peso ideal"
else:
    peso_status = "acima do peso ideal"

# Exibe resultados
print("\nSeu IMC é:", imc)
print("Seu peso ideal é:", peso_ideal, "kg.")
print("Você está", peso_status)

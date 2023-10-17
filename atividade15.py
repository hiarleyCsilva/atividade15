# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR
# Solicita ao usuário o comprimento de três retas
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verifica se as medidas satisfazem a desigualdade triangular
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("É possível formar um triângulo com essas medidas.")
else:
    print("Não é um triangulo.")

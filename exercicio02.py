#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n = float(input())

if n < 0:
    print("esse numero é negativo")
elif n >= 0:
    print("esse numero é positivo")
else:
    print("valor invalido")
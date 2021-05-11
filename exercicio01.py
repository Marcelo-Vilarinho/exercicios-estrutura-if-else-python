#Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input())
n2 = int(input())

if n1 > n2:
    print("o primeiro numero é maior")
elif n2 > n1:
    print("o segundo numero é maior")
else:
    print("numeros iguais")
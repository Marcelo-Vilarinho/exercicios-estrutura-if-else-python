#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, 
#caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes

A = float(input("digite o primeiro valor : "))
B = float(input("digite o segundo valor : "))
C = float(input("digite o terceiro valor "))


#verifica se as condiçoes para formar um triangulo estaõ certas
if A < (B + C) and B < (A + C) and C < (A + B):
    triangulo = True
    print('forma um triangulo')
else:
    triangulo = False
    print('não forma um triangulo')
 
#Triângulo Equilátero: três lados iguais   
if triangulo == True and  A == B and B == C:
    print('é um triangulo Equilátero')
    
#Triângulo Isósceles: quaisquer dois lados iguais    
if triangulo == True:
    if A == B or A == C or B == A or B == C or C == A or C == B:
        print('é um triangulo Isósceles')

#Triângulo Escaleno: três lados diferentes 
if triangulo == True and  A != B and B != C:
    print('é um triangulo Escaleno')
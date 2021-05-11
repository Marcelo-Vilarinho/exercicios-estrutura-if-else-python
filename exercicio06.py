#Faça um Programa que leia três números e mostre o maior deles. 

n1 = int(input()) 
n2 = int(input()) 
n3 = int(input()) 

if n1 > n2 and n1 > n3 : 
    print('primeiro numero maior: ', n1) 
elif n2 > n1 and n2 > n3: 
    print('segundo numero maior: ', n2) 
elif n3 > n1 and n3 > n2: 
    print('terceiro numero maior : ', n3) 
else: 
    print('digite apenas numeros')
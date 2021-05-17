#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
#e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

#Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0        A
  #Entre 7.5 e 9.0         B
  #Entre 6.0 e 7.5         C
  #Entre 4.0 e 6.0         D
  #Entre 4.0 e zero        E
 
nota1 = float(input("digite a primeira nota : "))
nota2 = float(input("digite a segunda nota : "))

print('\n')

media = (nota1 + nota2) / 2

if media >= 9.0 and media <= 10:
    print('Nota 1 :', nota1)
    print('Nota 2 : ', nota2)
    print('Media  : ', media)
    print('Conceito : A ')
    print('Aprovado !')
    

elif media >= 7.5 and media <= 9.0:
    print('Nota 1 : ', nota1)
    print('Nota 2 : ', nota2)
    print('Media  : ', media)
    print('Conceito : B ')
    print('Aprovado !')

elif media >= 6.0 and media <= 7.5:
    print('Nota 1 : ', nota1)
    print('Nota 2 : ', nota2)
    print('Media  : ', media)
    print('Conceito : C ')
    print('Aprovado !')

elif media >= 4.0 and media <= 6.0:
    print('Nota 1 : ', nota1)
    print('Nota 2 : ', nota2)
    print('Media  : ', media)
    print('Conceito : D ')
    print('reprovado !')

elif media <= 4.0 and media >= 0.0:
    print('Nota 1 : ', nota1)
    print('Nota 2 : ', nota2)
    print('Media  : ', media)
    print('Conceito : E ')
    print('reprovado !')
else:
    print('media : ', media)
    print('nota acima da media, aprovado !')
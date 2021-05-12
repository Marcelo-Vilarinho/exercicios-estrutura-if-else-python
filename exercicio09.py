#Faça um Programa que leia três números e mostre-os em ordem decrescente

primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('terceiro numero : '))

#comparando o maior numero e colocando na ordem decrescente
if primeiro > segundo > terceiro:
    print(primeiro,segundo,terceiro)
if primeiro > terceiro > segundo:
    print(primeiro,terceiro,segundo)
if segundo > primeiro > terceiro:
    print(segundo,primeiro,terceiro)
if segundo > terceiro > primeiro:
    print(segundo,terceiro,primeiro)
if terceiro > primeiro > segundo:
    print(terceiro,primeiro,segundo)
if terceiro > segundo > primeiro:
    print(terceiro,segundo,primeiro)

#comparando se alguns dos numeros tem valor iguais e colocando na ordem decrescente
if primeiro >= segundo >= terceiro:
    print(primeiro,segundo,terceiro)
if segundo >= primeiro >= terceiro:
    print(segundo,primeiro,terceiro)
if terceiro >= primeiro >= segundo:
    print(terceiro,primeiro,segundo)


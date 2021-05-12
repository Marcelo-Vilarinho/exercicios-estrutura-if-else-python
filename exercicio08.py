#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input())
produto2 = float(input())
produto3 = float(input())

if produto1 < produto2 and produto1 < produto3:
    print('primeiro produto com menor preço {}' .format(produto1))
elif produto2 < produto1 and produto2 < produto3:
    print('segundo produto com menor preço {}' .format(produto2))
elif produto3 < produto1 and produto3 < produto2:
    print('terceiro produto com menor preço {}' .format(produto3))
else:
    print('os produtos tem valores iguais')    
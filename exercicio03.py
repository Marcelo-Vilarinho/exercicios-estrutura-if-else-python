#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print('Por favor digite seu sexo com as seguintes opçoes  M - Masculino ou F - Feminino')
sexo = input()

if sexo == 'M':
    print('masculino')
elif sexo == 'F':
    print('feminino')
else:
    print("sexo invalido, digite apenas as opçoes acima")
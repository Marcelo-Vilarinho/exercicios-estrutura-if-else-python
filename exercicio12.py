#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do 
#Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto 
#menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas 
#no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo 
# abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

valor_hr = float(input("digite o valor de horas trabalhada : "))
qtd_trabalhada = float(input("digite quantas horas trabalhadas : "))

salario_liquido = valor_hr * qtd_trabalhada

if salario_liquido <= 900:

    desconto_inss = (5/100) * salario_liquido
    salario_desconto = salario_liquido - desconto_inss

    fgts = (11/100) * salario_liquido

    print("Salário Bruto : R$ {: .2f}".format(salario_liquido))
    print("(-) IR (insento) : R$ 0,00")
    print("(-) INSS  (5%) : R$ {: .2f} ".format(desconto_inss))
    print("(-)  FGTS (11%) : R$ {: .2f} ".format(fgts))
    print("Total de descontos : R$ {: .2f} ".format(desconto_inss))
    print("Salário Liquido : R$ {: .2f} ".format(salario_desconto))

elif salario_liquido <= 1500:
    
    inposto_renda = (5/100) * salario_liquido

    desconto_inss = (10/100) * salario_liquido
    salario_desconto = (salario_liquido - desconto_inss) - inposto_renda

    total_desconto = inposto_renda  + desconto_inss

    fgts = (11/100) * salario_liquido

    print("Salário Bruto : R$ {: .2f}".format(salario_liquido))
    print("(-) IR (5%) : R$ {: .2f}".format(inposto_renda))
    print("(-) INSS  (10%) : R$ {: .2f} ".format(desconto_inss))
    print("(-)  FGTS (11%) : R$ {: .2f} ".format(fgts))
    print("Total de descontos : R$ {: .2f} ".format(total_desconto))
    print("Salário Liquido : R$ {: .2f} ".format(salario_desconto))

elif salario_liquido <= 2500:
    
    inposto_renda = (10/100) * salario_liquido

    desconto_inss = (10/100) * salario_liquido
    salario_desconto = (salario_liquido - desconto_inss) - inposto_renda

    total_desconto = inposto_renda  + desconto_inss

    fgts = (11/100) * salario_liquido

    print("Salário Bruto : R$ {: .2f}".format(salario_liquido))
    print("(-) IR (10%) : R$ {: .2f}".format(inposto_renda))
    print("(-) INSS  (5%) : R$ {: .2f} ".format(desconto_inss))
    print("(-)  FGTS (11%) : R$ {: .2f} ".format(fgts))
    print("Total de descontos : R$ {: .2f} ".format(total_desconto))
    print("Salário Liquido : R$ {: .2f} ".format(salario_desconto))

elif salario_liquido > 2500:
    
    inposto_renda = (20/100) * salario_liquido

    desconto_inss = (10/100) * salario_liquido
    salario_desconto = (salario_liquido - desconto_inss) - inposto_renda

    total_desconto = inposto_renda  + desconto_inss

    fgts = (11/100) * salario_liquido

    print("Salário Bruto : R$ {: .2f}".format(salario_liquido))
    print("(-) IR (20%) : R$ {: .2f}".format(inposto_renda))
    print("(-) INSS  (5%) : R$ {: .2f} ".format(desconto_inss))
    print("(-)  FGTS (11%) : R$ {: .2f} ".format(fgts))
    print("Total de descontos : R$ {: .2f} ".format(total_desconto))
    print("Salário Liquido : R$ {: .2f} ".format(salario_desconto))


   
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai
#pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
#ou então o empréstimo será negado

valor_casa = float(input('Qual o valor da casa?  '))
salario = float(input('Qual o salário de comprador?  '))
anos_pagamento = int(input('Quantoa anos para pagar?  '))


salario_porcento = salario * 0.30   
prestacao = anos_pagamento * 12
prestacao_mensal= valor_casa / prestacao

print('presatacao mensal {}'.format(salario_porcento))
print('presatacao mensal {}'.format(prestacao_mensal))
print('presatacao mensal {}'.format(anos_pagamento))

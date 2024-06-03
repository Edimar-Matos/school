#4) Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

#- Para salários superiores a R$ 1.430,00, calcule um aumento de 10%
#- Para os inferiores ou iguais, o aumento é de R$ 15%.


salario = float(input("Qual o valor de seu salario: "))

if salario <= 1430:
    preco = salario * 0.10
    
else:
    preco = salario * 0.15

print('seu salario é :{:.2f}'.format(preco))
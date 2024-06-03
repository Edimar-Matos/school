# 2) Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Dijite um valor: '))
resultado = num % 2

if resultado == 0:
    print('O resultado do número {} é PAR'. format(num))
else:
    print('O resultado do número {} é IMPAR'.format(num))

    
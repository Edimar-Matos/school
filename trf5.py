#Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
#- O primeiro valor é MAIOR
#- O segundo valor é MENOR

def valor():
    vr1 = float(input('Seu primeiro numero: '))
    vr2 = float(input('Seu segundo numero: '))

    if vr1 > vr2:
        print('O primeiro valor é MAIOR')
        print('O segundo valor é MENOR')
        valor()
    elif vr1 < vr2:
        print('O primeiro valor é MENOR')
        print('O segundo valor é MAIOR')
        valor()
    else:
        print('Não existe valor maior, os dois são iguais')
        valor()
valor()

    
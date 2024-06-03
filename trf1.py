#1) Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km
#acima do limite.


vs = float(input('A velocidade de seu carro é: '))

base_v = 80

mut = 7.00

total = vs - 80

if vs > base_v:
    print('Voce foi multado à {} km/h'.format(vs))
    print('O valor da multa é: {}'.format(total * mut))
else:
    print('Parabens pela boa condução')


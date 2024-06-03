
distancia=float(input('Distancia de sua viagem: '))
print('A distancia e {}'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.60

print('O valor de sua viagem e de: R${:.2f}'.format(preco))
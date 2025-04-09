letra = input('Digite X: ')
contador = 0
if letra == 'x':
    print('Boa!')
else:
    while letra != 'x':
        print('BURRO! Isso não é X, digite novamente: ')
        letra = input('Digite X: ')
        
        contador += 1
        if letra == 'x':
            print(f'Boa! Você precisou repetir', contador, 'vezes para compreender!')



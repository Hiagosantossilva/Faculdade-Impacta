credito = float(input('Seu crédito: '))
total = 0 
preco = float(input('Preço do item: '))
quero_comprar = True
ni = 0

while quero_comprar:
    ni += 1
    total += preco
    credito -= preco

    x = input('Você quer continuar comprando? s/n:')

    if x == 's':
        preco = float(input('Preço do item: '))
    else:
        quero_comprar = False

print(f'Você comprou', ni, 'vezes')
print(f'Total da compra: R$ {total:.2f}')
print(f'Crédito restante: R$ {credito:.2f}')

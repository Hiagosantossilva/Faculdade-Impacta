number = float(input())

if number >= 0 and number <= 25:
    print(f'Intervalo [0,25]')
    
if number > 25 and number <= 50:
    print(f'Intervalo (25,50]')

if number > 50 and number <= 75:
    print(f'Intervalo (50,75]')

if number > 75 and number <= 100:
    print(f'Intervalo (75,100]')

if number > 100 or number < 0:
    print(f'Fora de intervalo')

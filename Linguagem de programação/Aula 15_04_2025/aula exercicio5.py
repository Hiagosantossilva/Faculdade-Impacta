tipo = input()
 
if tipo == 'invertebrado':
    caracteristica = input()

    if caracteristica == 'ave':
        alimentacao = input()
            
        if alimentacao == 'carnivoro':
                print('aguia')
        if alimentacao == 'onivoro': 
                print('pombo')

    if caracteristica == 'mamifero': 
        alimentacao = input()
                  
            if alimentacao == 'onivoro':
                print('homem')

            if alimentacao == 'herbivoro':
                print('vaca')

if tipo == 'vertebrado':
    caracteristica = input()
    
    if caracteristica == 'inseto':
        alimentacao = input()
            if alimentacao == 'hematofago':
                print('pulga')

            if alimentacao == 'herbivoro':
                print('lagarta')

    if caracteristica == 'anelideo':
        alimentacao = input()
            if alimentacao == 'hematofago':
                print('sanguessuga')

            if alimentacao == 'onivoro':
                print('minhoca')

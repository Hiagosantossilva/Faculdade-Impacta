n1, n2, n3, n4 = input().split(' ')
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/10
if media >= 7:
    status = 'Aluno em exame'
else:
    status = 'Aluno em exame'

if media < 5:
    status = 'Aluno reprovado'
    exame = float(input())
    notaFinal = (exame + media)/10

if media >= 7:
    status = 'Aluno em exame'
else:
    status = 'Aluno em exame'

if media < 5:
    status = 'Aluno reprovado'
    exame = float(input())
    
print(f'Media: {media}')
print(f'{status}.')


print(f'Nota do exame: {notaFinal}')

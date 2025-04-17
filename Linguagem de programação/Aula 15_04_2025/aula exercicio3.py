A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

valorA = 0
valorB = 0
valorC = 0
valorD = 0
valorE = 0

if A%2 == 0:
    valorA = 1

if B%2 == 0:
    valorB = 1

if C%2 == 0:
    valorC = 1

if D%2 == 0:
    valorD = 1

if E%2 == 0:
    valorE = 1

    
cont = valorA + valorB + valorC + valorD + valorE
print(f'{cont} valores pares')

A,B,C,D,E = input().split(" ")
A = int(A)
B = int(B)
C = int(C)
D = int(D)
E = int(E)

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

    
cont = valorA + valorB
print(f'{cont} valores pares')

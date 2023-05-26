numero = int(input('Digite um numero: '))
tot = 0

for c in range (1,numero+1):
    if numero % c == 0:
        print('\033[33m',end= ' ')
        tot +=1
    else:
        print('\033[31m',end= ' ')
    print(c,end= ' ')
print(f'\n\033[m O numero {numero} foi divisivel {tot} vezes')
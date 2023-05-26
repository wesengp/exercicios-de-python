n = int(input('Digite o numero que quer saber o fatorial: '))
c = n
f = 1
'''while c > 0:
    print(c, end=' ')
    print('x'if c>1 else '=', end= ' ')
    f *= c
    c -=1
print (f,end=' ')'''
#utilizando o For
for i in range(n,0,-1):
    print(i,end= ' ')
    print('x' if i > 1 else '=', end=' ')
    f *= i
print(f,end=' ')



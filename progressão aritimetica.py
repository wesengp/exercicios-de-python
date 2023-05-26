print('='*50)
print('      10 Termos de uma PA    ')
print('='*50)

primeiro_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão:  '))
decimo = primeiro_termo + (10)*razao

for i in range(primeiro_termo,decimo,razao):
    print(i,end=' -> ', )
print('Acabou')
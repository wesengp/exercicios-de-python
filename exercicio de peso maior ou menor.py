maior = 0
menor = 0
for p in range (1,6):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1: # Aqui é a primeira interação, pois o primeiro peso digitado será o menor e maior
        peso = maior
        peso = menor
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso encontrado foi {maior}')
print(f'O Menor peso encontrado foi {menor}')

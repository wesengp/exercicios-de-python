import random as numero_certo

print('Sou seu computador ...')
print('Acabei de Pensar em um numero de 1 a 10')
print('Consegue adivinhar qual foi? ')
computador = numero_certo.randint(0,10)
acertou = False
cont_palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite '))
    cont_palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Valor maior do que eu pensei.... Tente mais uma vez')
        elif jogador < computador:
            print('Valor menor do que eu pensei.... Tente mais uma vez')

print(f'Você acertou em {cont_palpite} tentativas')
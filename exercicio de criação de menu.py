import time
primeiro_valor = float(input('Digite um valor: '))
segundo_valor = float(input('Digite um valor: '))
opcao = 0
while opcao != 5:
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NUMEROS')
    print('[5] SAIR DO PROGRAMA')
    operacao = float(input('>>>> Qual sua Operação? '))
    print('==-==' * 8)
    if operacao == 1:
        soma = primeiro_valor + segundo_valor
        print(f'O valor da soma é {soma} ')
    elif operacao == 2:
        muliplicacao = primeiro_valor * segundo_valor
        print(muliplicacao)
    elif operacao == 3:
        if primeiro_valor > segundo_valor:
            print(f'O maior é {primeiro_valor}')
        else:
            print(f'O maior é {segundo_valor}')
    elif operacao == 4:
        time.sleep(1)
        primeiro_valor = float(input('Digite um valor: '))
        segundo_valor = float(input('Digite um valor: '))
    elif operacao == 5:
        break
    else:
        print('Opção inválida, digite os valores indicados no menu')

print('Fim do programa')

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    data = int(input(f'Em que ano a pessoa {pess}ª nasceu: '))
    idade_maior = atual - data
    if idade_maior <= 18:
        totmenor +=1
    else:
       totmaior +=1
print(f'Ao todo tivemos {totmaior} com maior idade e {totmenor} com menor idade')
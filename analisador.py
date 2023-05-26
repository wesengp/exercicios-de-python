cont = 0
maioridadehomem = 0
nomevelho = ''
somaidade= 0

for p in range (1, 4):
   print(f'------{p}ª PESSOA ----------')
   nome = str(input('Nome: ')).strip().upper()
   idade = int(input('Idade: '))
   sexo = str(input('[M/F]: ')).upper().strip()
   somaidade += idade
   if p == 1 and sexo in 'Mm':
      maioridadehomem = idade
      nomevelho = nome

   if sexo in 'Mm' and idade > maioridadehomem:
      maioridadehomem = idade
      nomevelho = nome
   if sexo in 'Ff' and idade < 20:
      cont +=1

mediaidade = somaidade/4

print(f'A idade do homem mais velho é {maioridadehomem} e ele se chama {nomevelho} ')
print(f'Média de idade das pessoas é {mediaidade}')
print(f'Existe {cont} do sexo feminino com menos de 20 anos')




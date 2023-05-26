import math

print("********************************")
print("Vamos calcular as equações do segundo grau")
print("********************************")
print("Para calcular a equação do segundo grau é preciso informar os valores dos coeficientes\n A,B,C")
print("Exemplo: x²+3x+6 na equação a seguir o valor de \n A: 1 B: 3 C: 3")
print("Então vamos lá com base no exemplo acima informe: ")
print()
a = int(input("Digite o Coeficiente de A: "))
b = int(input("Digite o Coeficiente de B: "))
c = int(input("Digite o Coeficiente de C: "))
delta = ((b**2) - 4*a*c)
print("O valor do delta é: ",delta)

if delta > 0:
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a
    print("X1 = ",x1, "\nX2 = ",x2)
elif delta == 0:
    x = -b/2*a
    print("X = ",x)
else:
    print("A Equação não possui raizes reais ")





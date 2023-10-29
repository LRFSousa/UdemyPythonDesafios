# Calculadora de IMC
'''

Fazer um programa que a pessoa entre com a altura em cm, seu peso em kg e ele calcule o IMC.

menor que 18.5 - magreza
entre 18,5 e 24,9 - normal
entre 25,0 e 29,9 - sobrepeso
entre 30 e 39,9 - obesidade
maior que 40,0 - obesidade grave

'''

peso = float(input('Entre com o peso (em kg): '))
altura = float(input('Entre com a altura (em cm): '))
imc = peso/(altura*altura/10000)
#dividi por 10.000 pois é altura/100 para passar p/ metro, como é ² fica *100*100

if imc < 18.5:
    print('Magreza, IMC = ',imc)
elif imc < 24.9:
    print('Normal, IMC = ', imc)
elif imc < 29.9:
    print('Sobrepeso, IMC = ', imc)
elif imc < 39.9:
    print('Obesidade, IMC = ', imc)
else:
    print('Obesidade grave, IMC = ', imc)
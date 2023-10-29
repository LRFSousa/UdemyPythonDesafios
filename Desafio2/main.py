# Desafio 2 - Trabalhando com funções

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer as seguintes informações: rendimento, altura e largura.
O programa deve mostrar na tela a mensagem: 'Você necessita de X latas de tinta.'

'''

def calculo(r,a,l):
    return a*l/r

rendimento = float(input('Entre com o rendimento da lata (em m²): '))
altura = float(input('Entre com a altura da parede (em m²): '))
largura = float(input('Entre com a largura da parede (em m²): '))
print('Você precisa de ', calculo(rendimento,altura,largura), ' latas de tintas.')

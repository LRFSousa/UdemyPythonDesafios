'''
Para este desafio, crie duas funções. A primeira função deve aceitar um número e retornar
o dobro desse número. A segunda função deve aceitar um número e retornar o quadrado desse número.
Em seguida, chame a segunda função dentro da primeira para retornar o quadrado do dobro de um número.

'''


def funcao1(x):
    return funcao2(2*x)


def funcao2(y):
    return y*y


numero = int(input('Entre com um número:'))
print('O quadrado do dobro do número é: ', funcao1(numero))
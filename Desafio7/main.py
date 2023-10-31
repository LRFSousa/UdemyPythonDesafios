'''
As funções recursivas são funções que se chamam dentro do seu próprio bloco de código.
Elas são úteis para resolver problemas que podem ser divididos em problemas menores de natureza
semelhante.

Um exemplo clássico de onde a recursão é usada é o cálculo do fatorial de um número. O fatorial
de um número n é o produto de todos os números inteiros positivos de n até 1.
'''


def fatorial(numero):
    fat = 1
    for i in range(1, numero + 1):
        fat *= i
        fat *= i
    return fat


numero = int(input('Entre com o número a ter o fatorial calculado: '))
print('O valor do fatorial de ', numero, ' é:', fatorial(numero))

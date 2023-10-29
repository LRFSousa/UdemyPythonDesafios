# Desafio 5 - Trabalhando com listas
"""
Crie um programa que o usuário entre com uma lista de frutas, depois:
 1 - imprima o primeiro e o último elemento da lista;
 2 - altere o segundo elemento da lista para o nome fornecido
 3 - solicite uma fruta para que você remova da lista
"""

dados = input('Entre com as frutas separadas por vírgula (,): ')
lista = dados.split(', ')
print('Primeiro elemento da lista: ' + lista[0] + ', último elemento da lista: ' + lista[-1])

lista[1] = input('Entre com o nome da nova fruta: ')
print(lista)
lista.remove(input('Entre com a fruta a ser removida: '))
print(lista)



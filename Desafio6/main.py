'''

Crie uma lista com os nomes de três cidades. Peça ao usuário para digitar o nome de uma cidade.
Se a cidade estiver na lista, imprima "A cidade está na lista de cidades". Se a cidade não
estiver na tupla, imprima "A cidade não está na lista de cidades".

'''

cidades = ('São Paulo', 'Rio de Janeiro', 'Salvador')
cidade_usuario = input('Digite o nome da cidade: ')

if cidade_usuario in cidades:
    print('A cidade está na lista de cidades')
else:
    print('A cidade não está na lista de cidades')
# Desafio1
'''
Criar um programa que dependendo da temperatuda (em celsius) da carne ele retorna o ponto
de cozimento em graus. O usuário deverá fornecer a temperatura.

Temperaturas de cozimento:
120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium Rare - (Ao ponto para o mal passada)
140°F ou 60°C - Medium (ao ponto)
150°F ou 65°C - Medium well (Ao ponto para o bem)
160°F ou 71°C - Well done (bem passada)
'''

temp = int(input('Qual a temperatura da carne? '))
if temp < 48:
    print('Cozinhe por mais alguns minutos.')
elif temp < 54:
    print('Carne selada.')
elif temp < 60:
    print('Ao ponto para o mal passada.')
elif temp < 65:
    print('Ao ponto.')
elif temp < 71:
    print('Bem passada.')
else:
    print('Diminua a temperatura')
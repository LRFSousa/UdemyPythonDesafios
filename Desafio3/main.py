# Desafio 3 - Trabalhando com 'Sets'

'''
Criar um programa que gere 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que têm carro e trabalham a noite.
Lista2 = Funcionários que têm carro e trabalham durante o dia.
Lista3 = Funcionários que não têm carro.

'''
n=0
funcionarios = set()
x = int(input('Entre com o número de funcionários: '))
while n < x:
    funcionarios.add(input('Nome: '))
    n += 1

func_tem_carro = set()
n=0
ftc = int(input('Entre com o número de funcionários que possuem carro: '))
while n < ftc:
    func_tem_carro.add(input('Nome: '))
    n += 1

turno_dia = set()
n=0
td = int(input('Entre com o número de funcionários que trabalham no turno de dia: '))
while n < td:
    turno_dia.add(input('Nome: '))
    n += 1

turno_noite = set()
tn = int(input('Entre com o número de funcionários que trabalham no turno noturno: '))
n=0
while n < tn:
    turno_noite.add(input('Nome: '))
    n += 1
print('Funcionários que têm carro e trabalham durante o dia: ', func_tem_carro.intersection(turno_dia))
print('Funcionários que têm carro e trabalham durante a noite: ', func_tem_carro.intersection(turno_noite))
print('Funcionários que não têm carro: ', funcionarios.difference(func_tem_carro))





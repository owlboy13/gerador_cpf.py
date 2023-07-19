#código feito nas primeiras aula de Python 
﻿import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito = (resultado *10) % 11
digito = digito if digito <= 9 else 0

#segundo digito
dez_digitos = nove_digitos + str(digito)
contador_regressivo_2 = 11

resultado_2 = 0
for digito_2 in dez_digitos:
    resultado_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_2 *10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito}{digito_2}'
if cpf_gerado[:9] == nove_digitos:
    print(f'{cpf_gerado} é válido!')
else:
    print('CPF inválido')

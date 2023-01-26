"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '746.824.890-70'
nove_digitos = []
cont2 = 10
num =  0
multi = 0

for i in cpf:

    try:

        num = int(i)
        if num or num == 0:
            mult = num * cont2
            cont2 -= 1
            nove_digitos.append(mult)
    except:
        ...
nove_digitos.pop()
nove_digitos.pop()
soma_nove = sum(nove_digitos) * 10
resto_divisao = soma_nove % 11
digito1 = resto_divisao if resto_divisao <= 9 else 0

print(nove_digitos, soma_nove,'-', digito1)
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""


nove_digitos2 = []
cont2 = 11
num2 = 0
multi2 = 0

for i in cpf:
    try:

        num2 = int(i)
        if num2 or num2 == 0:
            mult2 = num2 * cont2
            cont2 -= 1
            nove_digitos2.append(mult2)
    except:
        ...
nove_digitos2.pop()
nove_digitos2.pop()
nove_digitos2.append(int(cpf[0]) * 2)
soma_nove2 = sum(nove_digitos2) * 10
resto_divisao2 = soma_nove2 % 11
digito2 = resto_divisao2 if resto_divisao2 <= 9 else 0

print(nove_digitos2, soma_nove2,'-', digito2)
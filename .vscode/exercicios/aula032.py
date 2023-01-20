"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
n = (input('Digite um número inteiro: '))
if not n.isnumeric:
    print('Digite um número inteiro.')
else:
    n = int(n)
    if n % 2 == 0:
        print(f'o número {n} é par.')
    else:
        print(f'o número {n} é ímpar.')
print('')
print('')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23....teste... teste
"""
while True:
    hora = int(input('Que horas são ? '))
    

    if hora <= 11:
        print('Bom dia!') 
    elif hora > 11 and hora < 18:

        print('Boa tarde')
    elif hora >= 18 and hora < 24:
        print('Boa noite!')
    else:
        print('hora inválida')
    if hora == 0000:
        break
print('')
print('')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou ... testando git ...
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
while True:
    nome = input('Nome: ')
    if nome == '0':
        break
    if len(nome) <= 6:
        print('Seu nome é curto.')
    else:
        print('Seu nome é muito grande.')
    
"""
Iterando Strings com While  - acrescente sinais antes e depois das letras de um nome utilizando While

"""


nome  = 'Francis Paul da Rocha '
contador = 0
while contador < len(nome) + 1:
    print('-*-', end='')
    print(nome[contador], end='')
    contador += 1
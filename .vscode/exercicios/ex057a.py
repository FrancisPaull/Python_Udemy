"""Escreva um código que pede para o usuário digitar uma lista de nomes de pessoas e idades, 
em seguida, cria uma nova lista com as pessoas com idade acima de 25 anos. 
Em seguida, imprima a nova lista e a média de idade das pessoas incluídas na lista."""


def cadastro(n):
    quantidade  = n
    lista = []
    maiores_25 = []
    media_idade = []
    lista_completa = []
    for i in range(0,n):
        nome = input('Adicione um Nome: ')
        idade = int(input('Qual idade: '))
        media_idade.append(idade)        
        if idade > 25:
            maiores_25.append(nome)            
        lista.append(nome)
        lista.append(idade)
        
        lista_completa.append(lista[:])
        
        lista.clear()
        
    print(f'Média de idade é {sum(media_idade) / len(media_idade)}')
    print(f'A lista completa dos cadastrados: {lista_completa}')


cadastro(2)

    
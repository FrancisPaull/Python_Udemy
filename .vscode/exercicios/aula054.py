"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_compras = ['Arroz', 'Feijão', 'Macarrão']
lista = []

while True:
    try:
        opcao = input('Selecione uma opção. [i]nserir [a]pagar ou [l]istar:  ')
        if len(opcao) > 1:
            print("Entrada inválida, digite apenas uma letra .")
            continue

        elif opcao == 'i':
            while True:
                produto = input('Nome do produto: ')
                if produto == '':
                    print('Nada digitado. Por favor, digite o nome do produto.')
                else:
                    break
            lista.append(produto)
            lista_compras += lista[:]
            print(lista_compras)
        elif opcao == 'a':
            while True:
                apagar_indice = int(input("Digite qual indice apagar: "))
                if apagar_indice > len(lista_compras):
                    print('indice inválido:')
                elif len(lista_compras) == 0:
                    print('Não há produtos registrados.')
                else:
                    break
            lista_compras.pop(apagar_indice)
            print(lista_compras)
        lista.clear()




        if opcao == 'l':
            for indice, produto in enumerate(lista_compras):
                print(f'Produto.{indice} - {produto}.')

        if opcao not in 'ial':
            print('Opção inválida, tente novamente.')

    except:
        ...
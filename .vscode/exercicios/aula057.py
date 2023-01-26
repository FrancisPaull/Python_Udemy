"""ex: Escreva um código que pede para o usuário digitar uma lista de números inteiros e, 
em seguida, cria uma nova lista com todos os números ímpares da lista original. 
Em seguida, imprima a nova lista e a soma de todos os números ímpares da lista original."""

import os
numero  = 0
lista = []
impar = []
soma_impar = []
quantidade_ = int(input("Quantos valores gostaria de adicionar? "))
os.system('cls')
for i in range(0, quantidade_):
    numero = int(input('Digite um número inteiro: '))
    lista.append(numero) 
    os.system('cls')
    if numero % 2 == 1:
        impar.append(numero)
        soma_impar= sum(impar)


print(f'Os valores ímares digitados são: {impar}, e a soma dos números ímpares da lista é {soma_impar}')
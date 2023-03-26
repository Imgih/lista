#Escreva um programa que peça ao usuário para digitar uma lista de palavras e,
#em seguida, crie uma nova lista que contenha apenas as palavras que têm um número ímpar de letras.


minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = input("Entre com as palavras:  ")
    minha_lista.append(val)

   
nova_lista = []

for palavra in minha_lista:
    if len(palavra) % 2 == 1:
        nova_lista.append(palavra)

print(nova_lista)

 
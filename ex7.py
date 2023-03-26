#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, imprima o nome mais longo e o nome mais curto da lista.

minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = input("Entre com as palavras:  ")
    minha_lista.append(val)



mais_longo =  minha_lista[0]
menor = minha_lista[0]

for nome in minha_lista:
    if len(nome) > len(mais_longo):
        mais_longo = nome
    elif len(nome) < len(menor):
        menor = nome

print("A maior palavra é: ", mais_longo)
print("A menor palavra é: ", menor)
#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule a média dos números na lista.

minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = float(input("Entre com um número: "))
    minha_lista.append(val)

numeros = minha_lista

media = sum(numeros)/ len(numeros)

print("A média dos números na lista é: ", media)
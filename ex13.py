#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais alto na lista.


minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = int(input("Entre com os números:  "))
    minha_lista.append(val)
    
    
minha_lista.sort()

print("O segundo maior número é: ", minha_lista[-2])
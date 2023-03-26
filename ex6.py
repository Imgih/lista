#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista ordenada em ordem decrescente.


minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = int(input("Entre com um número: "))
    minha_lista.append(val)

minha_lista.sort(key=int, reverse=True)
print(minha_lista)
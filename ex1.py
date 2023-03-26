#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números pares da lista.

minha_lista = []
num = int(input("Quantos elementos deseja? "))

for i in range(num):
    val = int(input("Entre com um número: "))
    if val %2 == 0:
        minha_lista.append(val)
   
print(minha_lista)



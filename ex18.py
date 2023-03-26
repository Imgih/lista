#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por 3.


minha_lista = []
num = int(input("Quantos elementos deseja? "))


numeros_divi = []

for i in range(num):
    val = int(input("Entre com os números:  "))
    if val %3 == 0:
        numeros_divi.append(val)

print(numeros_divi)


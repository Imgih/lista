#Escreva um programa que peça ao usuário para digitar uma lista de números e, ,
#em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por um número fornecido pelo usuário.

minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    numeros = int(input("Entre com o nome:  "))
    minha_lista.append(numeros)



divisor = int(input("Digite um numero qualquer: "))

numeros = minha_lista 
divisiveis = []

for numero in numeros:
    if numero % divisor == 0:
        divisiveis.append(numero)
        
print(divisiveis)
   
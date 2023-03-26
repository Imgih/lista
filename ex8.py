#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são maiores do que 10.


minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = int(input("Entre com os números:  "))
    minha_lista.append(val)
    
    
numeros = minha_lista

for numero in numeros: 
    if numero > 10: 
        print(numero)
    elif numero < 10:
        print("Não tem núemros maiores que 10")
#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são menores do que 5.

minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = float(input("Entre com os números:  "))
    minha_lista.append(val)
    
    
numeros = minha_lista

for numero in numeros: 
    if numero < 5: 
        print(numero)
    elif numero > 5:
        print("Não tem núemros menores que 5")
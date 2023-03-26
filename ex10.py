#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista com os números duplicados removidos.



minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = int(input("Entre com os números:  "))
    minha_lista.append(val)

sem_repeticao= []
numeros = minha_lista


for numero in numeros: 
    if numero not in sem_repeticao:
        sem_repeticao.append(numero)

print(sem_repeticao)
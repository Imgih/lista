# um programa que peça ao usuário para digitar uma lista de números e, 
#em seguida, crie uma nova lista que contenha apenas os números que aparecem mais de uma vez na lista original.

minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = int(input("Entre com os números:  "))
    minha_lista.append(val)


numeros = minha_lista

lista_com_duplicatas = []

numeros_repetidos = []


for num in numeros:
    if numeros.count(num) > 1 and num not in numeros_repetidos:
        numeros_repetidos.append(num)

print(numeros_repetidos) 
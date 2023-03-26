#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.

minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = int(input("Entre com um número: "))
    minha_lista.append(val)
    

numeros = minha_lista

maior_numero = numeros[0] #inicializando a váriaveis que irá armazenar o maior número

for numero in numeros: # usando um loop for para percorrer a lista e encontrar o maior número
    if numero > maior_numero: 
        maior_numero = numero

print("O maior número da lista é: ", maior_numero)


menor_numero = numeros[0]

for numero in numeros:
    if numero < menor_numero:
        menor_numero = numero

print("O menor número da lista é: ", menor_numero)
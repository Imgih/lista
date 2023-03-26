#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, crie uma nova lista que contenha apenas os nomes que contêm a letra "e".



nomes_com_e = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    nomes = input("Entre com as palavras:  ")
    if 'e' in nomes.lower():
        nomes_com_e.append(nomes)
    
print(nomes_com_e)
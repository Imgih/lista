#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, 
#em seguida, verifique se um determinado nome está na lista. Se estiver, imprima "O nome está na lista"; caso contrário, imprima "O nome não está na lista".





minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    palavras = input("Entre com o nome:  ")
    minha_lista.append(palavras)



nomes = input("Digite um nome qualquer: ")

 
if nomes not in minha_lista:
    print("O nome não está na lista!")
elif nomes in minha_lista:
    print("O nome está na lista")
    

    
    
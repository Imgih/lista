#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule e imprima a soma de todos os números ímpares na lista.

minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = float(input("Entre com os números:  "))
    if val %2 == 1:
     minha_lista.append(val)  
     
  
soma = sum(minha_lista)   
print("A soma dos núemros ímpares é:", soma)
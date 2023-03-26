#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, remova todos os números duplicados da lista e imprima a nova lista.

minha_lista = []
num = int(input("Quantos elementos deseja? "))


for i in range(num):
    val = int(input("Entre com os números:  "))
    minha_lista.append(val)


lista_com_duplicatas = minha_lista

lista_sem_duplicatas = []

while lista_com_duplicatas:
    elemento = lista_com_duplicatas.pop(0) 
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)
        
print("A lista sem duplicatas é: ", lista_sem_duplicatas)
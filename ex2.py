#Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, imprima apenas as palavras que começam com a letra "a".

minha_lista = []
num = int(input("Quantos elementos deseja? "))

for i in range(num):
    val = input("Entre com a fruta: ")
    if (val[0] == 'a'):
        minha_lista.append(val)
   
print(minha_lista)

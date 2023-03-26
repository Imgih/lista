# pede ao usuário para digitar uma lista de nomes separados por vírgulas
nomes = input("Digite uma lista de nomes separados por vírgulas: ")

# cria uma nova lista que conterá apenas os nomes que contêm a letra "e"
nomes_com_e = minha_lista

# percorre cada nome na lista de nomes
for nome in nomes.split(','):
    # verifica se o nome contém a letra "e" (maiúscula ou minúscula)
    if 'e' in nome.lower():
        # adiciona o nome à lista de nomes com "e"
        nomes_com_e.append(nome)

# imprime a lista de nomes que contêm a letra "e"
print("Nomes que contêm a letra 'e':")
for nome in nomes_com_e:
    print(nome)
precos = []           #Cria a lista 

for i in range(10):                                                             #funçao de repetiçao de 10x
    preco = float(input(f"Digite o preço do produto {i + 1}: R$ "))             #pergunta os valores  
    precos.append(preco)                                                        #Adiciona os valores a lista

produtos = [preco for preco in precos if preco > 100]                           #Cria uma nova lista, com os valores acima de 100


print("Lista completa: ", precos)                 #mostra a lista completa
print("Proço acima de R$100: ", produtos)         #mostra os valore acima de 100 
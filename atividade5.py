a1 = int(input("Digite o primeiro termo: "))     # Recebe o primeiro termo da PA
r = int(input("Digite a razão: "))               # Recebe a razão da PA

pa = []                                          # Cria uma lista vazia


for n in range(1, 11):                           # Repete 10 vezes
    # Calcula o termo da PA
    termo = a1 + (n - 1) * r
    # Adiciona o termo na lista
    pa.append(termo)

print("PA:", pa)                                 # Mostra a lista com os 10 termos

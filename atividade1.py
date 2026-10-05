temperatura = []                    #criar a lista

#adiciona na lista as temperaturas que foram digitadas
temperatura.append(float(input("Digite a primera temperatura:")))
temperatura.append(float(input("Digite a segunda temperatura:")))
temperatura.append(float(input("Digite a tersera temperatura:")))
temperatura.append(float(input("Digite a quarta temperatura:")))
temperatura.append(float(input("Digite a quinta temperatura:")))

#mostra o resutado 
print("A lista completa ", temperatura)
print("Primeira temperatura", temperatura[0])
print("Utima temperatura", temperatura[4])
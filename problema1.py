n = int(input("digite a quantidade de termos: "))  #variavel que guarda a quantidade de termos

#primeiros valores
a = 0  
b = 1  

for i in range(n):  #Repete N veses 
    print(a)
    proximo = a + b #soma os 2 numeros pra descobrir o proximo 
    a = b          
    b = proximo


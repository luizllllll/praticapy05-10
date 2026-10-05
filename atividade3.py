quantidade = int(input("Quantidade de alunos: "))          #Variavel que guarda a quantidade de alunos

notas = ()                                                 #Criar uma tupla vazia pra guardar as notas

for i in range(quantidade):                                #Cria a funçao que vai repitir de acordo com a quantidade de alunos
    nome = input(f"Digite o nome dos aluno {i + 1}:")      #pergunta o nome do aluno
    nota = float(input(f"Digite a nota do aluno {nome}: "))#pergunta nota do aluno 

    notas = notas + (nota,)  #adiciona a nota dna tupla 

media = sum(notas) / len(notas) #faz a operaçao da media Sum soma e Len conta os elementos e divide


#mostra as respostas 
print("notas:", notas)
print("maior nota", max(notas))
print("menor nota", min(notas))
print("media:", media)
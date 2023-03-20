from lista import *

list = lista() #CRIAÇÃO DA LISTA.

for cont in range(1,6):
    list.append(cont) #ADICIOANDO OS VALORES DO 1 AO 5 NA LISTA.

print(list) #OUTPUT: 1 2 3 4 5
print(len(list)) #OUTPUT 5

list.pop() #FUNÇÃO QUE REMOVE O ULTIMO ELEMENTO
print(list) #OUTPUT: 1 2 3 4 
print(len(list)) #OUTPUT 4

list.remove(3) #FUNÇÃO DE RETORNAR ELEMENTO PELO VALOR
print(list) #OUTPUT: 1 2 4 
print(len(list)) #OUTPUT 3

list.insert(2,3) 
print(list) #OUTPUT 1 2 3 4
print(len(list)) #OUTPUT 4

print(list[1]) #OUTPUT 2

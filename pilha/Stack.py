from Node import Node #Importação do no

class Stack(): #Pilha
    def __init__(self): #Criação dos atributos.
        self.top = None
        self.size = 0

    def add(self, value): #Função para adicionar elemento na pilha.
        node = Node(value) #Vou jogar o novo elemento dentro de um Nó
        node.next = self.top
        self.top = node
        self.size += 1 #Tamanho do Nó aumenta mais um.
    
    def pop(self): #Função para remover elemento da pilha
        if self.size != 0:
            self.top = self.top.next #O proximo do Nó, vai receber um None, assim faz com que o ultimo elemento seja excluido
            self.size -= 1 #Tamanho do Nó diminui menos um
        else:
            print('Error, no element on stack.')

    def peek(self):
        if self.size != 0:
            pointer = self.top
            while (pointer):
                print(pointer.value)
                pointer = pointer.next
        else:
            print('Error, The stack is empty')
    
    def __len__ (self):
        return self.size


from Node import Node #importação do Nó

class Queue():
    def __init__(self): #Criação dos atributos.
        self.start= None
        self.last = None
        self.size = 0
    
    def add(self, value): #Função de adicionar elemento na fila
        node = Node(value) #Vou jogar o novo elemento dentro de um Nó
        self.size += 1
        if (self.last is None):
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if (self.start is None):
            self.start = node

#Não terminado
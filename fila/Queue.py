from Node import Node #importação do Nó

class Queue():
    def __init__(self): #Criação dos atributos.
        self.start= None
        self.last = None
        self.size = 0
    
    def add(self, value): #Função de adicionar elemento na fila
        if (self.start):
            node = Node(value)
            self.last.next = node
            self.last = node
            self.size += 1
        else:
            self.start = self.last = Node(value)
            self.size += 1
    
    def remove(self):
        if (self.size>1):
            pointer = self.start
            while(pointer.next != self.last):
                pointer = pointer.next
            pointer.next = None
            self.last = pointer
            self.size -= 1
        elif (self.size == 1):
            self.start = None
            self.last = None
            self.size -= 1

    def __repr__(self):
        if (self.size > 0):
            pointer = self.start
            r = ""
            while(pointer):
                r += str(pointer.value) + " "
                pointer = pointer.next
            return r
        else:
            return ""

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return self.size

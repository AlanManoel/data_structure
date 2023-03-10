from Node import *

class circular_list:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    def append(self, value):
        '''Função de adicionar elemento no final da lista'''
        if (self.size > 0):
            node = Node(value)
            self.last.next = node
            node.next = self.first
            self.last = node
            self.size += 1
        else:
            self.first = self.last = Node(value)
            self.last.next = self.first
            self.size += 1

    def insert(self, index, value):
        '''Função de inserção de valor pelo index'''
        if (index <= 0):
            node = Node(value)
            node.next = self.first
            self.first = node
            self.last.next = self.first
            self.size += 1
        elif (index <= self.size):
            pointer = self.first
            for cont in range(index - 1):
                pointer = pointer.next
            node = Node(value)
            node.next = pointer.next
            pointer.next = node
        else:
            self.append(value)
    
    def pop(self):
        pass

    def remove(self, value):
        pass

    def index(self, value):
        pass

    def __repr__(self):
        '''Função para retorna a lista'''
        if (self.size > 0):
            pointer = self.first
            r = ''
            while(pointer):
                if (pointer.next != self.first):
                    r += str(pointer.value) + ' '
                    pointer = pointer.next
                else:
                    r += str(self.last.value) +  ' '
                    break
            return r
        return "Lista vazia"
    

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        '''Função que ira retorna o tamanho da lista'''
        return self.size
    
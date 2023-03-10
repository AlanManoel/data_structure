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
        else:
            self.first = self.last = Node(value)
            self.last.next = self.first
            self.size += 1

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
    
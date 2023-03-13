from Node import *

class Doubly_linked_list:
    def __init__(self):
        self.list = None
        self.size = 0

    def append(self, value):
        if (self.list == None):
            self.list = Node(value)
            self.size += 1
        else:
            pointer = self.list
            while(pointer.right):
                pointer = pointer.right
            node = Node(value)
            node.left = pointer
            pointer.right = node
            self.size += 1

    def __repr__(self):
        if (self.size > 0):
            pointer = self.list
            r = ""
            while(pointer):
                r += str(pointer.value) + " "
                pointer = pointer.right
            return r
        else:
            return " "
        
    def __str__(self):
        return self.__repr__()


    def __len__(self):
        '''Função para retorna o tamanho da lista'''
        return self.size
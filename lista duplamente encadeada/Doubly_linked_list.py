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

    def insert(self, index, value):
        if (index <= 0):
            pointer = self.list
            node = Node(value)
            node.right = pointer
            pointer.left = node
            self.list = node
            self.size += 1
        elif (index <= self.size):
            node = Node(value)
            pointer = self.list
            for cont in range(index - 1):
                pointer = pointer.right
            node.left = pointer
            node.right = pointer.right
            pointer.right.left = node
            pointer.right = node
            self.size += 1
        else:
            self.append(value)
    
    def pop(self):
        pass

    def remove(self,  value):
        pass

    def index(self, index):
        pass

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
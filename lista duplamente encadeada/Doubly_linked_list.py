from Node import *

class Doubly_linked_list:
    def __init__(self):
        self.list = None
        self.size = 0

    def append(self, value):
        '''Função para adicionar no fim da fila'''
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
        '''Função de inserir no index desejado'''
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
        '''Função de remover no fim da fila'''
        if (self.size > 1):
            pointer = self.list
            while(pointer.right.right):
                pointer = pointer.right
            pointer.right.left = None
            pointer.right = None
            self.size -= 1
        elif (self.size == 1):
            self.list = None
            self.size -= 1
        
    def remove(self,  value):
        if (self.size > 0):
            pointer = self.list
            if (pointer.value == value):
                pointer = pointer.right
                self.list = pointer
                self.size -= 1
            else:
                while(pointer.right):
                    if (pointer.right.value == value):
                        if (pointer.right.right):
                            pointer.right.right.left = pointer
                            pointer.right = pointer.right.right
                            self.size -= 1
                        else:
                            self.pop()
                    else:
                        pointer = pointer.right


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
            return "Empty list "
        
    def __str__(self):
        return self.__repr__()


    def __len__(self):
        '''Função para retorna o tamanho da lista'''
        return self.size


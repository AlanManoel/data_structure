from Node import *

class lista:
    def __init__(self):
        self.lista = None
        self.size = 0
        
    def append(self, valor):
        if (self.lista == None):
            self.lista = Node(valor)
            self.size += 1
        else:
            ponteiro = self.lista
            while(ponteiro.next is not None):
                ponteiro = ponteiro.next
            ponteiro.next = Node(valor)
            self.size += 1
    
    def insert(self, index, valor):
        if (index <= 0):
            ponteiro = self.lista
            node = Node(valor)
            node.next = ponteiro
            self.lista = node
        elif (index <= self.size):  
            ponteiro = self.lista
            node = Node(valor)
            for cont in range(index - 1):
                ponteiro = ponteiro.next
            node.next = ponteiro.next
            ponteiro.next=node
        else:
            self.append(valor)
        self.size +=1

    def pop(self):
        if (self.size > 1):
            ponteiro = self.lista
            while (ponteiro.next is not None):
                if (ponteiro.next.next is None):
                    ponteiro.next = None
                    self.size -= 1
                else:
                    ponteiro = ponteiro.next
        elif (self.size == 1):
            self.lista = None
            self.size -=1
        else:
            print("\033[31mLista vazia\033[m")
        
    def remove(self, valor):
        if (self.size > 0):
            ponteiro = self.lista
            if (ponteiro.value == valor):
                ponteiro = ponteiro.next
                self.lista = ponteiro
                self.size -= 1
            else:
                while(ponteiro.next is not None):
                    if (ponteiro.next.value == valor):
                        ponteiro.next = ponteiro.next.next
                        self.size -= 1
                    else:
                        ponteiro = ponteiro.next
        else:
            print("\033[31mLista vazia\033[m")
    
    def index(self, index):
        ponteiro = self.lista
        if (index >= 0 and index < self.size):
            for cont in range(index):
                ponteiro = ponteiro.next
            print(ponteiro.value)
        else:
            print("\033[31mIndex invalido\033[m")
        
    def __len__(self):
        return self.size
    
    def __repr__(self):
        if (self.size > 0):
            r = ""
            ponteiro = self.lista
            while(ponteiro is not None):
                r += str(ponteiro.value) + " "
                ponteiro = ponteiro.next
            return r
        return ""

    def __str__(self):
        return self.__repr__()
from Node import *

class Doubly_linked_list:
    def __init__(self):
        self.list = None
        self.size = 0

    def __len__(self):
        '''Função para retorna o tamanho da lista'''
        return self.size
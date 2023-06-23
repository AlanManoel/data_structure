from Node import *

class Binary_tree:
    def __init__(self, value = None):
        self.size = 0
        if (value):
            self.root = Node(value)
            self.size += 1
        else:
            self.root = None
    
    def insert(self, value):
        try:
            v = int(value)
        except:
            print('Somente numeros')
        else:
            relative = None
            pointer = self.root
            while (pointer):
                if (pointer.value == value):
                    print('O numero já esta na arvore')
                    break
                else:
                    relative = pointer
                    if (value < pointer.value):
                        pointer = pointer.left
                    else:
                        pointer = pointer.right   
            if not (relative):
                self.root = Node(value)
                self.size += 1
            elif (value < relative.value):
                relative.left = Node(value)
                self.size += 1
            else:
                relative.right = Node(value)
                self.size += 1


    def pre_order(self, node = None):
        if (self.root):
            if not (node):
                node = self.root
            print(node.value, end=' ')
            if (node.left):
                self.pre_order(node.left)
            if (node.right):
                self.pre_order(node.right)
    
    def in_order(self, node = None):
        if(self.root):
            if not (node):
                node = self.root
            if (node.left):
                self.in_order(node.left)
            print(node.value, end=' ')
            if (node.right):
                self.in_order(node.right)

    def post_order(self, node = None):
        if (self.root):
            if not(node):
                node = self.root
            if (node.left):
                self.post_order(node.left)
            if (node.right):
                self.post_order(node.right)
            print(node.value, end=' ')
    
    def height(self, node = None):
        if (self.root):
            if not(node):
                node = self.root
            height_left = 0
            height_right = 0
            if (node.left):
                height_left =  self.height(node.left)
            if (node.right):
                height_right = self.height(node.right)
            if (height_right > height_left):
                return height_right + 1
            return height_left + 1
        
    def max_value(self):
        if (self.root):
            pointer = self.root
            while(pointer.right):
                pointer = pointer.right
            print(pointer)
    
    def min_value(self):
        if (self.root):
            pointer = self.root
            while(pointer.left):
                pointer = pointer.left
            print(pointer)

    def print_binary_tree(self):
        self.recursion_binary_tree(self.root)
    
    def recursion_binary_tree(self, node, level=0):
        if (node):
            self.recursion_binary_tree(node.right, level + 1)
            print(f'{"    " * level} ({node.value})')
            self.recursion_binary_tree(node.left, level + 1)

    def __len__(self):
        return self.size

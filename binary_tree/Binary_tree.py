from Node import *
from queue import Queue

class Binary_tree:
    def __init__(self, value = None):
        self.size = 0
        if (value):
            self.root = Node(value)
            self.size += 1
        else:
            self.root = None
    
    def insert(self, value):
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

    def level_route(self, node=None):
        if not(node):
            node = self.root
        queue = Queue()
        queue.put(node)
        while queue.qsize():
            node = queue.get()
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
            print(node, end=" ")

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
    
    def max_value(self, pointer=None):
        if not(pointer):
            pointer = self.root
        while(pointer.right):
            pointer = pointer.right
        return pointer.value

    def min_value(self, pointer=None):
        if not(pointer):
            pointer = self.root
        while(pointer.left):
            pointer = pointer.left
        return pointer.value

    def remove(self, value, node=None):
        if not(node):
            node = self.root
        if value < node.value:
            node.left = self.remove(value, node.left)
        elif value > node.value:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                pointer = self.min_value(node.right)
                node.value = pointer
                node.right = self.remove(pointer, node.right)
        return node

    def print_tree(self):
        self.recursion_binary_tree(self.root)
    
    def recursion_binary_tree(self, node, level=0):
        if (node):
            self.recursion_binary_tree(node.right, level + 1)
            print(f'{"    " * level} ({node.value})')
            self.recursion_binary_tree(node.left, level + 1)
    
            
    # def bin(self, node=None):
    #     if not node:
    #         node = self.root
    #     queue = Queue()
    #     queue.put(node)
    #     level = self.height()
    #     while (queue.qsize()):
    #         level_nodes = []
    #         level -= 1
    #         for i in range(queue.qsize()):
    #             node = queue.get()
    #             if node:
    #                 level_nodes.append(node.value)
    #                 queue.put(node.left)
    #                 queue.put(node.right)
    #             else:
    #                 level_nodes.append(None)

    #         print("  " * level, end="")

    #         for value in level_nodes:
    #             if value is None:
    #                 print("    ", end="")
    #             else:
    #                 print(f"({value})", end="")
    #         print()

    def __len__(self):
        return self.size

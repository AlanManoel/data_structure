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
        if not(self.search(value)):
            relative = None
            pointer = self.root
            while (pointer):
                if (pointer.value == value):
                    return False
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
            height_left = -1
            height_right = -1
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

    def search(self, value):
        return self.recursive_search(value, self.root)

    def recursive_search(self, value, node):
        if not(node):
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self.recursive_search(value, node.left)
        return self.recursive_search(value, node.right)

    def print_tree(self):
        self.recursion_binary_tree(self.root)
    
    def recursion_binary_tree(self, node, level=0):
        if (node):
            self.recursion_binary_tree(node.right, level + 1)
            print(f'{"    " * level} ({node.value})')
            self.recursion_binary_tree(node.left, level + 1)

    def __len__(self):
        return self.size


class Binary_AVL(Binary_tree):

    def insert(self, value):
        if not(self.search(value)):
            relative = None
            pointer = self.root
            while (pointer):
                if (pointer.value == value):
                    return False
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
        self.check_balance(self.root, self.root)

    def remove(self, value, node=None):
        if not(node):
            node = self.root
        if value < node.value:
            node.left = self.remove(value, node.left)
        elif value > node.value:
            node.right = self.remove(value, node.right)
        else:
            if node is self.root:
                if node.left is None:
                    self.root = node.right
                elif node.right is None:
                    self.root = node.left
                else:
                    pointer = self.min_value(node.right)
                    self.root.value = pointer
                    node.right = self.remove(pointer, node.right)
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
        self.check_balance(self.root, self.root)
        return node

    def rotation_simple_right(self, father, node): #simple a direita
        pointer = node.left 
        node.left = pointer.right
        pointer.right = node
        if node == self.root:
            self.root = pointer
        else:
            if (father.left == node):
                father.left = pointer
            else:
                father.right = pointer
        return pointer
        
    def rotation_simple_left(self, father, node): #simples a esquerda
        pointer = node.right
        node.right = pointer.left
        pointer.left = node
        if node == self.root:
            self.root = pointer
        else:
            if (father.left == node):
                father.left = pointer
            else:
                father.right = pointer
            
        return pointer
    
    def rotation_double_left(self, father, node): 
        self.rotation_simple_right(node, node.right)
        return self.rotation_simple_left(father, node)
    
    def rotation_double_right(self,father, node): 
        self.rotation_simple_left(node, node.left)
        return self.rotation_simple_right(father, node)
    
    def depth(self, node):
        if not(node):
            return 0
        depth_left = 0
        depth_right = 0
        if (node.left):
            depth_left= self.depth(node.left)
        if (node.right):
            depth_right= self.depth(node.right)
        if (depth_right > depth_left):
            return depth_right + 1
        return (depth_left + 1)

    def balancing_factor(self, node):
        if not(node):
            return 0
        else:
            height_left = 0
            height_right = 0
            if (node.left):
                height_left = self.depth(node.left)
            if (node.right):
                height_right = self.depth(node.right)
            return (height_left - height_right )
    
    def execute_balance(self,father, node, parent = None):
        fb = self.balancing_factor(node)
        if (fb > 1):
            if (self.balancing_factor(node.left) > 0):
                self.rotation_simple_right(father, node)
            if (self.balancing_factor(node.left) < 0):
                self.rotation_double_right(father, node)
        if (fb < -1):
            if (self.balancing_factor(node.right) <= 0):
                self.rotation_simple_left(father, node)
            if (self.balancing_factor(node.right) > 0):
                self.rotation_double_left(father, node)
        return node

    def check_balance(self, father, node):
        if (node):
            if (node.right):
                self.check_balance(node, node.right)
            if (node.left):
                 self.check_balance(node, node.left)
        return self.execute_balance(father, node)
 
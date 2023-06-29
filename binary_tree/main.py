from Binary_tree import *

# a = Binary_tree(20)
# a.insert(17)
# a.insert(24)
# # a.insert(16)
# # a.insert(18)
# # a.insert(23)
# # a.insert(26)p

# print(a.height())

# a.print_tree()
# print()
# print(a.height())



# print(b.balancing_factor(b.root))
# print(b.height(b.root.left))
# print(b.profundidade(b.root))
# print(b.height(b.root.right))
# b.balancing_factor(b.root.left)
# print(b.height(b.root.left.left))
# b.rotation_LL(b.root)
# b.execute_balance(b.root)
# print(b.balancing_factor(b.root))
# b.print_tree()
# print(b.level())



# print(len(b))


# print('pre ordem')
# a.pre_order()
# print()

# print('em ordem')
# a.in_order()
# print()

# print('pos ordem')
# a.post_order()
# print()

# print("Maior valor: ")
# a.max_value()
# print("Menor valor: ")


# pré-ordem a seqüência árvore seria 20, 17, 16, 18, 24, 23, 26; 
# intra-ordem, 16, 17, 18, 20, 23, 24, 26; 
# pós-ordem, 16, 18, 17, 23, 26, 24, 20


#                 (20)
#       (17)               (24)
# (16)      (18)      (23)      (26)
# a.remove(20)
# a.remove(17)
# print(a.max_value())
# a.print_tree()
# # a.level_route()
# a.remove(18)

# -------(20)
# ---(17)-----(24)
# (16)-(12)-(12)-(12)

b= Binary_AVL(15)
b.insert(27)
b.insert(49)
b.insert(10)
b.insert(8)
b.insert(67)
b.insert(59)
b.insert(9)
b.insert(13)
b.insert(20)
b.insert(14)

# b = Binary_AVL(50)
# b.insert(70)
# b.insert(30)
# b.insert(10)
# b.insert(40)
# b.insert(35)

# print(b.depth(b.root))

# print(b.balancing_factor(b.root.left))
# b.rotation_LL(b.root)
# b.execute_balance(b.root)
b.print_tree()
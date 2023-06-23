from Binary_tree import *

a = Binary_tree(20)
a.insert(17)
a.insert(24)
a.insert(16)
a.insert(18)
a.insert(23)
a.insert(26)
a.insert(22)


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
a.remove(20)
# print(a.max_value())
a.print_tree()
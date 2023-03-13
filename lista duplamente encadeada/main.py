from Doubly_linked_list import *

lista = Doubly_linked_list()
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(6)
lista.append(7)
lista.append(8)
lista.append(9)

lista.insert(0,1)
lista.insert(4,5)
lista.insert(100, 10)
lista.pop()

lista.remove(9)

print(lista)

print(len(lista))

print(lista.index(7))

from Queue  import *

a = Queue()
for cont in range(1,6):
    a.add(cont)

for cont in range(3):
    a.remove()
    
print(a)
print(len(a))
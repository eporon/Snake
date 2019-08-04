class node:
    def __init__(self,positionx=None,positiony=None,next = None):
        self.positionx = positionx
        self.positiony = positiony
        self.next = next

class Stack: 
    def __init__(self):
        self.head = None

    def Push(self, positionx,positiony):
        self.head = node(positionx=positionx,positiony=positiony, next=self.head) 

    def is_empty(self):
        return self.head == None

    def Pop(self):
        self.head = self.head.next

    def printlist(self):
     aux = self.head
     while aux:
      print(aux.positionx, end ="->")
      aux = aux.next

pila = Stack()
pila.Push(1,2)
pila.Push(2,1)
pila.Push(3,1)
pila.printlist()
print('\n')
pila.Pop()
pila.printlist()
print('\n')
class node:
    def __init__(self,name=None,score=None,next=None):
        self.name =name
        self.score =score
        self.next = next

class Queue: 
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def Enqueue(self, name,score):
        if not self.head:
            self.head = node(name=name,score=score)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(name=name,score=score)

    def Dequeue(self):
        self.head = self.head.next

    def printlist(self):
     aux = self.head
     while aux:
      print(aux.score, end ="->")
      aux = aux.next



cola = Queue()
cola.Enqueue('Pedro',1)
cola.Enqueue('Pedro',2)
cola.Enqueue('Pedro',3)
cola.Enqueue('Pedro',4)
cola.Enqueue('Pedro',5)
cola.printlist()
print('\n')
cola.Dequeue()
cola.Enqueue('Pedro',6)
cola.printlist()
print('\n')

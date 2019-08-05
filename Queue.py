class node:
    def __init__(self,name=None,score=None,next=None):
        self.name =name
        self.score =score
        self.next = next

class Queue: 
    def __init__(self):
        self.head = None

    def is_empty(self): #Pregunta si esta vacia
        return self.head == None

    def Enqueue(self, name,score): #Encola agregando al final
        if not self.head:
            self.head = node(name=name,score=score)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(name=name,score=score)

    def Dequeue(self): #Desencola de la cabeza
        self.head = self.head.next

    def printlist(self): #Imprime la cola
     aux = self.head
     while aux:
      print(aux.score, end ="->")
      aux = aux.next

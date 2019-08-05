class node:
    def __init__(self,positionx=None,positiony=None,next = None):
        self.positionx = positionx
        self.positiony = positiony
        self.next = next

class Stack: 
    def __init__(self):
        self.head = None

    def Push(self, positionx,positiony):  #Agrega en Cabeza
        self.head = node(positionx=positionx,positiony=positiony, next=self.head) 

    def is_empty(self): #Pregunta si esta vacia
        return self.head == None

    def Pop(self): #Saca la Cabeza para que sea LIFO
        self.head = self.head.next

    def printlist(self): #Imprime la Pila
     aux = self.head
     while aux:
      print(aux.positionx, end ="->")
      aux = aux.next

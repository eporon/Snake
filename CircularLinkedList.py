class node:
    def __init__(self,name=None,score=None,next=None,prior =None):
        self.name =name
        self.next = next
        self.prior = prior


class CircularLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
    
    def is_Empty(self):
        if self.first ==None:
            return True
        else:
            return False

    def add(self, name):
        if self.is_Empty():
            self.first =self.last = node(name=name)
        else:
            aux =node(name=name)
            aux.next =self.first
            self.first.prior =aux
            self.first =aux
        self.linknode()

    def search(self,name):
        aux = self.first
        while aux:
            if aux.name ==name:
                return True
            else:
                aux = aux.next
                if aux == self.first:
                    return False

    def add_last(self,name):
        if self.is_Empty():
            self.first = self.last = node(name=name)
        else:
            aux = self.last
            self.last =aux.next =node(name =name)
            self.last.prior =aux
        self.linknode()

    def linknode(self):
        if self.first !=None:
            self.first.prior =self.last
            self.last.next =self.first

    
    def startnode(self):
        aux = self.first
        while aux:
            print(aux.name)
            aux = aux.next
            if aux == self.first:
             break
    
    def finishnode(self):
        aux = self.last
        while aux:
            print(aux.name)
            aux = aux.prior
            if aux == self.last:
             break
    
    def deleteStart(self):
        if self.is_Empty():
            print("The data struct is empty")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first =self.first.next
        self.linknode()

    def deleteFinish(self):
        if self.is_Empty():
            print("The data struct is empty")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.last =self.last.prior
        self.linknode()
     



lista = CircularLinkedList()


lista.add_last('a')
lista.add_last('e')
lista.add_last('i')
lista.add_last('o')
lista.add_last('u')

lista.startnode()
print("*"*25)
lista.finishnode()

        
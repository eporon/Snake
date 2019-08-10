import os
import Open_Files
from Open_Files import open_file,start_file

class node:
    def __init__(self,name=None,score=None,next=None,prior =None):
        self.name =name
        self.next = next
        self.prior = prior


class CircularLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.item = None

    def nextitem(self): #Devuelve el nombre siguiente al actual
        if self.item ==None:
            self.item = self.first
            return self.item.name
        else:
            self.item = self.item.next
            return self.item.name

    def prioritem(self): #Devuelve el nombre anterior al actual
        if self.item != None:
            self.item = self.item.prior
            return self.item.name

    def is_Empty(self): #Verifica si esta vacia la lista
        if self.first ==None:
            return True
        else:
            return False

    def add(self, name):  #Agrega el valor al inicio de la lista circular
        if self.is_Empty():
            self.first =self.last = node(name=name)
        else:
            aux =node(name=name)
            aux.next =self.first
            self.first.prior =aux
            self.first =aux
        self.linknode()



    def search(self,name): #Verifica si el usuario se encuentra en la lista
        aux = self.first
        while aux:
            if aux.name ==name:
                return True
            else:
                aux = aux.next
                if aux == self.first:
                    return False

    def add_last(self,name):  #Agrega el valor al final de la lista circular
        if self.is_Empty():
            self.first = self.last = node(name=name)
        else:
            aux = self.last
            self.last =aux.next =node(name =name)
            self.last.prior =aux
        self.linknode()

    def linknode(self): #Une los nodos respecto 
        if self.first !=None:
            self.first.prior =self.last
            self.last.next =self.first

    
    def startnode(self): #Imprime la lista desde el inicio
        aux = self.first
        while aux:
            print(aux.name)
            aux = aux.next
            if aux == self.first:
             break
    
    def finishnode(self): #Imprime la lista desde el final
        aux = self.last
        while aux:
            print(aux.name)
            aux = aux.prior
            if aux == self.last:
             break
    
    def deleteStart(self): #Elimina el nodo inicial
        if self.is_Empty():
            print("The data struct is empty")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first =self.first.next
        self.linknode()

    def deleteFinish(self): #Elimina el nodo Final
        if self.is_Empty():
            print("The data struct is empty")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.last =self.last.prior
        self.linknode()

    def Report_User(self): #Genera el Archivo .dot para la lista circular doble enlazada y Genera la Imagen
            nodonum =0
            #f_output = open(rutadeubicacion+'\\Report_Users.txt','w')
            f_output = open('Report_Users.txt','w')
            f_output.write("digraph{\n node[shape = record,style=filled, color = lightgray];")
            f_output.write("label = \"Circular Linked List of Users\"; \n")
            f_output.write("\n")
            
            aux = self.first
            while aux:
                f_output.write("\t\t d%d[label=\"%s\"];\n"%(nodonum,aux.name))
                aux = aux.next
                nodonum+=1
                if aux == self.first:
                 break
            f_output.write("{rank=same")
            for i in range(0,(nodonum//2)+1):
                 f_output.write("d%d; d%d;"%(i,nodonum-1-i))
            f_output.write("}\n")

            for i in range(0,nodonum):
                if i ==nodonum-1:
                     f_output.write("\t\t d%d->d%d[color =\"yellow1\"];\n"%(i,0))
                     f_output.write("\t\t d%d->d%d[color =\"yellow1\"];\n"%(0,i))
                else:
                    f_output.write("\t\t d%d->d%d[color =\"yellow1\"];\n"%(i,i+1))
                    f_output.write("\t\t d%d->d%d[color =\"yellow1\"];\n"%(i+1,i))    
            f_output.write("\t }")        
            f_output.close()
            commandfile = 'dot -Tpng Report_Users.txt -o Report_Users.png'
            start_file(commandfile)
            path = 'Report_Users.png'
            open_file(path)
            

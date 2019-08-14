import os
import Open_Files
from Open_Files import open_file,start_file
class node:
    def __init__(self,positionx=None,positiony=None,next = None):
        self.positionx = positionx
        self.positiony = positiony
        self.next = next


class Stack:
    def __init__(self):
        self.head = None
        self.num = 0

    def Push(self, positionx,positiony):  #Agrega en Cabeza
        self.head = node(positionx=positionx,positiony=positiony, next=self.head)
        self.num+=1

    def is_empty(self): #Pregunta si esta vacia
        return self.head == None

    def Pop(self): #Saca la Cabeza para que sea LIFO
        self.head = self.head.next
        self.num-=1


    def printlist(self): #Imprime la Pila
     aux = self.head
     while aux:
      print("[%s,%s],"%(aux.positionx,aux.positiony), end ="->")
      aux = aux.next

    def Report_Stack(self): #Genera el Archivo .dot para la lista doble enlazada y Genera la Imagen
            nodonum =0

            f_output = open('Report_Stack.txt','w')
            f_output.write("digraph{\n node[shape = record,style=filled];")
            f_output.write("rankdir = LR;")
            f_output.write("label = \"SCORE\"; \n")
            f_output.write("\n")
            aux = self.head
            #Imprimir Nodos
            pila = "\tStack[label=\"<fnull>| "
            while aux:
                if(aux.next != None):
                    pila = pila + "<f%s>(%s,%s)|"%(nodonum,aux.positionx,aux.positiony)
                else:
                    pila = pila + "<f%s>(%s,%s)"%(nodonum,aux.positionx,aux.positiony)
                aux = aux.next
                nodonum+=1
            pila = pila + "\"];\n"
            f_output.write(pila)
            f_output.write("\t }")
            f_output.close()
            commandfile = 'dot -Tpng Report_Stack.txt -o Report_Stack.png'
            start_file(commandfile)
            path = 'Report_Stack.png'
            open_file(path)

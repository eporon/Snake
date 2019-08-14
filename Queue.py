import os
import Open_Files
from Open_Files import open_file,start_file
class node:
    def __init__(self,name=None,score=None,next=None):
        self.name =name
        self.score =score
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.noscore = 0

    def is_empty(self): #Pregunta si esta vacia
        return self.head == None

    def Enqueue(self, name,score): #Encola agregando al final
        self.noscore+=1
        if not self.head:
            self.head = node(name=name,score=score)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(name=name,score=score)

    def Dequeue(self): #Desencola de la cabeza
        self.head = self.head.next
        self.noscore-=1

    def printlist(self): #Imprime la cola
     aux = self.head
     while aux:
      print("%s,%s"%(aux.name,aux.score), end ="->")
      aux = aux.next

    def Report_ScoreBoard(self): #Genera el Archivo .dot para la lista doble enlazada y Genera la Imagen
            nodonum =0
            f_output = open('Report_ScoreBoard.txt','w')
            f_output.write("digraph{\n node[shape = record,style=filled];")
            f_output.write("label = \"SCOREBOARD\"; \n")
            f_output.write("\n")
            f_output.write("\t\t null[label=\"{NULL |}\"];\n")
            aux = self.head
            #Imprimir Nodos
            while aux:
                f_output.write("\t\t a%d[label=\"{(%s,%s) |}\"];\n"%(nodonum,aux.name,aux.score))
                aux = aux.next
                nodonum+=1
            #Enlazar Nodos
            for i in range(0,nodonum):
                if i != nodonum-1:
                     f_output.write("\t\t a%s->a%s[color=\"chocolate1\"];\n"%(i,i+1))
            f_output.write("\t\t a%s->null[color=\"chocolate1\"];\n"%(nodonum-1))
            f_output.write("\t }")
            f_output.close()

            commandfile = 'dot -Tpng Report_ScoreBoard.txt -o Report_ScoreBoard.png'
            start_file(commandfile)
            path = 'Report_ScoreBoard.png'
            open_file(path)

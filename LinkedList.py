import os
import Open_Files
from Open_Files import open_file,start_file

class Node:
    def __init__(self,datey,datex):
        self.next = None
        self.prior = None
        self.datex = datex
        self.datey = datey

    def See_Node(self):
        return self.datex
class LinkedList:

    def __init__(self):
        self.head = None
        self.last = None
        self.sizesnake = 0

    def is_Empty(self): #Pregunga si la lista esta vacia
        if self.head == None:
            return True
        else:
            return False
    def insert_first(self,datey,datex): #Inserta el nodo en la cabeza de la lista
        self.sizesnake+=1
        temp = Node(datey,datex)
        if self.is_Empty() == True:
            self.head = temp

        else:
            temp.next = self.head
            self.head.prior =temp
            self.head =temp
        aux = self.head
        while aux!=None:
            if(aux.next is None):
                self.last = aux
            aux = aux.next

    def delete_first(self):  #Elimina elementos desde la cabeza
        self.sizesnake-=1
        if self.is_Empty()==False:
            self.head = self.head.next
            self.head.prior = None

    def delete_last(self): #Elimina Elmenetos desde la cola
        self.sizesnake-=1
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prior.next = None

    def delete(self,pos): #Elimina Elementos desde determinada posicion
        self.sizesnake-=1
        prior = self.head
        current = self.head
        k=0
        if pos>0:
            while k !=pos and current.next !=None:
                prior = current
                current = current.next
                k+=1
            if k==pos:
                temp = current.next
                prior.next = current.next
                temp.prior = prior

    def list_node(self): #Lista los elementos desde la cabeza
        print('*'*10)
        temp = self.head
        print('[',end=' ')
        while temp!=None:
            print("[%s,%s],"%(temp.datey,temp.datex),end='')
            temp = temp.next
        print(']')

    def to_update(self,coordinatey,coordinatex): #Actualiza el snake mientras se mueve
        temp = self.head
        while temp!=None:
            temp.datey += coordinatey
            temp.datex += coordinatex
            temp = temp.next

    def insert_at_end(self,datey,datex): #Inserta elementos al final de la lista
        self.sizesnake+=1
        if self.head is None:
            new_node = Node(datey,datex)
            self.head = new_node
            self.last = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(datey,datex)
        n.next = new_node
        new_node.prior = n
        self.last = new_node

    def Evaluate_head(self): #Evalua que la posicion actual de la cabeza no haya chocado con alguna de sus partes
        temp = self.head.next
        while temp!=None:
            if(self.head.datex == temp.datex and self.head.datey ==temp.datey):
                return True
            temp = temp.next
        return False

    def Report_Snake(self): #Genera el Archivo .dot para la lista doble enlazada y Genera la Imagen
            nodonum =0
            f_output = open('Report_Snake.txt','w')
            f_output.write("digraph{\n node[shape = record,style=filled];")
            f_output.write("label = \"SNAKE\"; \n")
            f_output.write("\n")
            aux = self.head
            f_output.write("\t\t null0[label=\"{|NULL|}\"];\n")
            f_output.write("\t\t null1[label=\"{|NULL|}\"];\n")
            #Imprimir Nodos
            while aux:
                f_output.write("\t\t a%d[label=\"{|(%s,%s)|}\"];\n"%(nodonum,aux.datex,aux.datey))
                aux = aux.next
                nodonum+=1
            #Enlazar Nodos
            for i in range(0,nodonum):
                if i==0 and i != nodonum-1:
                     f_output.write("\t\t a%s->a%s[color=\"crimson\"];\n"%(i,i+1))
                elif(i!=nodonum-1):
                     f_output.write("\t\t a%s->a%s[color=\"crimson\"];\n"%(i,i+1))
                     f_output.write("\t\t a%s->a%s[color=\"crimson\"];\n"%(i,i-1))
                else:
                    if(i==nodonum-1 and i!=0):
                        f_output.write("\t\t a%s->a%s[color=\"crimson\"];\n"%(i, i-1))

            f_output.write("\t\t null0->a0[color=\"crimson\"];\n")
            f_output.write("\t\t a%s->null1[color=\"crimson\"];\n"%(nodonum-1))
            f_output.write("\t }")
            f_output.close()

            commandfile = 'dot -Tpng Report_Snake.txt -o Report_Snake.png'
            start_file(commandfile)
            path = 'Report_Snake.png'
            open_file(path)

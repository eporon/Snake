#Importacion de Sys
import sys
import os

#Importar libreria time para el uso de Hilos
import time

#Importacion de Estructuras para la utilizacion en el programa
import Stack
import Queue
import curses
import CircularLinkedList
from CircularLinkedList import CircularLinkedList
#Importacion del modulo de graficos curses
import ModGrafico 
from ModGrafico import print_menu,print_center,menu,print_users

#Importacion del modulo de carga de archivos
import bulkfile 
from bulkfile import CargarArchivo


#--------------------------------------------Estructuras a utilizar
listuser = CircularLinkedList()




def main(stdscr):
    global listuser 
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0
    print_menu(stdscr, current_row)
    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if(current_row == 0):
                menuuser =True
                print_users(stdscr, listuser.nextitem())
                while menuuser:
                    opcionuser = stdscr.getch()
                    if opcionuser == curses.KEY_LEFT:
                        print_users(stdscr,listuser.prioritem())
                    elif opcionuser == curses.KEY_RIGHT:
                        print_users(stdscr,listuser.nextitem())
                    else:
                        menuuser =False
            if(current_row == 1):
                pass
            if(current_row == 2):
                pass
            if(current_row == 3):
                listuser.Report_User()
            if(current_row == 4):    
                print_center(stdscr, "Cargando el Archivo...")                 
                listuser = CargarArchivo(namefile)
                time.sleep(3)
                print_center(stdscr, "Archivo Cargado")  
            if(current_row == 5):
                sys.exit()

            stdscr.getch()
            if current_row == len(menu)-1:
                break
        print_menu(stdscr, current_row)

namefile = input("Input name file: ")
curses.wrapper(main)






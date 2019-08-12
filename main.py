#Importacion de Modulos que serviran para tratar con la consola
import sys
import os

#Importar libreria time para el uso de Hilos
import time

#Importacion de Estructuras para la utilizacion en el programa
import Stack
from Stack import Stack
import Queue
from Queue import Queue
import curses
import CircularLinkedList
from CircularLinkedList import CircularLinkedList

#Importacion del modulo de graficos curses
import ModGrafico 
from ModGrafico import print_menu,print_center,menu,print_users

#Importacion del modulo de carga de archivos
import bulkfile 
from bulkfile import CargarArchivo

#Importacion del Modulo para manejar el snake
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, A_BOLD, A_UNDERLINE
from random import randint
print(KEY_UP, KEY_RIGHT, KEY_DOWN, KEY_LEFT)

import Food
from Food import Food


#--------------------------------------------Scope de variables tipo EDD a utilizar---------------------------------------------------
listuser = CircularLinkedList() #Lista para usuarios disponibles en el juego
listscore = Stack() #Pila que manejara el puntaje de los usuarios
listscoreBoard = Queue() #Cola Que maneja los ultimos 10 puntajes en el juego
menu = ['1. Play', '2. ScoreBoard', '3. User Selection', '4. Reports', '5. Bulk Loading', '6.Exit'] 

def playGame(stdscr):
    key = KEY_RIGHT
    score = 0
    count = 0
    food = Food()
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    print(h)
    print(w)
    stdscr.attron(A_BOLD)                                                            
    stdscr.border(0)  
    menustring ='Snake Reload'
    stdscr.addstr(0, w//2 - len(menustring)//2, menustring)    
    if food.type_food == 0:
        stdscr.addstr(food.y_coordinate,food.x_coordinate, "*")
    else:
        stdscr.addstr(food.y_coordinate,food.x_coordinate, "+")    
        stdscr.addstr(0, 10, 'Score: %d '%score)  
        #stdscr.addstr(0,100, 'User: %s'%listuser.item.name)
    stdscr.attroff(A_BOLD)
    stdscr.refresh()

def main(stdscr):
    global listuser 
    
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.curs_set(0)
    current_row = 0
    #Imprime el menu en pantalla
    print_menu(stdscr, current_row)

    #Mantiene el hilo principal para Verificar la tecla ingresada para poder elegir un item del menu
    while 1:
        key = stdscr.getch() #TECLA INGRESADA

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if(current_row == 0): #ITEM SELECCIONADO PARA JUGAR
                playGame(stdscr)
            if(current_row == 1): #ITEM SELECCIONADO PARA EL SCOREBOARD
                pass
            if(current_row == 2): #ITEM SELECCIONADO PARA USER SELECTION
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
            if(current_row == 3): #ITEM SELECIONADO PARA REPORTS, AUN FALTA IMPLEMENTACION POR AHORA SOLO SE TIENE REPORTE DE USUARIOS
                listuser.Report_User()
            if(current_row == 4): #ITEM SELECCIONADO PARA CARGAR EL ARCHIVO CON EL NOMBRE QUE SE PIDE AL INICIO DEL PROGRAMA   
                print_center(stdscr, "Cargando el Archivo...")                 
                listuser = CargarArchivo(namefile)
                time.sleep(3)
                print_center(stdscr, "Archivo Cargado")  
            if(current_row == 5): #ITEM SELECCIONADO PARA SALIR DEL JUEGO
                sys.exit()
            stdscr.getch() #Pausa para reiniciar el ciclo          
            if current_row == len(menu)-1: #Para asegurar que el ciclo se cerro
                break
        print_menu(stdscr, current_row) #Imprime el estado final del programa

    

'''
--------------------------------------------------PROCESO DE EJECUCION DEL PROGRAMA-------------------------------------------------------
'''
namefile = input("Input name file: ")   #1. Se solicita el nombre por anticipado del archivo para la carga masiva
curses.wrapper(main) # Ejecucion del main






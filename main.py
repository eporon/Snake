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
import LinkedList
from LinkedList import LinkedList


#Importacion del modulo de graficos curses
import ModGrafico
from ModGrafico import print_menu,print_center,menu,print_users,print_Scoreboard, print_menuReports,menu,menuReport

#Importacion del modulo de carga de archivos
import bulkfile
from bulkfile import CargarArchivo

#Importacion del Modulo para manejar el snake
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, A_BOLD, A_UNDERLINE
from random import randint

#Importacion del paquete del juego
import snake
from snake import  playGame


#--------------------------------------------Scope de variables tipo EDD a utilizar---------------------------------------------------
listuser = CircularLinkedList() #Lista para usuarios disponibles en el juego
listscore = Stack()  #Pila que manejara el puntaje de los usuarios
listscoreBoard = Queue() #Cola Que maneja los ultimos 10 puntajes en el juego
snake = LinkedList()





def main(stdscr):
    global listuser,listuser,listscore
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.curs_set(0)
    current_row = 0
    current_rowR = 0
    #Imprime el menu en pantalla
    print_menu(stdscr, current_row)


    #Mantiene el hilo principal para Verificar la tecla ingresada para poder elegir un item del menu
    while 1:
        key = stdscr.getch() #TECLA INGRESADA
        if key == curses.KEY_UP and current_row > 0: #Sube la barra de seleccion
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1: #Baja la barra de seleccion
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]: #Boton para seleccionar opcion

            if(current_row == 0): #ITEM SELECCIONADO PARA JUGAR
                if(listuser.is_Empty()): #Ingresar usuario en caso de no haber
                    curses.endwin()
                    nameu = input("Input name default user: ")
                    listuser.add_last(nameu)
                if(listscore.num > 0):
                    for i in range(0,listscore.num):
                        listscore.Pop()
                if(snake.sizesnake >=0):
                    for i in range(0,snake.sizesnake):
                        snake.delete_last()
                    snake.sizesnake = 0
                playGame(listuser.item.name,listscore,listscoreBoard,snake)
                print(snake.sizesnake)
            if(current_row == 1): #ITEM SELECCIONADO PARA EL SCOREBOARD
                print_Scoreboard(stdscr, listscoreBoard)
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
                print_menuReports(stdscr, current_rowR)
                menuReportTrue = True
                while menuReportTrue:
                    keyR = stdscr.getch() #TECLA INGRESADA
                    if keyR == curses.KEY_UP and current_rowR > 0: #Sube la barra de seleccion
                        current_rowR -= 1
                    elif keyR == curses.KEY_DOWN and current_rowR < len(menuReport)-1: #Baja la barra de seleccion
                        current_rowR += 1
                    elif keyR == curses.KEY_ENTER or keyR in [10, 13]: #Boton para seleccionar opcion
                        if(current_rowR == 0):
                            listuser.Report_User()
                        if(current_rowR == 1):
                            listscore.Report_Stack()
                        if(current_rowR == 2):
                            listscoreBoard.Report_ScoreBoard()
                        if(current_rowR == 3):
                            snake.Report_Snake()
                        if(current_rowR == 4):
                            menuReportTrue =False
                        #stdscr.getch() #Pausa para reiniciar el ciclo
                        if current_rowR == len(menuReport)-1: #Para asegurar que el ciclo se cerro
                            break
                    print_menuReports(stdscr, current_rowR)

                #temp = listscore.printlist()
                #print('\n')
                #listscoreBoard.printlist()
            if(current_row == 4): #ITEM SELECCIONADO PARA CARGAR EL ARCHIVO CON EL NOMBRE QUE SE PIDE AL INICIO DEL PROGRAMA
                print_center(stdscr, "Espere Cargando el Archivo...")
                listuser = CargarArchivo(namefile)
                time.sleep(2)

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

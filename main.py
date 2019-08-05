#Importacion de Modulos que serviran para tratar con la consola
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


#--------------------------------------------Estructuras a utilizar---------------------------------------------------
listuser = CircularLinkedList()




def main(stdscr):
    global listuser 
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
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
                pass
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






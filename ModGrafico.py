'''
MODULO UTILIZADO PARA LA CREACION DE MENUS EN CONSOLA
'''

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, A_BOLD, A_UNDERLINE,textpad
from random import randint
menu = ['1. Play', '2. ScoreBoard', '3. User Selection', '4. Reports', '5. Bulk Loading', '6.Exit']
menuReport = ['1. Report of users', '2. Report of score', '3. Report ScoreBoard', '4. Report Snake','5.Return ']

#Funcion para imprimir el menu
def print_menu(stdscr, selected_row_idx):
   #Imprime el marco y Asigna al centro La palabra Main Menu
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.attron(A_BOLD)
    stdscr.border(0)
    menustring =' MAIN MENU '
    stdscr.addstr(0, w//2 - len(menustring)//2, menustring)
    stdscr.attroff(A_BOLD)

    #Agrega los items de cada menu
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            curses.initscr()
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

#Funcion para imprimir el menu Reporte
def print_menuReports(stdscr, selected_row_idx):
   #Imprime el marco y Asigna al centro La palabra Reports
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.attron(A_BOLD)
    stdscr.border(0)
    menustring =' REPORTS '
    stdscr.addstr(0, w//2 - len(menustring)//2, menustring)
    stdscr.attroff(A_BOLD)

    #Agrega los items de cada menu de Reportes
    for idx, row in enumerate(menuReport):
        x = w//2 - len(row)//2
        y = h//2 - len(menuReport)//2 + idx
        if idx == selected_row_idx:
            curses.initscr()
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def print_Scoreboard(stdscr, listscoreBoard):
   #Imprime el marco y Asigna al centro La palabra ScoreBoard
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.attron(A_BOLD)
    stdscr.border(0)
    menustring ='Scoreboard '
    stdscr.addstr(0, w//2 - len(menustring)//2, menustring)
    stdscr.attroff(A_BOLD)
    list = ['NAME -> SCORE']
    #Agrega los name y score
    aux = listscoreBoard.head
    while aux:
        list.append("%s -> %s"%(aux.name,aux.score))
        aux = aux.next
    for idx, row in enumerate(list):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        stdscr.addstr(y, x, row)
    stdscr.refresh()







#Funcion para agregar palabras al centro de la ventana
def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()





#Funcion para pintar la Seleccion de Usuarios
def print_users(stdscr,text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.attron(A_BOLD)
    stdscr.border(0)
    menustring ='USER SELECTION'
    stdscr.addstr(0, w//2 - len(menustring)//2, menustring)
    stdscr.attroff(A_BOLD)
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x,"<---  " + text + "  --->")
    stdscr.refresh()

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, A_BOLD, A_UNDERLINE
from random import randint

#import ModGrafico
menu = ['1. Play', '2. ScoreBoard', '3. User Selection', '4. Reports', '5. Bulk Loading', '6.Exit']


def print_menu(stdscr, selected_row_idx):
   
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.attron(A_BOLD)                                                            
    stdscr.border(0)  
    menustring =' MAIN MENU '
    stdscr.addstr(0, w//2 - len(menustring)//2, menustring)            
    stdscr.attroff(A_BOLD)   


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



def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

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


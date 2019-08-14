
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, A_BOLD, A_UNDERLINE
from random import randint
import LinkedList
from LinkedList import LinkedList
import Food
from Food import Food
import ModGrafico
from ModGrafico import print_center

def playGame(player,listscore,listscoreBoard,snake):
    stdscr = curses.initscr()
    win = curses.newwin(30, 120, 0, 0)
    win.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    win.nodelay(1)

    #Empieza Caminando hacia la derecha
    key = KEY_RIGHT

    #Variables del juego
    level = 1
    score = 0
    count = 0
    leveltrue = True
    levelspeed = 180

    #Inicializar el snake
    snake.insert_first(15,14)
    snake.insert_first(15,15)
    snake.insert_first(15,16)
    snake.insert_first(15,17)

    #Inicializa Primer Comida
    food = Food()
    if food.type_food == 0:
        win.addch(food.y_coordinate,food.x_coordinate, '*')
    else:
        win.addch(food.y_coordinate,food.x_coordinate, '+')                                                    # Assigns a character for that particular spot on the window where the food will start. Both index 0, and index 1, of Food will need the same char symbol. Think about it.

    #Play
    while key != 27:

        #Inicia la Ventana del Snake
        win.attron(A_BOLD)
        win.border(0)
        win.addstr(0, 15, ' Score : ' + str(score) + ' ')
        win.addstr( 0, 90, "Player: " + str(player)+ ' ' )
        win.addstr(0, 45, ' SNAKE RELOAD - level %s '%level)
        win.attroff(A_BOLD)

        #Velocidad de Nivel
        if(score == 5 and leveltrue): #Cambio de Nivel y aumento de velocidad
            leveltrue =False
            levelspeed-=90
            level+=1
        #Inicializa la velocidad
        speed = int(levelspeed - ((snake.sizesnake)/5 + (snake.sizesnake)/10) % 120)

        #función de tiempo de espera con hilos en torno a la velocidad
        win.timeout(speed)

        #contador de espacio recorrido snake
        count += 1

        #Listener que Controla los Eventos del Teclado al presionar teclas
        prevKey = key   #prevKey mantiene referencia a la ultima tecla presionada
        event = win.getch()
        key = key if event == -1 else event #-1 para no entradas y en casa de haber se la asigna a key

        #Pausar/Reanudar y Generar Report_Snake
        if key == ord(' '): #Devuelve ascii
            key = -1
            snake.Report_Snake()
            while key != ord(' '):
                key = win.getch()  #Hasta que se vuelva a presionar espacio continua con el hilo principal
            key = prevKey
            continue

        #Pregunta si la tecla presionada es una Tecla de Movimiento o Tecla para salir
        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
            key = prevKey  #prevKey mantiene referencia a la ultima tecla presionada


        #Inserta el valor al que la cabeza se movio para poder controlar si hubo choque con comida
        snake.insert_first(snake.head.datey+(key == KEY_DOWN and 1) + (key == KEY_UP and -1),snake.head.datex+(key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1))

        #Evalua si la cabeza choco con su cuerpo
        if (snake.Evaluate_head()):
            break

        #Evalua si la cabeza choco con el marco
        if snake.head.datex ==0 or snake.head.datex ==119 or snake.head.datey == 0 or snake.head.datey == 29:
            curses.beep()
            break


        #Evalua si la cabeza del snake Chocho con comida
        if snake.head.datex == food.x_coordinate and snake.head.datey == food.y_coordinate :
            #Verifica si la comida es mala
            if food.type_food == 0:
                temp = snake.head
                #Si la lista no esta vacia borra un nodo y limpia la ventana
                if(listscore. is_empty() == False):
                    listscore.Pop()
                while temp!=None:
                    win.addch(temp.datey,temp.datex, ' ')
                    temp = temp.next
                snake.delete_last()
                snake.delete_last()
                if(score>0): #Elimina puntos si tiene
                    score-=1
            #Si la comida es Buena Agrega nodo y suma puntos
            else:
                listscore.Push(food.x_coordinate,food.y_coordinate)
                score += 1

            #Se Elimina la comida y se verifica que la comida generada no sea en el cuerpo del snake
            food = []
            while food == []:
                food = Food()
                snakep =snake.head
                while snakep!=None:
                    if food.x_coordinate==snakep.datex and food.y_coordinate==snakep.datey :
                        food = []
                        break;
                    snakep = snakep.next

            #Agrega la comida generada ya sea buena o mala en la ventana
            if food.type_food == 0:
                win.addch(food.y_coordinate,food.x_coordinate, '*')
            else:
                win.addch(food.y_coordinate,food.x_coordinate, '+')
        else: #Si el valor agregado no fue comida entonces limpia la ventana y quita el valor extra agregado
            temp = snake.head
            while temp!=None:
                win.addch(temp.datey,temp.datex, ' ')
                temp = temp.next
            snake.delete_last()

        #Redibuja el Snake
        win.addch(snake.head.datey, snake.head.datex, '■')
        temp = snake.head.next
        while temp!=None:
            win.addch(temp.datey,temp.datex, '#')
            temp = temp.next
    #fin de ventana
    curses.endwin()

    #Una vez terminado el juego agrega a scoreboard y controla que no sobrepase los 10
    listscoreBoard.Enqueue(player,score)
    if(listscoreBoard.noscore>10):
        listscoreBoard.Dequeue()

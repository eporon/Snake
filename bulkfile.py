'''
MODULO UTILIZADO PARA LA CARGA DE ARCHIVOS
'''
import os
from CircularLinkedList import CircularLinkedList

#Funcion que devuelve la lista una lista circular de usuarios pasandole como parametro el nombre del archivo
def CargarArchivo(nombrearchivo):
    '''
    Esto solo funciona en Windows
    '''
    #rutadeubicacion = os.path.dirname(os.path.abspath(__file__)) #El archivo debe encontrarse en el mismo directorio que bulfile.py
    listacarga = CircularLinkedList()
    try:
        #f_input  = open(rutadeubicacion+'\\'+ nombrearchivo +'.csv','r')
        f_input  = open(nombrearchivo +'.csv','r')
        print(f_input.readlines(1)) #Lee el encabezado en caso de haber
        for line in f_input:
            line = line.strip()
            listacarga.add_last(line)
        f_input.close()
        return listacarga
    except IOError:
        print('Su archivo de carga No existe')

import os
from CircularLinkedList import CircularLinkedList

def CargarArchivo(nombrearchivo):
    rutadeubicacion = os.path.dirname(os.path.abspath(__file__))
    listacarga = CircularLinkedList()
    try:
        f_input  = open(rutadeubicacion+'\\'+ nombrearchivo +'.csv','r') 
        print(f_input.readlines(1)) #Lee el encabezado en caso de haber
        for line in f_input:
            line = line.strip()
            listacarga.add_last(line)
        f_input.close()
        return listacarga
    except IOError:
        print('Su archivo de carga No existe en el directorio del archivo')



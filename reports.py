import os
rutadeubicacion = os.path.dirname(os.path.abspath(__file__))
def Report_User():
    try:
        f_output = open(rutadeubicacion+'\\Report_Users.txt','w')
        for line in f_input:
            line = line.strip()
            sentence = line.split(',')
            if 15<=int(sentence[1])<=30:
                f_output.write("El juego %s demoro %s minutos.\n"%(sentence[0],sentence[1]))
        f_output.close()
        os.system(rutadeubicacion+"\\archivo_201712132.txt")
    except IOError:
        print('El archivo puntajes no existe')


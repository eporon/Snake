import os
import subprocess
import platform

'''
El comando que puse en ruta de ubicacion solo sirve para Windows por eso no abria en tu Mac
'''
#rutadeubicacion = os.path.dirname(os.path.abspath(__file__))
#print(rutadeubicacion)
'''
Encontre esta forma de poder abrir un archivo sin importar el sistema operatio, para mac es Darwin
'''
def open_file( path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

def start_file( commandfile):
    if platform.system() == "Windows":
        os.system(commandfile)
    elif platform.system() == "Darwin":
        subprocess.call(commandfile, shell=True)
    else:
        os.system(commandfile)
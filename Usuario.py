from io import open
class Usuario:
    def __init__(self, usuario_info, contrasena_info):
        #aquí para ocupar todo lo de herencia como no xd 
        self.__usuario = nombre
        self.__contrasena = edad
        
    def getUsuario(self):
        return self.__usuario
    
    def getcontrasena(self):
        return self.__contrasena
    
    
    def setUsuario(self, nombre):
        self.__nombre = nombre
        
    def setcontrasena(self, edad):
        self.__edad = edad
        

  
    #guardar datos en archivo txt
    def guarEstu(self):
        data = [self.__usuario, self.__contrasena]
        contenido = str(data)
        fichero = open("login.txt", 'a')
        fichero.write("\n" + contenido + "\n")
        fichero.close()
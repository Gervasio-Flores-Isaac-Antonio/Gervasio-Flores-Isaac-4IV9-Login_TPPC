from io import open

class Persona:
    def __init__(self, boleta, edad, grupo, nombre):
        #aquí para ocupar todo lo de herencia como no xd 
        self.__nombre = nombre
        self.__edad = edad
        self.__boleta = boleta
        self.__grupo = grupo
     
    #GETTERS 
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getBoleta(self):
        return self.__boleta
    
    def getGrupo(self):
        return self.__grupo
    
    #SETTERS
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setEdad(self, edad):
        self.__edad = edad
        
    def setBoleta(self, boleta):
        self.__boleta = boleta

    def setGrupo(self, grupo):
        self.__grupo = grupo    
  
    #guardar datos en archivos txt
    def guarEstu(self):
        data = [self.__nombre, self.__boleta, self.__grupo, self.__edad]
        contenido = str(data)
        fichero = open("isaacDB.txt", 'a')
        fichero.write("\n" + contenido + "\n")
        fichero.close()
        
    def guarProf(self):
        data2 = [self.__nombre, self.__boleta, self.__grupo, self.__edad]
        contenido = str(data2)
        fichero = open("profesoresDB.txt", 'a')
        fichero.write("\n" + contenido + "\n")
        fichero.close()
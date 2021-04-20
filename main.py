from Persona import Persona
from tkinter import *
from tkinter import messagebox as MessageBox
import re
from io import open


class ControlEscolar(Toplevel):
    def __init__(self, master):
        self.master = master
        master.title("Registro Profesores y Alumnos")
        master.geometry('850x600')
        
        #TITULO
        self.titulo = Label()
        self.titulo.pack(anchor = CENTER)
        self.titulo.config(text="REGISTRO ESCOLAR PROFESORES Y ALUMNOS", fg = "#30486e", bg = "#7394c9",font = ("Comic Sans MS", 21))
        
        #HEADER
        self.ins = Label()
        self.ins.pack(anchor = CENTER)
        self.ins.config(text="Seleccione Boton Profesor o Estudiante", fg = "#30486e", bg = "#7394c9",font = ("Comic Sans MS", 15))


        #BOTONES
        #***********************************************************************
        #Estudiante
        self.estu = Button(master, text = "Estudiante", command = self.btn_es)
        self.estu.place(x= 70, y = 90, width = 120, height = 60)
        self.estu.config(fg = "#1c1f1f", font = ("Comic Sans MS", 17), bg ="#76c8cc")
        
        #PROFESOR
        self.pro = Button(master, text = "Profesor", command = self.btn_pr)
        self.pro.place(x = 70, y = 155, width= 120, height=60)
        self.pro.config(fg = "#1c1f1f", font = ("Comic Sans MS", 17), bg ="#76c8cc")
               
        #GUARDA EN ARCHIVO
        self.reg = Button(master, text="Registrar", command=self.btn_re)
        self.reg.place(x = 450, y = 430, width= 160, height=72)    #(x=70, y = 500, width= 160, height=72)
        self.reg.config(fg = "#1c1f1f", font = ("Comic Sans MS", 17), bg ="#76c8cc")
        
        #CONSULTA DATOS DE ARCHIVO GUARDADOS
        self.cam = Button(master, text = "Consulta", command = self.btn_co)
        self.cam.place(x = 70, y = 500, width = 160, height = 72)        #(x = 580, y=430, width = 160, height = 72)
        self.cam.config(fg = "#1c1f1f", font = ("Comic Sans MS", 17), bg ="#76c8cc")
        #***********************************************************************
        
        
        
        #ETIQUETAS VARIABLES
        self.lblboleta = StringVar()
        self.lblboleta.set("No. Boleta: ")
        
        self.lblgrupo = StringVar()
        self.lblgrupo.set("Grupo: ")

        self.lbledad = StringVar()
        self.lbledad.set("Edad: ")

#***********************************************************************
        #ETIQUETAS
        #ETIQUETA nombre
        self.nombre = Label()
        self.nombre.place(x = 200, y= 200)
        self.nombre.config(text = "Nombre y Apellido:", fg = "#3295a8", bg = "#120b75",font = ("Comic Sans MS", 17))

        #ETIQUETA boleta
        self.boleta = Label()
        self.boleta.place(x = 200, y= 250)
        self.boleta.config(textvariable = self.lblboleta, fg = "#3295a8", bg = "#120b75",font = ("Comic Sans MS", 17))

        #ETIQUETA grupo
        self.grupo = Label()
        self.grupo.place(x = 200, y = 300)
        self.grupo.config(textvariable = self.lblgrupo, fg = "#3295a8", bg = "#120b75",font = ("Comic Sans MS", 17))

        #ETIQUETA edad
        self.edad = Label()
        self.edad.place(x=200, y=350)
        self.edad.config(textvariable = self.lbledad, fg = "#3295a8", bg = "#120b75",font = ("Comic Sans MS", 17))
        
 #***********************************************************************       
        #variables 
        self.name = StringVar()
        self.boleta = StringVar()
        self.grupo = StringVar()
        self.edad = StringVar()

        self.primero = Entry(textvariable = self.name)
        self.primero.place(x= 420, y = 200, width = 250, height = 30)

        self.segundo = Entry(textvariable = self.boleta)
        self.segundo.place(x = 420, y = 250, width = 250, height = 30)

        self.tercero = Entry(textvariable = self.grupo)
        self.tercero.place(x = 420, y = 300, width = 250, height = 30)

        self.cuarto = Entry(textvariable = self.edad)
        self.cuarto.place(x=420, y = 350, width=250, height=30)
#*********************************************************************** 
        #COMPORTAMIENTO DE BOTONES
        
        #BANDERAS
        self.estudiante = True
        self.profesor = False
        
    def btn_es(self):
        self.lblboleta.set("No. Boleta: "); 
        self.lblgrupo.set("Grupo: "); 
        self.lbledad.set("Edad: ")
        self.estudiante = True
        self.profesor = False
    def btn_pr(self):
        self.lblboleta.set("Materia: "); 
        self.lblgrupo.set("Grupos: "); 
        self.lbledad.set("Horas: ")
        self.estudiante = False
        self.profesor = True
    def btn_re(self):
        self.nombre = self.name.get()
        self.boleta = self.boleta.get()
        self.grupo = self.grupo.get()
        self.edad = self.edad.get()

#***********************************************************************        
        #VALIDACION DE INPUT TEXT
        pat1 = re.compile(r'\D{3,30}')
        pat2 = re.compile(r'\d{1,3}')
        pat3 = re.compile(r'\w{4,15}')
 
 #***********************************************************************        
 
        self.numero = 0
        
        if(pat1.match(self.nombre)):
            self.numero += 1
        else:
            MessageBox.showerror("Error", "Ingrese Nombre campo 1")
            self.numero=0
            
        if(pat3.match(self.boleta)):
            self.numero += 1
        else:
            MessageBox.showerror("Error", "Ingrese Boleta en el campo 2")
            self.numero=0
            
        if(pat3.match(self.grupo)):
            self.numero +=1
        else:
            MessageBox.showerror("Error", "Ingrese Grupo campo 3")
            self.numero=0
            
        if(pat2.match(self.edad)):
            self.numero +=1
        else:
            MessageBox.showerror("Error", "Ingrese Edad campo 4")
            self.numero=0

        #SI ES 4 TODOS LOS CAMPOS FUERON LLENADOS
        if(self.numero == 4):
            if(self.estudiante == True):
                self.guard = Persona(self.nombre, self.boleta, self.grupo, self.edad)
                self.guard.guarEstu()
            if(self.profesor == True):
                self.guard2 = Persona(self.nombre, self.boleta, self.grupo, self.edad)
                self.guard2.guarProf()

#***********************************************************************         
 #PANTALLA DE CONSULTA DE DATOS DE LOS ARCHIVOS
    def btn_co(self):
        self.mostrar = Toplevel()
        self.mostrar.geometry('500x500')
        self.mostrar.configure(background = "#120b75")
        
        self.mostrar.etiqueta = Label(self.mostrar)
        self.mostrar.etiqueta.place(x = 20, y = 10)
        self.mostrar.etiqueta.config(text = "Profesores - Estudiantes", fg = "#3295a8", bg = "#120b75",font = ("Comic Sans MS", 17))
        
        
        #LEER ARCHIVO DE PROFESORES
        


        #LEER ARCHIVO DE PROFESORES
        self.le = Text(self.mostrar)
        self.le.place(x=30, y = 80)
        self.le.config(fg = "#3295a8", bg = "#120b75",font = ("Comic Sans MS", 12))

        #LEER ARCHIVO DE PROFESORES
        fichero = open("profesoresDB.txt", 'r+')
        contenido = fichero.read()
        self.le.delete(1.0,'end')
        self.le.insert('insert', contenido)
        fichero.close()


        #LEER ARCHIVO DE ALUMNOS
        self.le2 = Text(self.mostrar)
        self.le2.place(x=30, y = 320)
        self.le2.config(fg = "#3295a8", bg = "#120b75", font = ("Comic Sans MS", 12))
        
        
        #LEER ARCHIVO DE ALUMNOS
        fichero2 = open("isaacDB.txt", 'r+')
        contenido2 = fichero2.read()
        self.le2.delete(1.0,'end')
        self.le2.insert('insert', contenido2)
        fichero2.close()

        self.mostrar.resizable(True, True)

root = Tk()
root.resizable(False, False)
root.configure(background = "#120b75")
ControlEscolar(root)
root.mainloop()
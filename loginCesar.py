from Usuario import Usuario
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import re
from io import open
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)


class LoginCifradoCesar:
    def __init__(self, master):

        self.master = master
        master.title("Login")
        master.geometry('700x450')


#*******************************************************************************

        #ETIQUETAS
        self.etiqueta1 = Label()
        self.etiqueta1.pack(anchor = CENTER)
        self.etiqueta1.config(text="PANTALLA DE INICIO DE SESION", fg = "#b21f66", bg = "#7394c9",font = ("Comic Sans MS", 25))

        self.lblusuario = StringVar()
        self.lblusuario.set("Usuario: ")
        
        self.lblcontrasena = StringVar()
        self.lblcontrasena.set("Contrasena: ")

#*******************************************************************************

        self.usuariop = Label()
        self.usuariop.place(x=150,y=150)
        self.usuariop.config(textvariable = self.lblusuario, fg = "black", bg = "#7394c9",font = ("Comic Sans MS", 17))

        self.contrasena = Label()
        self.contrasena.place(x=150,y=220)
        self.contrasena.config(textvariable = self.lblcontrasena, fg = "black", bg = "#7394c9",font = ("Comic Sans MS", 17))


 #*******************************************************************************
 
        #BOTONES
        self.boton3 = Button(master, text="Decifrar", command = self.btn_decryp)
        self.boton3.place(x=170, y = 380, width= 160, height=50)
        self.boton3.config(fg = "#161925", font = ("Comic Sans MS", 12), bg ="#7394c9")

        self.boton2 = Button(master, text="Registrarse", command = self.btn_registro)
        self.boton2.place(x=270, y = 290, width= 160, height=72)
        self.boton2.config(fg = "#161925", font = ("Comic Sans MS", 12), bg ="#7394c9")
        

        self.boton1 = Button(master, text="Cifrado", command = self.btn_encryp)
        self.boton1.place(x=380, y = 380, width= 160, height=50)
        self.boton1.config(fg = "#161925", font = ("Comic Sans MS", 12), bg ="#7394c9")


#*******************************************************************************
       #INPUT BOX PARA USUARIO Y CONTRASENA 

        self.in_usuario = StringVar()
        self.in_contrasena = StringVar()

        self.primero = Entry(textvariable = self.in_usuario)
        self.primero.place(x= 350, y = 160)

        self.segundo = Entry(textvariable = self.in_contrasena, show="*")
        self.segundo.place(x = 350, y = 230)


#*****************************************************************************
    
       

#*****************************************************************************  

    def btn_registro(self):
        usuario_info = self.in_usuario.get()
        contrasena_info = self.in_contrasena.get()
        print(usuario_info,"\t", contrasena_info)
 
        messageUser = usuario_info
        messagePass = contrasena_info
        key = 16
        mode = 'e'
        
        print('usuario: ',messageUser)
        print('contrasena: ',messagePass)
        print('key: ',key)
        print('mode: ',mode)
        cifradoPass = getTranslatedMessage(mode, messagePass, key)
        cifradoUser = getTranslatedMessage(mode, messageUser, key)
        print(cifradoPass)
        print(cifradoUser)
 
        #GUARDADO EN ARCHIVO
        #Open and write data to a file
        file = open("pass.txt", "a")
        file.write(cifradoPass)
        file.write("\t\n")
        file.close()
        
        file = open("user.txt", "a")
        file.write(cifradoUser)
        file.write("\t\n")
        file.close()
        MessageBox.showinfo("Exito al Registrar!!", "Contrasena Cifrada!")
#*****************************************************************************  

    def btn_decryp(self):
        self.mostrar = Toplevel()
        self.mostrar.geometry('500x500')
        self.mostrar.configure(background = "#7394c9")
        self.mostrar.etiqueta = Label(self.mostrar)
        self.mostrar.etiqueta.place(x = 20, y = 20)
        self.mostrar.etiqueta.config(text = "Contrasena Decifrada", fg = "black", bg = "#7394c9",font = ("Comic Sans MS", 17))
         
         #LEER ARCHIVO DE user       
        self.le = Text(self.mostrar)
        self.le.place(x=30, y = 80)
        self.le.config(fg = "black", bg = "#7394c9",font = ("Comic Sans MS", 17))

        fichero = open("user.txt", 'r+')
        contenido = fichero.read()
        message = contenido
        key = 16
        mode = 'd'
        print('contrasena: ',message)
        print('key: ',key)
        print('mode: ',mode)
        
        contenidoUser = getTranslatedMessage(mode, message, key)
        self.le.delete(1.0,'end')
        self.le.insert('insert', contenidoUser)
        fichero.close()
       
       
        #LEER ARCHIVO DE pass
        fichero = open("pass.txt", 'r+')
        self.le2 = Text(self.mostrar)
        self.le2.place(x=30, y = 320)
        self.le2.config(fg = "#3295a8", bg = "#120b75", font = ("Comic Sans MS", 12))
                
        #LEER ARCHIVO DE pass
        fichero2 = open("pass.txt", 'r+')
        contenido2 = fichero2.read()
        
        message = contenido2
        key = 16
        mode = 'd'
        
        print('contrasena: ',message)
        print('key: ',key)
        print('mode: ',mode)
        
        contenidoPass = getTranslatedMessage(mode, message, key)
        
        
        self.le2.delete(1.0,'end')
        self.le2.insert('insert', contenidoPass)
        fichero2.close()
       
       
        self.mostrar.resizable(True, True)
       
       
       
       
        
 #*****************************************************************************      
        #CONSULTA DE DATOS DE USUARIO LOGIN
    def btn_encryp(self):
        self.mostrar = Toplevel()
        self.mostrar.geometry('500x500')
        self.mostrar.configure(background = "#7394c9")
        self.mostrar.etiqueta = Label(self.mostrar)
        self.mostrar.etiqueta.place(x = 20, y = 20)
        self.mostrar.etiqueta.config(text = "Contrasena Cifrada", fg = "black", bg = "#7394c9",font = ("Comic Sans MS", 17))
         
         #LEER ARCHIVO DE user       
        self.le = Text(self.mostrar)
        self.le.place(x=30, y = 80)
        self.le.config(fg = "black", bg = "#7394c9",font = ("Comic Sans MS", 17))

        fichero = open("user.txt", 'r+')
        contenido = fichero.read()
        self.le.delete(1.0,'end')
        self.le.insert('insert', contenido)
        fichero.close()
       
        #LEER ARCHIVO DE pass
        fichero = open("pass.txt", 'r+')
        self.le2 = Text(self.mostrar)
        self.le2.place(x=30, y = 320)
        self.le2.config(fg = "#3295a8", bg = "#120b75", font = ("Comic Sans MS", 12))
                
        #LEER ARCHIVO DE pass
        fichero2 = open("pass.txt", 'r+')
        contenido2 = fichero2.read()
        self.le2.delete(1.0,'end')
        self.le2.insert('insert', contenido2)
        fichero2.close()
       
       
        self.mostrar.resizable(True, True)
        
def getTranslatedMessage(mode, message, key):

    if mode[0] == 'd':

        key = -key

    translated = ''



    for symbol in message:

        if symbol.isalpha():

            num = ord(symbol)

            num += key



            if symbol.isupper():

                if num > ord('Z'):

                    num -= 26

                elif num < ord('A'):

                    num += 26

            elif symbol.islower():

                if num > ord('z'):

                    num -= 26

                elif num < ord('a'):

                    num += 26



            translated += chr(num)

        else:

            translated += symbol

    return translated
        
        
        
        

root = Tk()
root.resizable(False, False)
root.configure(background = "#7394c9")
LoginCifradoCesar(root)
root.mainloop()


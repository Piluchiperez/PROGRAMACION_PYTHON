from tkinter import *
from tkinter import messagebox

raiz=Tk()

raiz.title("Proyecto CRUD")
miMenu=Menu(raiz)
raiz.config(menu=miMenu)
#----------Ventana-------------
miVentana=Frame()
miVentana.pack()
miVentana.config(bg="cyan", width=600, height=500)

# ------------ mensajes emergentes-----------con parámetros
def infoDocu(ms1, ms2):   
    messagebox.showinfo(ms1,ms2)

def alertaRecomendados():
    messagebox.showwarning("Recomendados!","Estate atento a las ofertas")

def salirAplicacion():
    valor=messagebox.askokcancel("Salir","¿Deseas salir de la aplicación?")
    if valor:
        raiz.destroy()
    
def cerrarDocumento():
    valor=messagebox.askretrycancel("reintentar","No es posible cerrar")
    if valor==False:
        raiz.destroy()

def opcionconectar():
    pass

#---------Menú y submenus-------------
bbdd=Menu(miMenu, tearoff=0)
bbdd.add_command(label="Conectar", command=opcionconectar)
bbdd.add_separator()
bbdd.add_command(label="Salir", command=salirAplicacion)

borrar=Menu(miMenu, tearoff=0)  #añadir mensaje confirmacion

crud=Menu(miMenu,tearoff=0)
crud.add_command(label="Crear")
crud.add_command(label="Leer")
crud.add_command(label="Actualizar")
crud.add_command(label="Eliminar")

ayuda=Menu(miMenu, tearoff=0)
ayuda.add_command(label="Versión", command=lambda:infoDocu("Información sobre la Versión","Versión 1.0"))
ayuda.add_command(label="Documentación", command=lambda:infoDocu("Documentación","http://www.docu.com"))

miMenu.add_cascade(label="BBDD", menu=bbdd)
miMenu.add_cascade(label="Limpiar formulario", menu=borrar)
miMenu.add_cascade(label="CRUD", menu=crud)
miMenu.add_cascade(label="Ayuda", menu=ayuda)


miId=StringVar()
cuadroMiId=Entry(miVentana, textvariable=miId)
cuadroMiId.grid(row=0, column=1,pady=3,padx=3)
cuadroMiId.config()

MiIdLabel=Label(miVentana,text="ID: ",)
MiIdLabel.grid(row=0, column=0, sticky="e", pady=3,padx=3)
#el parámetro sticky define cómo se alineará el elemento gráfico en el grid.
#sticky="e"

miNombre=StringVar()
cuadroMiNombre=Entry(miVentana,textvariable=miNombre)
cuadroMiNombre.grid(row=1,column=1,pady=3,padx=3)
cuadroMiNombre.config()

miNombreLabel=Label(miVentana,text="Nombre usuario: ")
miNombreLabel.grid(row=1, column=0, sticky="e", pady=3,padx=3)

miPass=StringVar()
miPassLabel=Label(miVentana, text="Password: ")
miPassLabel.grid(row=3, column=0, sticky="e", padx=3, pady=3)


cuadroMiPassword=Entry(miVentana,textvariable=miPass)
cuadroMiPassword.grid(row=3, column=1,pady=3,padx=3)
cuadroMiPassword.config(show="*")




raiz.mainloop()

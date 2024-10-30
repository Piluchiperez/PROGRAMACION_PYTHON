import sqlite3
from tkinter import messagebox

def opcionconectar():
    miConexion=sqlite3.connect("BaseCRUD.bd")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            create table USUARIOS (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NOMUSUARIO VARCHAR(50),
                        PASSWORD VARCHAR(10),
                        APELLIDOS VARCHAR(50),
                        DIRECCION VARCHAR(50),
                        COMENTARIOS VARCHAR(100))
                        '''  )
        pintaMensaje("Información","Tabla usuarios creada con éxito.")
    except:
        pintaMensaje("Información","La tabla ya está creada.")
    

def pintaMensaje(ms1, ms2):
    messagebox.showinfo(ms1, ms2)
        

def grabar(registro):
	print(registro[:])
     
def leer(miId):
     miCursor.execute("select * from usuarios where miId=Id")
     
     
	
	
	
	
# @   try:
#		miCursor.execute("insert into USUARIOS values (null)")
#		pintamensaje("Información","Registro añadido con éxito")
#	except:
#		pintamensaje("Información","Registro no grabado")
		

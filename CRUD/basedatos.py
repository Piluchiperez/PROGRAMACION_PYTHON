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
    miConexion=sqlite3.connect("BaseCRUD.bd")
    miCursor=miConexion.cursor()    
    miCursor.execute("select * from usuarios where miId=Id")
    return miCursor.fetchone()

def modificar(registro):
    miConexion=sqlite3.connect("BaseCRUD.bd")
    miCursor=miConexion.cursor()    
    miCursor.execute('''
                     update usuarios set nomusuario = registro[1], 
                     password=registro[2], 
                     apellidos=registro[3], 
                     direccion=registro[4], 
                     comentarios=registro[5] 
                     from usuarios where Id=registro[0]''')
    
def borrar(miId):
    miConexion=sqlite3.connect("BaseCRUD.bd")
    miCursor=miConexion.cursor()    
    miCursor.execute("delete * from usuarios where miId=Id") 
    
    
    

     
     
	
	
	
	
# @   try:
#		miCursor.execute("insert into USUARIOS values (null)")
#		pintamensaje("Información","Registro añadido con éxito")
#	except:
#		pintamensaje("Información","Registro no grabado")
		

from os import system
from sqlite3 import connect
from re import search
from datetime import datetime
import socket
from tcppinglib import tcpping



def conexion():
    con = connect("bd_sucursal.db")
    return con

def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = """CREATE TABLE tabla_ping
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre,
             descripcion,
             puerto
             )
         """
    cursor.execute(sql)
    con.commit()
    ## TABLA 2 ##
    sql = """CREATE TABLE tabla_estado
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre,
             descripcion,
             puerto
             )
         """
    cursor.execute(sql)
    con.commit()

try:
    conexion()
    crear_tabla()
    
except:
    print("bd_proyecto/tabla_ping/tabla_estado")


def ver(tabla, tree):
    guardado = tree.get_children()
    for elementos in guardado: 
        tree.delete(elementos)
    sql = "SELECT * FROM "+tabla
    print(sql)
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)
    resultado = datos.fetchall()
    for fila in resultado:
        tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))

def guardar(tabla,nombre,descripcion, puerto, tree):
    sql= "INSERT INTO "+tabla+" (nombre, descripcion, puerto) VALUES (?, ?, ?)"
    print(sql)
    data = (nombre.get(), descripcion.get(), puerto.get())
    con=conexion()
    cursor=con.cursor()
    cursor.execute(sql, data)
    con.commit()
    ver(tabla,tree)  

def borrar(tabla, tree):
    valor = tree.selection()
    item = tree.item(valor)
    id = item['text']
    con=conexion()
    cursor=con.cursor()
    data = (id,)
    sql = "DELETE FROM "+tabla+" WHERE id = ?;"
    print(sql)
    cursor.execute(sql, data)
    con.commit()
    ver(tabla, tree)  

def ping(text_0, label, text_1, text_2):
    text_0.delete("1.0","end")
    sql = "SELECT * FROM tabla_ping"
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)
    resultado = datos.fetchall()
    for fila in resultado:
        respuesta=tcpping(address= fila[2], port= fila[3], count=1)
        indice=text_0.index("end")
        indice_2=text_2.index("end")
        if respuesta.is_alive == True:
            text_0.insert(indice, fila[1]+ "  Conectado  ✔\n")
            text_1.delete("1.0","end")
            text_1.insert("end",respuesta)
        else:
            text_0.insert(indice ,fila[1]+ "  Desconectado  ⚠\n")
            tiempo=datetime.now()
            text_2.insert(indice_2, str(tiempo)+" "+ fila[1]+"\n")
    
    patron = search('Desconectado', text_0.get("1.0","end"))
    if patron == None: 
        label.config(text="Servidor ✅",foreground="green")  
    else:
        label.config(text="Servidor ⚠",foreground="red")  
        
    return text_0, label, text_1, text_2
   
 


    
    
  



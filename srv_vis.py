from tkinter import Frame
from tkinter import Label
from tkinter import Text
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
from tkinter import ttk
from tkinter import Tk
from tkinter import Menu
from srv_mod import guardar
from srv_mod import borrar
from srv_mod import ver
from srv_mod import ping
import threading




def vista(monitor):
    
    monitor.title("SERVIDORES")
    monitor.geometry("1000x540")

    frame1= Frame(monitor, borderwidth=5, relief="groove")
    frame1.pack(side="left",fill="y")
    
    ## URL ##
    label=Label(frame1, text="Servidor")
    label.grid(row=0,column=0)

    text_0=Text(frame1,wrap="word", height=37, 
                width=40, bg="#dcdcdc", padx=5, 
                pady=5, relief="groove", foreground="black")
    text_0.grid(row=1,padx=5 ,pady=5)

    # VALIDADORES #
    #label_1=Label(frame1, text="VALIDADORES")
    #label_1.grid(row=0, column=1)

    text_1=Text(frame1,wrap="word", height=37, 
                width=40, padx=5, pady=5,bg="#dcdcdc",
                relief="groove", foreground="black")
    text_1.grid(row=1, column=1, padx=5 ,pady=5)

    frame2= Frame(monitor, borderwidth=5, relief="groove")
    frame2.pack(side="right",fill="y")

    text_2=Text(frame2,wrap="word", height=38, 
                width=55, padx=5, pady=5,bg="#dcdcdc", 
                relief="groove", foreground="black")
    text_2.grid(row=1, padx=5 ,pady=5)

    #Barra de Menu 
    barra_menu = Menu(monitor)
    monitor.config(menu=barra_menu)
    menu = Menu(barra_menu, tearoff=False)
    menu.add_command(label='Url',command=lambda: ventana("tabla_ping"))
    menu.add_command(label='Iniciar',command=lambda: inicio(text_0, label, text_1, text_2))
    
    menu.add_separator()
    menu.add_command(label='Salir', command=monitor.destroy)
    barra_menu.add_cascade(label="Menú", menu=menu)
    
    
    def inicio(text_0, label, text_1, text_2):
        ping(text_0, label,text_1, text_2)
        tiempo_ping=threading.Timer(30, lambda:inicio(text_0, label, text_1, text_2))
        tiempo_ping.start()
    
def ventana(tabla):
    print(tabla)
    ventana_2 = Tk()
    ventana_2.geometry("500x400")
    ventana_2.title('MONITOR')
    ventana_label=Label(ventana_2 ,text="Agregar")
    ventana_label.grid(row=0)
    nombre=StringVar(ventana_2)
    nombre_entry=Entry(ventana_2, textvariable= nombre, width=25)
    nombre_entry.grid(row=1)
    descripcion=StringVar(ventana_2)
    descripcion_entry=Entry(ventana_2, textvariable= descripcion, width=25)
    descripcion_entry.grid(row=2)
    puerto=StringVar(ventana_2)
    puerto_entry=Entry(ventana_2, textvariable= puerto, width=25)
    puerto_entry.grid(row=3)
    
    tree = ttk.Treeview(ventana_2)
    tree["columns"] = ("col1","col2","col3")
    tree.column("#0", width=50, minwidth=50)
    tree.column("col1", width=80, minwidth=100)
    tree.column("col2", width=200, minwidth=100)
    tree.column("col3", width=200, minwidth=100)
    tree.heading("col1", text="NOMBRE")
    tree.heading("col2", text="DESCRIPCION")
    tree.heading("col3", text="PUERTO")
    tree.grid(row=4, columnspan=15)
    boton_g = Button(ventana_2, text="Guardar",
                    command=lambda: guardar(tabla, nombre, descripcion, puerto, tree ))
    boton_g.grid(row=5)
    boton_e = Button(ventana_2, text="Eliminar",
                    command=lambda: borrar(tabla, tree))
    boton_e.grid(row=6, column=0)         
    ver(tabla,tree)
    

 
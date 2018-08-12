#!usr/bin/python3
# -*- coding: utf-8 -*-

print( "App de consola" )

def recorrer_numeros( num1, num2 ):

	if num1 > num2:
		mayor = num1
		menor = num2

	else:
		mayor = num2
		menor = num1

	while menor <= mayor:
		print( menor )
		menor = menor + 1

		if( menor % 2 == 0 ):
			print( "El numero {} es un número par".format(menor) )


num1 = int( input("Escriba un número: ") )
num2 = int( input("Escriba un número: ") )

recorrer_numeros(num1, num2)


print( "\nPyGTK" )

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

window = Gtk.Window( title = "He vuelto, mortales!" )
window.connect( 'delete-event', Gtk.main_quit )
window.show_all()

def crear_ventana():

	ventana = Gtk.Window()
	ventana.set_default_size( 200, 300 )
	ventana.connect( 'destroy', Gtk.main_quit )

	etiqueta = Gtk.Label('El mosquito verde te acosa el jardín, humano avispado!')
	ventana.add( etiqueta )

	etiqueta.show()
	ventana.show()

crear_ventana()

Gtk.main()


print( "\nTkinter" )

print( "Instalar con apt-get python3-tk")

print( "\tWidget Label")

from tkinter import *

ap1 = Tk()
texto = Label( 
	ap1, 
	text = 'TK - WidgetLabel: La barbarie ha vuelto!' 
	)

texto.grid(column = 1 )
texto.bind('<Enter>', lambda e: texto.configure( text = 'El raton ha entrado' ) )
# texto.pack()

texto2 = Label( 
	ap1, 
	text = 'TK - WidgetLabel: La barbarie ha vuelto!' 
	)

texto2.grid(column = 1 )
texto2.bind('<Enter>', lambda e: texto2.configure( text = 'El raton ha entrado en el texto dos' ) )
# texto2.pack()


ap1.mainloop()


class AppTkinter(Frame):

    def saludar(self):
        print( "¡Me obligan a saludar, supuesto simio superior!" )

    def crear_widgets(self):

        self.texto = Label(self)
        self.texto['text'] = "Texto de prueba."
        # self.texto['text'] = "Texto de prueba."
        self.texto.pack()


        self.saludo = Button(self)
        self.saludo["text"] = "Holo",
        self.saludo["command"] = self.saludar
        self.saludo["bg"] = "blue"
        self.saludo['width'] = '3'
        self.saludo['height'] = '3'
        self.saludo['anchor'] = "w"
        self.saludo['cursor'] = "hand1"
        self.saludo['bd'] = 5
        self.saludo['relief'] = 'groove'

        self.saludo.pack()
        # self.saludo.pack({"side": "left"})

        self.QUIT = Button(self)
        self.QUIT["text"] = "Salir"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT['bd'] = 4
        # self.QUIT['padding'] = (5, 10)
        self.QUIT['relief'] = 'sunken'

        self.QUIT.pack(
        	{
        		"fill": "x",
        		"padx": "10px",
        		"pady": "10px",
        		"side": "bottom"
        	}
        )



    def __init__(self, master = None):

        Frame.__init__(self, master)

        # Opciones de root: https://www.tcl.tk/man/tcl8.6/TkCmd/wm.htm
        
        self.pack()
        self.crear_widgets()

        print( self.pack_slaves() )



print( "\tWidget de Frame por clase")

root = Tk()
root.geometry( "200x300" )
app_tkinter = AppTkinter( master = root )
app_tkinter.master.title = 'Titulo de App'
app_tkinter.mainloop()
root.destroy()

print( "\nWxPython" )

error_inst = ""
print( "Linux - Error de instalacion: ", error_inst )

# import wx

# app = wx.App( False )
# frame = wx.Frame( None, wx.ID_ANY, 'Malditos mortales!!' )
# frame.Show(True)
# app.MainLoop()


print( "\nPyQt" )

print( "Instalar con apt-cache search PyQt y apt-get install con el deseado" )

print( "\tPyQt4 - Comentado" )

# import sys

# from PyQt4 import QtGui

# class Ventana_pyqt4(QtGui.QMainWindow):

# 	def __init__(self):

# 		super(Ventana, self).__init__()

# 		self.setWindowTitle('Mardito roedores con PyQt4')


# app = QtGui.QApplication( sys.argv )
# ventana_pyqt4 = Ventana_pyqt4()
# ventana_pyqt4.show()

# sys.exit( app.exec_() )


print( "\tPyQt5 - Comentado")

print( "Error de consola - (10_app.py:9102): Gtk-ERROR **: GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported" )

# import sys

# from PyQt5 import QtWidgets

# class Ventana_pyqt5(QtWidgets.QMainWindow):

# 	def __init__(self):

# 		super(Ventana, self).__init__()

# 		self.setWindowTitle('Mardito roedores')


# app = QtWidgets.QApplication( sys.argv )
# ventanita = Ventana()
# ventanita.show()

# sys.exit( app.exec_() )


print( "\nPyside")

print( "Instalar con pip pyside" )

print( "problema con pyside - comentado")
# import sys
# from PySide.QtCore import *
# from PySide.QtGui import *

# app = QApplication( sys.argv )
# ventana = QWidget()
# ventana.resize( 320, 240 )
# ventana.SetWindowtitle( 'Hola Mundo' )

# etiqueta = QLabel( ventana )
# etiqueta.settext( 'Hola mundillo!' )
# etiqeuta.setGeometry( QRect(130, 110, 60, 10) )
# ventana.show()

# sys.exit(app.exec())


# def crear_ventana():

# 	ventana = Gtk.Window()
# 	ventana.set_default_size( 200, 300 )
# 	ventana.connect( 'destroy', Gtk.main_quit )

# 	etiqueta = Gtk.Label('El mosquito verde te acosa el jardín, humano avispado!')
# 	ventana.add( etiqueta )

# 	etiqueta.show()
# 	ventana.show()

# crear_ventana()
# Gtk.main()
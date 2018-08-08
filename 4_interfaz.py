#!usr/bin/python3
# -*- coding: UTF-8 -*-

print( "4 - Interfaz Gráfica de Python" )

print( "\nWxPython" )

print( "Descargar wxPython de wxpython.org o instalar desde consola con 'pip3 install -U wxPython'")

print( "Problema en Linux para instalar wxPython")

print( "\nScript en consola")

Comprueba la instalacion correcta
import wx

Añade la ruta si no está bien instalado
import sys
sys.path.append('C:\\ruta\Python\lib\wxPython')

print("\n2 - Creacion de una ventana simple")
import wx

app = wx.App()
frame = wx.Frame( None, -1, 'Ventana 1', size=(900, 400) )	# Creamos el objeto con medidas (ancho, alto)
frame.Show()	# Creamos el contenedor padre para crear la ventana
app.MainLoop()	# Mostrar la ventana


print("\n3 - Creacion de una ventana simple por una clase - modulizacion")
import wx

class Ventana_Demo():

	def __init__( self, parent, title ):

		super(Ventana_Demo, self).__init__( parent, title="Ventana 2", size=(400, 400) )
		self.Show(True)


app = wx.App()
Ventana_Demo( None, 'Demo' )
app.MainLoop()	# Mostrar la ventana


print("\n4 - Posición de la ventana")
import wx

class Ventana_Demo():

	def __init__( self, parent, title ):

		super(Ventana_Demo, self).__init__( parent, title="Ventana 2", size=(400, 400) )

		self.Centre() # posiciona la ventana en el centro de la pantalla

		self.Show(True)


app = wx.App()
Ventana_Demo( None, 'Demo' )
app.MainLoop()	# Mostrar la ventana


print("\n4 - Posición del menu de la ventana")
import wx

class Menu_Demo( wx.Frame ):

	def __init__( self, parent, title ):

		super(Menu_Demo, self).__init__( parent, title = title, size = (400, 400) )

		self.SetPosition( (40, 40) ) # posiciona la ventana desde el (0x, 0y) de la pantalla

		self.InitUI()

	def initUI(self):

		menubar = wx.MenuBar()
		fileMenu = wx.Menu()

		fileitem = fileMenu.Append( wx.ID_EXIT, 'Salir' ) # Opcion del menu
		menubar.Append( fileMenu, '&Archivo' ) # Etiqueta en barra superior
		self.SetMenuBar( menuBar )
		self.Bind( wx.EVT_MENU, self.OnQuit, fileItem )
		self.Show( True )

	def OnQuit( self, e ):

		self.Close()


app = wx.App()


print("\n5 - Ventana de login")
import wx

class MiFrame( wx.Frame ):

	def __init__( self ):

		wx.Frame.__init__( self, None, title = "Login" )
		panel = wx.Panel( self )
		self.count = 0

		self.mainSizer = wx.BoxSizer( wx.VERTICAL )

		usernameLb1 = wx.StaticText( panel, label = "Usuario:" )
		self.username = wx.TextCtrl( panel )
		self.anadirWidgets( usernameLb1, self.username )

		pwLb1 = wx.StaticText( panel, label = "Contraseña:" )
		self.pw = wx.textCtrt( panel )
		self.anadirWidgets( pwLb1, self.pw )

		boton = wx.Button( panel, label = "Acceder" )
		boton.Bind( wx.EVT_BUTTON, self.onClick )
		self.mainSizer.Add( boton, 0, wx.ALL | wx.CENTER, 5 )

		panel.SetSizer( self.mainSizer )
		self.show()
		

	def anadirWidgets(self, label, texto):

		sizer = wx.BoxSizer( wx.HORIZONTAL )
		sizer.Add( label, 0, wx.ALL | wx.CENTER, 5 )
		sizer.Add( texto, 1, wx.ALL | wx.EXPAND, 5 )

		self.mainSizer.Add( sizer, 0, wx.ALL | wx.EXPAND )


	def onClick( self, event ):

		password = self.pw.GetValue()
		user = self.username.GetValue()

		if user != "alumno" and password != "alumno":

			mensaje = "Te quedan %s intentos" % str(3 - self.count)
			dialogo = wx.MessageDialog( self, mensaje, "", wx.OK )
			dialogo.ShowModal()
			dialogo.Destroy()

			self.count += 1
			password = self.pw.GetValue()
			password = self.username.GetValue()

			if self.count == 3:

				self.Destroy()

		
		if user == "alumno" and password == "alumno":

			ventana = VentanaNueva( None )
			ventana.Show()


class VentanaNueva( wx.Frame ):

	def __init__( self, parent ):

		wx.Frame.__init__( self, parent )
		panel = wx.Panel( self, -1 )
		texto = wx.StaticText( panel, label = "Estás dentro!" )

if __name__ == "__main__":
	
	app = wx.App( False )
	frame = MiFrame()
	app.MainLoop()	# Mostrar la ventana



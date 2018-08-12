print( "\nPyGTK" )

import gtk

def crear_ventana():

	ventana = gtk.Window()
	ventana.set_default_size( 200, 300 )
	ventana.connect( 'destroy', gtk.main_quit )

	etiqueta = gtk.Label('El mosquito verde te acosa el jardín, humano avispado!')
	ventana.add( etiqueta )

	etiqueta.show()
	ventana.show()

crear_ventana()
gtk.main()
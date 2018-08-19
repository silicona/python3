#!usr/bin/python3
#-*- coding:utf-8 -*-

import argparse
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM



# Colores Tkinter: http://wiki.tcl.tk/37701

TABLEROS = ['debug', 'n00b', 'l33t', 'error']
MARGEN = 20	# Margen del tablero
LADO = 50	# Lado de cada celda
ANCHO = ALTO = MARGEN * 2 + LADO * 9	# Dimensiones del tablero


class SudokuError(Exception):

	''' Error especifico de la aplicación '''
	pass


def leer_argumentos():

	''' lee el argumento de sudoku.py <nombre_tablero> '''
	lector_arg = argparse.ArgumentParser()
	lector_arg.add_argument( "--tablero",
							 help = "Tablero deseado",
							 type = str,
							 choices = TABLEROS,
							 required = True )

	# Crear un dict { flag: arg }
	args = lector_arg.parse_args()
	return args.tablero


class IUSudoku(Frame):

	''' UI Tkinter, responsable de dibujar el tablero y recoger la entrada del usuario '''
	def __init__(self, padre, juego):

		self.juego = juego
		self.padre = padre

		Frame.__init__(self, padre)

		self.fila, self.columna = 0, 0

		self.__iniciar_IU()


	def __iniciar_IU(self):

		self.padre.title( "Sudoku, un juego de simios" )
		self.pack( fill = BOTH, expand = 1 )
		
		self.canvas = Canvas( self, width = ANCHO, height = ALTO )
		self.canvas.pack( fill = BOTH, side = TOP )

		btn_limpiar = Button( self, 
							  text = 'Limpiar tablero', 
							  command = self.__limpiar_tablero )

		btn_limpiar.pack( fill = BOTH, side = BOTTOM )

		self.__dibujar_tablero()
		self.__dibujar_puzzle()

		# Button-1 = Boton Izq del raton
		self.canvas.bind( "<Button-1>", self.__click_celda )
		self.canvas.bind( "<Key>", self.__pulsar_tecla )


	# Metodos Helper
	def __dibujar_tablero(self):

		''' Dibuja el tablero con lineas azules y cuadros de 3x3 '''

		for i in range(10):
		# for i in xrange(10):

			color = "blue" if i % 3 == 0 else "gray"

			x0 = MARGEN + i * LADO
			y0 = MARGEN
			x1 = MARGEN + i * LADO
			y1 = ALTO - MARGEN
			self.canvas.create_line( x0, y0, x1, y1, fill = color )

			x0 = MARGEN
			y0 = MARGEN + i * LADO
			x1 = ANCHO - MARGEN
			y1 = MARGEN + i * LADO
			self.canvas.create_line( x0, y0, x1, y1, fill = color )


	def __dibujar_puzzle(self):

		self.canvas.delete( "numeros" )

		for i in range(9):
		# for i in xrange(9):

			for j in range(9):
			# for j in xrange(9):

				respuesta = self.juego.puzzle[i][j]

				if respuesta != 0:

					x = MARGEN + j * LADO + LADO / 2
					y = MARGEN + i * LADO + LADO / 2
					original = self.juego.inicio_puzzle[i][j]
					color = "black" if respuesta == original else "sea green"

					self.canvas.create_text( x, y, text = respuesta, tags = "numeros", fill = color )


	def __limpiar_tablero(self):

		self.juego.iniciar()
		self.canvas.delete( "Victoria" )
		self.__dibujar_puzzle()

	def __click_celda(self, evento):
		if self.juego.fin_juego:

			return

		x, y = evento.x, evento.y

		if( MARGEN < x < ANCHO - MARGEN and MARGEN < y < ALTO - MARGEN ):

			self.canvas.focus_set()

			# Obtener los números de fila y col desde x e y
			fila, col = int((y - MARGEN) / LADO), int((x - MARGEN) / LADO)

			# import pdb; pdb.set_trace()
			# Si la celda esta seleccionda, des-seleccionarla
			if( fila, col ) == ( self.fila, self.columna):

				self.fila, self.columna = -1, -1

			elif self.juego.puzzle[fila][col] == 0:

				self.fila, self.columna = fila, col


			self.__dibujar_cursor()

	def __dibujar_cursor(self):

		''' Ilumina la celda pulsada '''
		self.canvas.delete( "cursor" )

		if self.fila >= 0 and self.columna >= 0:

			x0 = MARGEN + self.columna * LADO + 1
			y0 = MARGEN + self.fila * LADO + 1
			x1 = MARGEN + (self.columna + 1) * LADO - 1
			y1 = MARGEN + (self.fila + 1) * LADO -1

			self.canvas.create_rectangle(
				x0, y0, x1, y1,
				outline = "red", tags = "cursor"
			)

	def __pulsar_tecla(self, evento):

		if self.juego.fin_juego:

			return

		if self.fila >= 0 and self.columna >= 0 and evento.char in "123456789":

			self.juego.puzzle[self.fila][self.columna] = int( evento.char )
			self.columna, self.fila = -1, -1
			self.__dibujar_puzzle()
			self.__dibujar_cursor()

			if self.juego.comprobar_final():

				self.__dibujar_victoria()

	def __dibujar_victoria(self):

		# crea un óvalo
		x0 = y0 = MARGEN + LADO * 2
		x1 = y1 = MARGEN + LADO * 7
		self.canvas.create_oval(
			x0, y0, x1, y1,
			tags = 'victoria', fill = "dark orange", outline = "orange"
		)

		# Crea texto
		x = y = MARGEN + 4 * LADO + LADO / 2
		self.canvas.create_text(
			x, y,
			text = "Has ganado. ¿Seguro que no has copiado la solución?",
			tags = "ganador",
			fill = "white",
			font = ( "Arial", 32 )
		)


class TableroSudoku(object):

	''' Representacion del tablero '''
	def __init__(self, archivo_tablero):

		self.tablero = self.__crear_tablero( archivo_tablero )


	def __crear_tablero(self, archivo):

		''' Crea una matriz, lista de listas '''
		tablero = []

		for linea in archivo:

			linea = linea.strip()

			if len( linea ) != 9:

				raise SudokuError('Cada línea debe tener 9 carácteres')

			tablero.append([])

			for char in linea:

				if not char.isdigit():

					raise SudokuError('El caracter debe ser un entero')

				# Añade el char al último tuple(actual)
				tablero[-1].append( int(char) )

		if len( tablero ) != 9:

			raise SudokuError('El tablero no tiene 9 filas.')

		return tablero


class JuegoSudoku(object):

	''' Juego, a cargo de guardar el estado del tablero y comprobar si se ha resuelto '''
	def __init__(self, archivo_tablero):

		self.archivo_tablero = archivo_tablero
		self.inicio_puzzle = TableroSudoku( archivo_tablero ).tablero


	def iniciar(self):

		self.fin_juego = False
		self.puzzle = []

		for i in range(9):
		# for i in xrange(9):

			self.puzzle.append([])

			# for j in xrange(9):
			for j in range(9):

				self.puzzle[i].append( self.inicio_puzzle[i][j] )


	def comprobar_final(self):

		for fila in range(9):
		# for fila in xrange(9):

			if not self.__comprobar_fila(fila):

				return False

		for columna in range(9):
		# for columna in xrange(9):

			if not self.__comprobar_columna( columna ):

				return False

		for fila in range(3):
		# for fila in xrange(3):

			for columna in range(3):
			# for columna in xrange(3):

				if not self.__comprobar_cuadro( fila, columna ):

					return False

		self.fin_juego = True
		return True


	def __comprobar_bloque(self, bloque):

		return set(bloque) == set( range(1,10) )


	def __comprobar_fila(self, fila):

		return self.__comprobar_bloque( self.puzzle[fila] )

	def __comprobar_columna(self, columna):

		return self.__comprobar_bloque( [self.puzzle[fila][columna] for fila in range(9)] )
		# return self.__comprobar_bloque( [self.puzzle[fila][columna] for fila in xrange(9)] )

	def __comprobar_cuadro(self, fila, columna):

		return self.__comprobar_bloque(
			[
				self.puzzle[r][c]
				for r in range( fila * 3, (fila + 1) * 3 )
				for c in range( columna * 3, (columna + 1) * 3 )
				# for r in xrange( fila * 3, (fila + 1) * 3 )
				# for c in xrange( columna * 3, (columna + 1) * 3 )

			]
		)


if __name__ == "__main__":


	# Ejecución obligatoria por comandos
	nombre_tablero = leer_argumentos()

	with open( "%s.sudoku" % nombre_tablero, "r") as archivo_tablero:

		juego = JuegoSudoku( archivo_tablero )
		juego.iniciar()

		raiz = Tk()
		IUSudoku( raiz, juego )
		raiz.geometry( "%dx%d" % (ANCHO, ALTO + 40) )

		raiz.mainloop()




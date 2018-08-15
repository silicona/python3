#!usr/bin/python3
# -*- coding: utf-8 -*-

import math
import re

def raiz_cuadrada( numero ):

	raiz = math.sqrt(numero)

	return raiz


km = 10	# Local al main

def acelerar():

	global km	# global

	tiempo = 1	# local

	km += 5

	return km



class Blob:

	def __init__( self, ancho, alto, *_ ):	# Con *_, ignora los argumentos que exceden a los parametros

		# print( 'Blob creado con ancho {} y alto {}'.format(ancho, alto) )
		self.ancho = ancho
		self.alto = alto


class Rectangulo(Blob):

	def __init__( self, width, height,
					color = 'black', enfasis = None, luz = 0 ):

		if width == 0 and height == 0 and color == 'red' \
			and (enfasis == 'strong' or luz > 100):

			raise ValueError( "Has perdido, humano" )

			# try:
			# 	raise ValueError("Has perdido, humano")

			# except ValueError as error:
			# 	print( "\tCazado rect_1: " + str(error) )

		if width == 4 and height == 2 and \
			(color == 'rojo' or enfasis is None):

			try:
				raise Exception('No lo creo, humano')

			except Exception as e:
				print( '\tCazado solo rect_2 por parentesis en if: ', e)

		Blob.__init__( self, width, height,
						color, enfasis, luz )

	# 	self.__dar_forma(width, height)


	# def __dar_forma(self, ancho, alto):

	# 	self.ancho = ancho
	# 	self.alto = alto


	def mostrar( self ):

		print( "\tMe muestro:", self )


	def medir( self, ancho, alto ):

		if self.ancho == ancho and self.alto == alto:
			return True

		else:
			return False

import pdb

'''
Debug de Python
pdb.set_trace() marca un punto de ruptura para TDD con su propia consola:

	list - Comando que lista el snippet que da error (5 lineas a cada lado)
	[variable] - Muestra el valor de la variable
	help - Muestra todos los comandos
	n - step forward to next line of execution.
	args - list the variables involved in the current execution point.
	continue - run the code through to completion.
	jump <line number> - run the code until the specified line number.
	quit/exit - stop pdb.
'''

class Calculadora(object):

	def sumar( self, x, y ):

		tipos = ( int, float, complex )
		# tipos = ( int, long, float, complex )

		if isinstance(x, tipos) and isinstance(y, tipos):

			# pdb.set_trace() # Comentado para continuar el script
			return x + y

		else:

			raise ValueError

	def restar(a, b):
		return a - b


	def multiplicar(a, b):
		return a * b
 
	 
	def dividir(numerator, denominator):
		return float(numerator) / denominator


class Romanos():

	def __init__(self):

		self.mapa_numeral = (
			('M',  1000),
			('CM', 900),
			('D',  500),
			('CD', 400),
			('C',  100),
			('XC', 90),
			('L',  50),
			('XL', 40),
			('X',  10),
			('IX', 9),
			('V',  5),
			('IV', 4),
			('I',  1)
		)

		self.patron_numeral = re.compile('''
			^                   # beginning of string
			# M{0,3}            # thousands - 0 to 3 Ms
			M{0,4}              # thousands - 0 to 4 Ms - ACTUALIZACION A 5000
			(CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
								#            or 500-800 (D, followed by 0 to 3 Cs)
			(XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
								#        or 50-80 (L, followed by 0 to 3 Xs)
			(IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
								#        or 5-8 (V, followed by 0 to 3 Is)
			$                   # end of string
			''', re.VERBOSE
		)

		# REFACTORIZACION
		self.tabla_a_romano = [ None ]

		self.tabla_desde_romano = {}

		self.construir_tablas()



	def a_romano(self, num_ent):

		'''Convierte un entero al numeral romano'''

		# if num > 3999: # Actualizado para los tests 2 y 3 de tdd_tests.py
		# if not( 0 < num_ent < 4000):	# ACTUALIZADO A 5000

		if not isinstance(num_ent, int):
		# if int(num_ent) != num_ent:
			raise ErrorNoEntero('Intenta usar un número, lumbrera latina.')
			
		if not( 0 < num_ent < 5000):
			raise ErrorFueraDeRango('El número debe estar entre 0 y 4999, simio imberbe!')

		# REFACTORIZACION
		# if not isinstance(num_ent, int):
		# 	raise ErrorNoEntero('Roma no partía números, ni perdonaba la ignorancia.')

		# resultado = ''
		# for numeral, entero in self.mapa_numeral:

		# 	while num_ent >= entero: 

		# 		resultado += numeral
		# 		num_ent   -= entero
		# 		# Explicacion por consola
		# 		# print('Restando {0} de la entrada, sumando {1} a la salida.'.format(entero, numeral))

		# return resultado

		return self.tabla_a_romano[ num_ent ]


	def desde_romano(self, num_rom):

		'''Convierte un numeral romano en entero'''

		# REFACTORIZACION
		# if not num_rom:
		# 	raise ErrorNumeralRomanoInvalido( "¿Dijiste algo? Habla más claro, soprano!")

		# if not self.patron_numeral.search(num_rom):
		# 	raise ErrorNumeralRomanoInvalido( "¿No sabes escribir en romano? {0} no es válido!".format(num_rom) )
                    
		# resultado = 0
		# index = 0

		# for numeral, entero in self.mapa_numeral:

		# 	while num_rom[index:index + len(numeral)] == numeral:

		# 		resultado += entero
		# 		index += len( numeral )
		# 		# Explicacion por consola
		# 		# print('Encontrado ', numeral, ' de longitud ', len(numeral), ', sumando ', entero)

		# return resultado

		if not isinstance( num_rom, str ):
			raise ErrorNumeralRomanoInvalido( "Alea Jacta String, dijo el poeta." )

		if not num_rom:
			raise ErrorNumeralRomanoInvalido( "¿Dijiste algo? Habla más claro, soprano!")

		if num_rom not in self.tabla_desde_romano:
			raise ErrorNumeralRomanoInvalido( "¿No sabes escribir en romano? {0} no es válido!".format(num_rom) )

		return self.tabla_desde_romano[ num_rom ]
        

	def construir_tablas(self):

		def a_romano(num_ent):

			resultado = ''

			for numeral, entero in self.mapa_numeral:

				if num_ent >= entero:

					resultado = numeral
					num_ent -= entero
					break

			if num_ent > 0:

				resultado += self.tabla_a_romano[ num_ent ]

			return resultado

		for entero in range( 1, 5000):

			numeral_romano = a_romano( entero )
			self.tabla_a_romano.append( numeral_romano )
			self.tabla_desde_romano[numeral_romano] = entero


class ErrorFueraDeRango(ValueError): pass


class ErrorNoEntero(ValueError): pass


class ErrorNumeralRomanoInvalido(ValueError): pass



# Sobre roman1.py - Romanos()
# Copyright (c) 2009, Mark Pilgrim, All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
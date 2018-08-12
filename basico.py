#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Comentario en Bloque

Comentario en Bloque
'''

hola = 'Hola' * 3
print( hola )

running = 'Running down the hill'
print( running )

suma = 2 + 3
print( 2 + 3 )
print( str(suma) )

total = hola +\
		running +\
		str(suma)
print( total )

# s = ( 'Area: {0}, Estimado: ({1}): {2}'
# 		.format(area_of_circle, puntos, estimado(radius, puntos)) )

# Palabras clave
import keyword
print( "\nPalabras Clave", keyword.kwlist )

print("\nPalabras reservadas")
print('and 		del 	for 	is 		raise 		assert')
print('if 		else 	elif 	from 	lambda 		return')
print('break 	global 	not 	try 	class 		except')
print('or 		while 	continue		exec 		import')
print('yield 	def 	finally 		in 			print')

# Indentacion
print( "\nINDENTACION - Clase Rectangulo" )
class Blob:

	def __init__( self, ancho, alto, *_ ):	# Con *_, ignora los argumentos que exceden a los parametros

		print( 'Blob creado con ancho {} y alto {}'.format(ancho, alto) )


class Rectangulo(Blob):

	def __init__( self, width, height,
					color = 'black', enfasis = None, luz = 0 ):

		if width == 0 and height == 0 and color == 'rojo' \
			and (enfasis == 'strong' or luz > 100):

			try:
				raise ValueError("Has perdido, humano")
			except ValueError as error:
				print( "\tCazado rect_1: " + str(error) )

		if width == 4 and height == 2 and \
			(color == 'rojo' or enfasis is None):

			try:
				raise Exception('No lo creo, humano')

			except Exception as e:
				print( '\tCazado solo rect_2 por parentesis en if: ', e)

		Blob.__init__( self, width, height,
						color, enfasis, luz )


	def mostrar( self ):

		print( "\tMe muestro:", self )


rect_ok = Rectangulo( 4, 4 )
rect_ok.mostrar()
rect_1 = Rectangulo( 0, 0, 'rojo')
rect_2 = Rectangulo( 4, 2)


print( "\nSímbolos" )
print( "\t''=	+=	-=	*=	/=	**=	//=''" )

print( "\nTipo de dato")

print( "int - Números enteros: Decimal: 24 - 60 / Binario: 0b010011 - 0b1101 / Hexadecimal: 0x18 - 0x3cf4 / Octal: 030 - 074" )
print( "float - Números de punto flotante: 3.141595 - 12. - -45.3556" )
print( "complex - Números complejos: 6.32 + 45j - 0.117j - (2 + 0j) - 1j" )
print( "bool - Booleanos: True - False" )
print( "str - Cadena: 'Adios, cruel humano'" )
print( "None - Valor none" )

print( "\nFunciones de tipo de dato" )
print( "type() - tipo de dato de una variable" )
print( "str() - Transforma en cadena, si es posible" )
print( "int() - Transforma en entero, si es posible (complex no)" )
print( "float() - Transforma en float, si es posible (complex y string solo alfa no)" )
print( "complex() - Transforma en complex, si es posible (string solo alfa no)" )
print( "bool() - Transforma en booleano: 0 = False" )
print( "eval() - Evalúa un objeto str como si fuera una expresión, no un string sin más" )
print( "upper() / lower() / capitalize() - Caracteres de str en mayusculas / minusculas / prim mayuscula" )

print( "\nTipo de dato secuencial" )
print( "Strings - Cadena" )
print( "list - Array numerico: [5, 7, 9, 'Sergio', 45.3] (Anidacion del mismo tipo)" )
print( "tuple - Array numerico inmutable: (5, 7, 9, 'Sergio', 45.3) (Posibles keys de Diccionarios)" )
print( "range - Array numerico: [5, 7, 9, 'Sergio', 45.3]" )
print( "set - Conjunto no ordenado de elementos unicos: set('abracadabra')" )
print( "diccionario - Array con clave y valor: {'a': 1, 'b': 2, 'c': 3, 'd': 4}" )

print( "\nFunciones de tipo de dato secuencial" )
print( "len() - Devuelve la longitud de un str o list: len('Python es grande') -> ", len('Python es grande') )
arr = ['Python', 'es','grande']
arr.sort()
print( "sort() - Reordena aletoriamente un list: ['Python', 'es', 'grande'].sort() -> ", arr )
print( "split() - Convierte un str en list: 'Python es grande'.split() -> ", 'Python es grande'.split() )
print( "[ini:fin] - Extrae de un str o list: 'Python es grande'[2:12] -> ", "Python es grande"[2:12] )
print( "[::pas] - Extrae de un str o list cada pas: 'Python es grande'[::3] -> ", "Python es grande"[::3] )
print( "[ini: fin: pas] - Extrae de un str o list: 'Python es grande'[2: 12: 2] -> ", "Python es grande"[2: 12: 2] )
print( "+ / += - Concatena str o list" )
print( "* - Repite str o list" )
print( "var in list - Devuelve True si var está en list" )
print( "var not in list - Devuelve True si var no está en list" )
print( "- | & ^ - Comparaciones entre sets" )
print( "dict() - Crea un dict con los argumentos" )
print( "zip() - Crea un dict con dos elementos iterables" )
print( "keys() - Crea un list con las claves de un dict" )



print( "\nOperadores" )

print(" +	-> Suma")
print(" -	-> Resta")
print(" *	-> Multiplicacion")
print(" /	-> División natural")
print(" //	-> División floor - redondeo hacia abajo")
print(" %	-> Modulo - Resto de división")
print(" **	-> Exponencial - eleva a la potencia de x")
print(" == 	-> Identidad simple")
print(" is 	-> ==")
print(" != 	-> Diferencia simple")
print(" <> 	-> !=")
print(" is not -> !=")
print(" >/<	-> Mayor / menor")
print(" >=/<= -> Igualdad o mayor / menor")


print( "\nGuión bajo (_) en Python3 comentado" )
'''
# GUIÓN BAJO (_) HACE REFERENCIA A LA ÚLTIMA VARIABLE

>>> 10	-> 10
>>> _*2	-> 20
>>> _*3	-> 60

# GUIÓN BAJO (_) IGNORA VALORES ESCIFICOS

x, _, y = ( 1, 2, 3 )	-> x = 1, y = 3

x, *_, y = ( 1, 2, 3, 4, 5 )	-> x = 1, y = 5

for _ in range(10):	-> Ignora el index

	do_something()

# GUIÓN BAJO (_) DECLARA OBJETOS PRIVADOS

'''
# DOBLE GUIÓN BAJO (_) ANTEPONE EL NOMBRE DE CLASE EN LA FUUNCION - NO CONFLICTOS

class _Base:	# Clase privada

	_factor_oculto = 2	# Variable privada

	def __init__(self, precio):

		self.precio = precio


import random
print( "\nAzar en juego:")

a = random.randrange( 10 )
print('En una escala del 0 al 10, tu atracción por la Tierra es:')
print( "\tY tu has dicho: ", a)

if a > 9 : 
	texto = "\tParece que sabes donde pisas, simio imberbe."

else:
	texto = "\tNo aciertas ni una. ¿Realmente sabes porque cayó la manzana de Newton?"

print( texto )

# BUCLES
print( "\nBUCLES" )
entrada = str
while( (entrada != 's') and ( entrada != 'n') ) :

	# entrada = raw_input( '¿Eres mayor de edad? (s/n)' ) # Python 2
	entrada = input( '¿Eres mayor de edad? (s/n)' )	# Python 3

if entrada == 's' :

	print( '\t** Estimad@ cliente **\n\tVisite nuestro bar!!\n')

else :

	print( '\t** Enclenque humano **\n\tVuelve cuando seas mayor de edad!!\n' )

secuencia = ['uno', 'dos', 'tres']
print( "Tipo de secuencia: " + str( type(secuencia) ) )

for elemento in secuencia:
	print( "\tElemento: " + elemento )

print( "\nFor con Rango" )
for i in range(6) :

	print( "\ti: " + str(i) )

print( "\nMetodos de Medias" )

def escribe_med():

	media = ( a + b ) / 2

	print( "\tLa media de {:d} y {:d} es: {:f}" . format(a, b, media) )

	return


def escribe_media(a, b) :

	# global a
	# global b

	media = ( a + b ) / 2

	print( "\tLa media de {:d} y {:d} es: {:f}" . format(a, b, media) )

	print("\ta={:d}, b={:d}" . format( a, b ) )
	return media

a, b = 3, 5

escribe_med()

media = escribe_media(a, b)
print( media )

def cambia(b):

	b += [5]

a, b = [3], [4]

cambia(a)
print( a )

# EXCEPCIONES
print( "\nExcepciones" )

dividendo = 5
divisor = 0
try:
	cociente = dividendo / divisor
except:
	print( "\nExcepción capturada, enclenque humano." )

def divide( x, y ):

	try:
	
		resultado = x / y
	
	except ZeroDivisionError as e:
		print( "\tHas intentado dividir por cero, humano. Mal hecho...", str(e) )
	
	else:
		print( "\tEl resultado es ", resultado )

	finally:

		print( '\t\tEjecutando clausula Finally' )

divide( 2, 0 )

# EXCEPCION A MEDIDA - Clase a partir de Exception y ser llamada con raise
class PassLargo( Exception ):
	''' Excepción definida por usuario '''
	def __init__( self, longitud ):	# Metodo constructor

		Exception.__init__( self )	# Contruye la excepción...
		self.longitud = longitud	# ... con el atrivuto de longitud

try:
	clave = input( "\nTeclea un password:" )

	if len( clave ) < 6 :

		raise PassLargo( len(clave) )

except PassLargo as lp:

	print('\t** Terco humano **\n\tPassLargo: Error por longitud: {0}' . format(lp.longitud) )

else:

	print( "\tSin error en la contraseña, terco humano.")

print("\nFACTORIAL")
def factorial(n):

	'''
	Calcula el factorial de n
	Pre: n debe ser entero mayor que 0
	Post: Devuelve el factorial pedido
	'''

	try:
		assert n >= 0, "Assert en acción:\n\tn debe ser igual o mayor que 0"

	except AssertionError as e:

		print('\tAssert cazado (no interrumpe ejecución):', e)

	factorial = 1

	# for i in xrange( 2, n + 1 ): # Python 2
	for i in range( 1, n + 1 ):
		factorial *= i

	return factorial

print( 'Factorial 1: ', factorial(-1) )
print( 'Factorial 2: ', factorial(5) )


print("\nVISIBILIDAD")

def acelerar():

	global km	# global

	tiempo = 1	# local

	km += 5

km = 10	# Local al main

print( "\tVelocidad:", km)	# 10

acelerar()
print( "\tVelocidad:", km)	# 15

try:

	print( '\n\tTiempo:', tiempo)	# no definida

except Exception as error:

	print('\tVariable tiempo no está definido:', str(error) )

print("\nMATH")

import math

def raiz_cuadrada( numero ):

	raiz = math.sqrt(numero)

	return raiz

a = 9
print( "\tLa raiz de {} es: {}".format(a, raiz_cuadrada(a)) )

b = 14
print( "\tLa raiz de {} es: {}".format(b, raiz_cuadrada(b)) )

c = 23456
print( "\tLogaritmo de {} en base 'e': {}".format(c, math.log(c)) )

print( "\nEstadisticas" )
import statistics as stats

edades = [22, 33, 44, 26, 32, 12]
print( "\tEstadísitica de edades: ", stats.mean(edades) )

print( "\nCalendario" )
from datetime import datetime, date, time, timedelta
import calendar

ahora = datetime.now()

print( "\tDia: ", ahora.day )
print( "\tMes: ", ahora.month )
print( "\tAño: ", ahora.year )
print( "\tHora: ", ahora.hour )
print( "\tMinutos: ", ahora.minute )
print( "\tSegundos: ", ahora.second )
print( "\tMicrosegundos: ", ahora.microsecond )

hora = time(10, 5, 0)
print( "\tCreando un dato time: ", hora)

hora2 = time(23, 25, 40)
print( "\tCreando otro dato time: ", hora2)

print( "\tUno > Otro: ", hora > hora2 )

fec1 = date.today()
fec2 = date.today() + timedelta(days = 2)
print( "\tfec1 > fec2: ", fec1 > fec2 )

import time as tiempo

print( "\tDiferencia UTC y horario verano: ", tiempo.altzone)
print( "\tDiferencia UTC y horario local: ", tiempo.timezone)
print( "\tajuste de verano: ", tiempo.tzname)
print( "\tHorario actual con ajuste verano: ", tiempo.daylight)

print( "\tCalendario", calendar.month(2018, 8) )


print( "\nDemora de procesamiento")
import timeit
# demora = timeit.timeit("[x for x in xrange(1000000) if x%4]", number = 100) # Python 2 # Más rápido que 3
demora = timeit.timeit("[x for x in range(1000000) if x%4]", number = 100) # Python 3
print( 'Tiempo de Demora:', demora )


print( 'Fin' )
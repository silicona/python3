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

import keyword
print( keyword.kwlist )

import random
a = random.randrange( 10 )

if a > 5 : 
	
	print( 'La variables es mayor que 5' )

else:

	print( 'Más suerte la próxima vez.')

entrada = str
while( (entrada != 's') and ( entrada != 'n') ) :

	entrada = raw_input( '¿Eres mayor de edad? (s/n)' ) # Python 2
	# entrada = input( '¿Eres mayor de edad? (s/n)' )	# Python 3

if entrada == 's' :

	print( 'El usuario es mayor de edad')

else :

	print( 'Vuelve cunado seas mayor de edad' )

secuencia = ['uno', 'dos', 'tres']
print( "Tipo de secuencia: " + str( type(secuencia) ) )

for elemento in secuencia:

	print( elemento )

for i in range(6) :

	print( i )


def escribe_med():

	media = ( a + b ) / 2

	print( "La media de {:d} y {:d} es: {:f}" . format(a, b, media) )

	return


def escribe_media(a, b) :

	# global a
	# global b

	media = ( a + b ) / 2

	print( "La media de {:d} y {:d} es: {:f}" . format(a, b, media) )

	print("a={:d}, b={:d}" . format( a, b ) )
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

def factorial(n):

	'''
	Calcula el factorial de n
	Pre: n debe ser entero mayor que 0
	Post: Devuelve el factorial pedido
	'''

	assert n >= 0, "n debe ser igual o mayor que 0"
	fact = 1

	# for i in xrange( 2, n + 1 ): # Python 2
	for i in range( 2, n + 1 ):
		fact *= i

	return fact

print( factorial(2) )


import timeit
demora = timeit.timeit("[x for x in xrange(1000000) if x%4]", number = 100) # Python 2 # Más rápido que 3
# demora = timeit.timeit("[x for x in range(1000000) if x%4]", number = 100) # Python 3
print( demora )


print( 'Fin' )
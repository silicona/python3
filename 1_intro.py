print( "\nCapitulo 1 - Introducción\n" )

cadena = " Python Avanzado "

print( "La posicion de h en la cadena es: " + str( cadena.find("h") ) )

otra = cadena.strip()

print( "\nUsando strip...\n" )
print( cadena )
print( otra )

otra = cadena.split()

print( "\nUsando split...\n" )
print( cadena )
print( otra )

may = cadena.upper()
mi = cadena.lower()

print( "\nUsando upper y lower...\n" )
print( may )
print( mi )

lista = [6, 3, 1, 9 ,6, 4, 2, 8]

print( "\nUsando sorted con una lista..\n" )
print( sorted(lista) )

print( "\nUsando sorted con una lista de forma invertida..\n" )
print( sorted(lista, reverse = True) )

print( "\nUsando el método sort de las listas...\n" )

lista_sort = lista
lista_sort.sort()
print( lista_sort )

print( "\nConjuntos con set\n")

conjunto = set( '6390' )
conjunto2 = { '5', '0', '7' }

print( conjunto )
print( "\n" )
print( conjunto2 )

print( "\nUsando & con conjuntos (devuelve los elementos comunes)\n")

print( conjunto & conjunto2 )

print( "\nUsando método intersection de conjuntos (lo mismo que &)\n")

print( conjunto.intersection(conjunto2) )



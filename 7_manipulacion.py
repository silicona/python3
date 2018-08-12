#!usr/bin/python3
# -*- coding:utf-8 -*-

print( "Manipulación de datos" )

print( "XML" )

import xml.sax

class ABCContentHandler( xml.sax.ContentHandler ):

	def __init__(self):
		xml.sax.ContentHandler.__init__(self)

	def iniciaElemento( self, nombre, attrs ):
		print( "Empieza el elemento '" + nombre + "'" )

		if nombre == "address":
			print( "\tTipo del atributo: '" + attrs.getValue("type") + "'" )

	def acabaElemento( self, nombre ):
		print( "\tFinal del elemento '" + nombre + "'" )

	def caracteres( self, contenido ):
		print( "Caracteres: " + contenido )

def main(nombre_archivo_fuente):
	fuente = open( nombre_archivo_fuente )
	xml.sax.parse( fuente, ABCContentHandler() )

if __name__ == '__main__':

	# main("svg.xml")
	pass


print( "\nXPATH")

print( "Instalar con pip lxml")

import lxml.etree as ET

s = '''
	<document>
		<internal-code code="201">
			<internal-desc>Galletas Parseadas</internal-desc>
			<top-grouping>Terminado</top-grouping>
			<web-category>Galletitas</web-category>
			<web-sub-category>Parseadas</web-sub-category>
		</internal-code>
		<internal-code code="202">
			<internal-desc>Galletas Cocinadas</internal-desc>
			<top-grouping>Terminado</top-grouping>
			<web-category>Galletitas</web-category>
			<web-sub-category>Cocinadas</web-sub-category>
		</internal-code>
		<internal-code code="203">
			<internal-desc>Galletas Pochas</internal-desc>
			<top-grouping>Terminado</top-grouping>
			<web-category>Galletitas</web-category>
			<web-sub-category>Pochamiento total</web-sub-category>
		</internal-code>
	</document>
	'''

root = ET.fromstring(s)
for texto in root.xpath('.//internal-code[@code="203"]/web-category/text()'):

	print( "Desde el xml, Categoria: ", texto )


print( "\nXSLT" )

xslt_root = ET.XML('''
	<xsl:stylesheet version="1.0"
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
		<xsl:template match="/">
			<foo><xsl:value-of select="/a/b/text()"/></foo>
		</xsl:template>
	</xsl:stylesheet>''')

transformar = ET.XSLT( xslt_root )

root = ET.XML( '<a><b>Texto de prueba</b></a>' )
resultado = transformar(root)

print( "Resultado de XSLT: ", resultado.getroot().text )

print( "\nHTML" )

archivo = open("prueba.html", "w")

mensaje = '''
	<html>
		<head></head>
		<body>
			<p>La luz roja se ha iluminado en nuestro mundo. Ahora se apagará en el vuestro.</p>
		</body>
	</html>'''

resultado = archivo.write( mensaje )
if resultado:
	print( "\tHTML creado en prueba.html" )

archivo.close()


print( "\nEncriptacion" )

print( "Instalar con pip pycrypto" )

from Crypto.Hash import SHA256, MD5

hash = SHA256.new()
hash.update( 'mortales'.encode('utf-8') )

print( "\tResultado de SHA256: ", hash.digest() )

md = MD5.new()
frase = 'mortales'.encode('utf-8')
md.update( frase )

print( "\tResultado de MD5: ", md.digest() )


print( "\nNÚMEROS ALEATORIOS")

import random

print( "\tAleatorio (random.randrange(10)): ", random.randrange(10) )

print( "\tAleatorio con ultimo número (random.randint(1, 10)): ", random.randint(1, 10) )


print( "\nREGEXP" )

import re
patron = re.compile('([ab])([3-5]+)')

busqueda = 'a455 a333b435'
coincidencia = patron.search( busqueda )
print( "Sobre: ", busqueda )
print( "\tGrupos: ", coincidencia.groups() )
print( "\tGrupo 0: ", coincidencia.group(0) )
print( "\tGrupo 1: ", coincidencia.group(1) )
print( "\tGrupo 2: ", coincidencia.group(2) )


print( "\nIMÁGENES" )

print( "instalar con pip Pillow")

from PIL import Image

imagen = Image.open( 'vaca.jpeg' )

imagen.show()


print( "\nARCHIVOS" )

import os
import sys
import argparse

# os.system( "type practica_lectura.txt" )	# Windows
os.system( "cat practica_lectura.txt" )	# Linux / Mac

# os.system( "compact \\c practica_lectura.txt" )	# Windows

print( "\nNum de parametros: ", len(sys.argv) )
print( "\nLista de parametros: ", sys.argv )

parser = argparse.ArgumentParser( description = "Procesando la depuracion" )
parser.add_argument( "-v", "--verbose", help = "Mostrar info de depuración", action = 'store_true' )
args = parser.parse_args()

if args.verbose:
	print( "Depuración activada" )

else:
	print( args )


print( "\nSERVICIOS WEB" )

import urllib.request, json

with urllib.request.urlopen("https://maps.googleapis.com/maps/api/geocode/json?&address=google") as url:

	data = json.loads( url.read().decode() )
	print( data )
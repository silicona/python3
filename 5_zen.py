#!usr/bin/python3
# -*- coding: UTF-8 -*-

print( "5 - Zen en Python" )

print( "\nurllib (analisis de web) y BeautifulSoup (lectura de web)" )

from urllib.request import urlopen
html = urlopen( "http://www.google.com/" )
print( html.read(100) )

print( "\nLectura con BeautifulSoup4" )

# print( "El web scraping está muy relacionado con la indexación de la web, \
# 	la cual indexa la información de la página utilizando un robot y es una técnica universal adoptada por la mayoría de los motores de búsqueda. \
# 	El web scraping se enfoca más en la transformación de datos sin estructura \
# 	en la web en datos estructurados que puede ser almacenado y analizados. \
# 	Algunos usos del web scraping es la comparación de precios en tiendas, \
# 	monitorear datos relacionados con el clima de cierta región, \
# 	la detección de cambios en sitios web y la integración de datos en sitios webs. \
# 	También es utilizado para obtener información relevante de un sitio a través de los rich snippets." )

print( "Paquetes necesarios: beautifulsoup4, request, lxml. Instalar con pip" )

import requests
from bs4 import BeautifulSoup

req = requests.get( 'https://en.wikipedia.org/wiki/Python_(programming_language)' )
soup = BeautifulSoup( req.text, "lxml" )
print(  soup.title )

for sub_titulo in soup.find_all('a'):

	print( sub_titulo.text )
	print( 'Hasta aqui' )
	break


print( "\nPractica de lectura desde web" )

url = input( "Escribe la direccion:" )
url = 'google.es'

req = requests.get( "http://" + url )
data = req.text
soup = BeautifulSoup( data, "lxml" )

print( soup.title )

for sub_titulo in soup.find_all('img'):

	print( sub_titulo.get('src') )

print( "\nPractica de lectura desde archivo" )

archivo = open("practica_lectura.txt")
data = archivo.read()
print( 'Datos: ' + data )

archivo.close()


archivo = open("practica_lectura.txt")

dat = archivo.read(10)
print( 'Datos 10 caracteres: ' + dat )


archivo.close()


print( "\nPractica de escritura en archivo" )

archivo = open( "practica_lectura.txt", "a" )
archivo.write( "\nA continuación")
archivo.close()

archivo = open( "practica_lectura.txt" )
datos = archivo.read()
print( datos )

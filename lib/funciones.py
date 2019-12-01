#! usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import os
import time
import pip
import sys


def dejar_solo_numeros(string):

	if isinstance( string, int ): return string

	res = re.sub( r'[^0-9]+', '', string)

	return res


def devuelve_clave(dict, valor):

	''' Los valores del dict deben ser diferentes '''

	claves = list()
	items = dict.items()

	for item in items:

		if item[1] == valor:

			return item[0]
			# claves.append(item[0])

	return False


def devuelve_lineas_archivo(self, ruta_archivo):

	list_salida = []

	with open( ruta_archivo, 'r' ) as lineas:

		for linea in lineas:
			
			list_salida.append(linea)

	return list_salida


def devuelve_hoy_normal():

	return time.strftime("%d/%m/%Y")


def devuelve_hoy_con_hora_normal():

	return time.strftime("%d/%m/%Y %H:%M")
	

def devuelve_provincia_id(id_o_nombre):

	provincias = {
		'01': 'Álava',	 '02': 'Albacete', '03': 'Alicante', 	'04': 'Almería', 	'05': 'Ávila',
		'06': 'Badajoz', '07': 'Baleares', '08': 'Barcelona', 	'09': 'Burgos', 	'10': 'Cáceres',
		'11': 'Cádiz', 	 '12': 'Castellón de la Plana', '13': 'Ciudad Real', '14': 'Córdoba', '15': 'A Coruña',
		'16': 'Cuenca',  '17': 'Girona', 	'18': 'Granada', 	'19': 'Guadalajara', '20': 'Guipúzcoa',
		'21': 'Huelva',  '22': 'Huesca', 	'23': 'Jaén', 		'24': 'León', 		'25': 'Lerida',
		'26': 'La Rioja','27': 'Lugo', 		'28': 'Madrid', 	'29': 'Málaga', 	'30' :'Murcia',
		'31': 'Navarra', '32': 'Orense', 	'33': 'Asturias', 	'34': 'Palencia', 	'35': 'Las Palmas',
		'36': 'Pontevedra', '37': 'Salamanca', '38': 'Santa Cruz de Tenerife', '39': 'Cantabria', '40': 'Segovia',
		'41': 'Sevilla', '42': 'Soria', 	'43': 'Tarragona', 	'44': 'Teruel', 	'45': 'Toledo',
		'46': 'Valencia','47': 'Valladolid','48': 'Vizcaya', 	'49': 'Zamora', 	'50': 'Zaragoza',
		'51': 'Ceuta', 	 '52': 'Melilla'
	};

	id_o_nombre = str(id_o_nombre)

	if re.search(r'^[^0-9]+$', id_o_nombre):

		return devuelve_clave(provincias, id_o_nombre);


	if len(id_o_nombre) == 1:

		id_o_nombre = '0' + id_o_nombre

		
	return provincias.get(id_o_nombre) or False;


def escribir_log(ruta, log):

	f = open(ruta, 'a')

	# f.write(log.encode('utf-8'))	# Py2
	f.write( str(log) )	# Py3

	f.close()


def limpiar_archivo(self, archivo_log):

	''' Limpia un archivo .txt de logs '''

	if re.search(r"\.txt", archivo_log) != None & os.path.exists(archivo_log):

		archivo = open( archivo_log, 'w' )

		archivo.write('')

		archivo.close()

		return True

	return False


def poner_mayuscula(string):

	string = string.capitalize()

	return string


def quitar_espacios(string):

	res = re.sub("\s", "", string)

	return res


def ver_modulos_instalados():

	'''
	lista_paquetes = sorted( [(p.key, p.version) for p in pip.get_installed_distributions()] )

	print( "{0:<30}{1:<30}".format('Nombre de Paquete', 'Versión') )

	for paquete, version in lista_paquetes:

		print("{0:<30}{1:<30}".format(paquete, version))
	'''

	print(sys.path)
	from pkgutil import iter_modules

	# print( *(m[1] for m in  iter_modules()), sep='\n' )


if __name__ == '__main__':

	dict_test = {
		"prim": "Aa",
		"seg": 	2
	}

	assert dejar_solo_numeros("a1b 2c3") == "123", 'Debería quitar todo lo que no fueran números.'

	assert devuelve_clave(dict_test, "Aa") == "prim", "Debería devolver la clave prim."

	assert devuelve_clave(dict_test, 2) == "seg", "Debería devolver la clave seg con valor de tipo identico."

	assert devuelve_clave(dict_test, "2") == False, "Debería devolver False con valor de tipo distinto."

	assert devuelve_clave(dict_test, "Bb") == False, "Debería devolver False con valor inexistente."

	assert devuelve_provincia_id(1) == 'Álava', 'Debería ser Álava con 1 integer.'

	assert devuelve_provincia_id('1') == 'Álava', 'Debería ser Álava.'

	assert devuelve_provincia_id('01') == 'Álava', 'Debería ser Álava con 01.'

	assert devuelve_provincia_id('Álava') == "01", 'Debería devolver 01.'

	assert devuelve_provincia_id('82') == False, 'Debería devolver False con 82.'

	assert devuelve_provincia_id('Jauja') == False, 'Debería devolver False con Jauja.'

	assert dict_test.get('prim') == "Aa", 'Deberia devolver Aa con prim'

	assert dict_test.get('Error') == None, 'Deberia devolver None con clave inexistente.'

	assert quitar_espacios('123 4567 890') == '1234567890', 'Debería quitar espacios en blanco'

	# print devuelve_hoy_normal()

	# print devuelve_hoy_con_hora_normal()


	directorio = os.getcwd()
	log = "Hola caracola"

	escribir_log(directorio + '/scracher_log.txt', log)




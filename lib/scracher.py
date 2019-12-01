#! usr/local/bin/python
# -*- coding: utf-8 -*-

#import sys

import os
import json
import random
import re
import requests
import sys
import time

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver.common.by import By

sys.path.append('./')

# from funciones import *
# import lib.funciones as Fx
import funciones as Fx

class Scracher():

	def __init__(self):

		self.hash   = "3s5r/#a8hi%ea·doar!!iGFa.a=ajo"
		self.fuente = ''
		self.url    = "http://localhost/oclemconcursos/auto/4887_api_scracher.php"
		# self.url    = "http://localhost/concursos/auto/4887_api_scracher.php"
		# self.url = "https://oclemconcursos.com/concursos/auto/4887_api_scracher.php"
		
		self.driver  = False
		self.actions = False

		self.concursos     = []
		self.url_concursos = []
		# self.id_asociado  = 0
		self.id_municipio = 0
		self.provincia    = ''



	def abrir_conexion(self, navegador = ''):

		driver = False

		if navegador == 'firefox':
		
			driver = webdriver.Firefox()

		elif navegador == 'chrome':

			driver = webdriver.Chrome()

		elif navegador == 'opera':

			driver = webdriver.Opera()

		else:

			driver = webdriver.Firefox()

		self.driver  = driver
		self.actions = ActionChains(self.driver)

		self.concursos     = []
		self.url_concursos = []
		# self.id_asociado  = 0
		self.id_municipio = 0
		self.provincia    = ''

		return driver


	def buscar_elemento( self, texto, tipo = 'link_text', contenedor = False):

		elemento = False
		driver = self.driver

		if contenedor != False: driver = contenedor

		try:

			if tipo == 'clase':

				elemento = driver.find_element_by_class_name(texto)

			elif tipo == 'id':

				elemento = driver.find_element_by_id(texto)

			elif tipo == 'link_text':

				elemento = driver.find_element_by_link_text(texto)

			elif tipo == 'name':

				elemento = driver.find_element_by_name(texto)

			elif tipo == 'partial_link_text':

				elemento = driver.find_element_by_partial_link_text(texto)

			elif tipo == 'xpath':

				elemento = driver.find_element_by_xpath(texto)

			elif tipo == "css":

				elemento = driver.find_element_by_css_selector(texto)

			elif tipo == "etiqueta":

				elemento = driver.find_element_by_tag_name(texto)


		except NoSuchElementException:

			if self.origen == 'Idealista':

				if texto == "picture[@class='logo-branding']/a": texto = "Branding"

				if texto == "item-parking": return False

				if texto == "item-not-clickable-phone": texto = "Teléfono"

			print("Scracher: " + texto + " no encontrado")

		except Exception as error:

			print("Error: ", error)

			return False

		finally:

			return elemento


	def cerrar(self):

		self.driver.quit()

		self.driver = False
		self.actions = False


	def conectar(self, url = ''):

		if url == '': return False

		self.driver.get(url)


	def devuelve_anuncio_base(self):

		return {
			"origen": "",
			"provincia" : "",
			"ciudad"	: "",
			"direccion" : "",
			"titulo"	: "",
			"enlace"	: "",
			"propietario" : "Posible propietario",
			"telefono"	: "",
			"importe"	: "",
			"observaciones"	: "",
			"caracteristicas" : "",
		}


	def dormir(self, indice, ratio, minutos = 5):

		if indice % ratio == 0:

			print('Durmiendo...')

			time.sleep(minutos * 60)


	def enviar_url(self, url):

		datos = {
			'accion': 	self.fuente,
			'hash': 	self.hash,
			'url' : 	url,
		}

		res = requests.post(self.url, datos)

		if res.status_code == 200:

			try:
				return json.loads(res.text)

			except:

				txt = res.text + "\n"

				return txt

		return False


	def enviar_resultados_old(self):

		if len(self.anuncios) > 0:

			datos_json = json.dumps(self.anuncios)

			datos = {
				'accion': 		'guardar_anuncio_scracher',
				'hash': 		self.hash,
				'datos': 		datos_json,
				'id_asociado': 	self.id_asociado,
				'id_municipio': self.id_municipio,
			}

			# url    = "http://localhost/dp/plataforma/auto/4887_api_scracher.php"

			# res = requests.post(url, datos)
			res = requests.post(self.url, datos)

			if res.status_code == 200:
				# print(res.text)
				return json.loads(res.text)

			return False

		return "No hay anuncios que enviar."


	def escribir_log(self, log):

		direc = os.getcwd()

		mac = re.search('htdocs', direc)
		windows = re.search('(system32|wamp64)', direc)

		if windows != None:

			direc = "C:\\wamp64\\www\\cron\\logs\\"

		else :

			direc += "/"

		Fx.escribir_log(direc + self.fuente + '_scracher_log.txt', log)


	def esperar_elemento(self, selector = '', tipo = 'id', delay = 15):

		pagina = False

		if selector == '': 
			
			pagina = WebDriverWait(self.driver, delay)

		elif tipo == 'id':

			pagina = WebDriverWait(self.driver, delay).until( EC.presence_of_element_located((By.ID, selector)) )

		elif tipo == 'clase':

			pagina = WebDriverWait(self.driver, delay).until( EC.presence_of_element_located((By.CLASS_NAME, selector)) )

		return pagina


	def esperar_visibilidad(self, selector = '', tipo = 'id', delay = 15):

		if selector == '': return False

		pagina = False

		if tipo == 'id':

			pagina = WebDriverWait(self.driver, delay).until( EC.visibility_of_element_located((By.ID, selector)) )

		elif tipo == 'clase':

			pagina = WebDriverWait(self.driver, delay).until( EC.visibility_of_element_located((By.CLASS_NAME, selector)) )

		return pagina


	def establece_asociado(self, id_asociado): self.id_asociado = id_asociado;


	def establece_municipio(self, id_municipio): self.id_municipio = id_municipio;


	def establece_fuente(self, fuente):	self.fuente = fuente


	def establece_provincia(self, provincia): self.provincia = provincia


	# def leer_enlaces_contr(self, set_enlaces):
	def leer_enlaces_contr(self):

		tabla = self.buscar_elemento("myTablaBusquedaCustom", "id")

		html = tabla.find_elements_by_class_name('tdExpediente')
		# html = driver.find_element_by_id('myTablaBusquedaCustom').find_elements_by_class_name('tdExpediente')
		regex = r"idLicitacion':'([0-9]*)'"
		enlace_base = "https://contrataciondelestado.es/wps/portal/!ut/p/b1/jc7JCsIwGATgR8qfvR7TJUmlLhBSbS6Sg0ily0V8fmPxanVuA9_AoIA6LhkHyalEZxSm-Oxv8dHPUxzePYhL7rJM5ViBcTsMSlRUcALYOJJAlwCnBWu37VG42gDUVpeNxxwMEf_t4UsU_NqfUFgIqw5FoS2BzNESSFN6L2yqhnzA2sUFrHzY23m8ojEMelPf2QvicMGP/dl4/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_BS88AB1A0GSM10A6E365201G25/act/id=0/p=ACTION_NAME_PARAM=SourceAction/p=idLicitacion="

		# print( "cantidad", len(html) )

		for expediente in html:

			id_expediente = re.search( regex, expediente.get_attribute('innerHTML') )

			enlace = enlace_base + id_expediente.group(1) + '/327063124463/-/'
			# print(expediente.get_attribute('innerHTML'))
			
			self.url_concursos.append(enlace)
			# set_enlaces.append(enlace)

		# mi_set = set(set_enlaces)

		# return mi_set

		#BUSCAR ENLACES
		# matches = re.finditer(regex, html)

		# for matchNum, match in enumerate(matches):
		#     matchNum = matchNum + 1
			
		#     for groupNum in range(0, len(match.groups())):
		#         groupNum = groupNum + 1
				
		#         if(groupNum == 1):
		#             enlace = 'https://contrataciondelestado.es/wps/portal/!ut/p/b1/jc7JCsIwGATgR8qfvR7TJUmlLhBSbS6Sg0ily0V8fmPxanVuA9_AoIA6LhkHyalEZxSm-Oxv8dHPUxzePYhL7rJM5ViBcTsMSlRUcALYOJJAlwCnBWu37VG42gDUVpeNxxwMEf_t4UsU_NqfUFgIqw5FoS2BzNESSFN6L2yqhnzA2sUFrHzY23m8ojEMelPf2QvicMGP/dl4/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_BS88AB1A0GSM10A6E365201G25/act/id=0/p=ACTION_NAME_PARAM=SourceAction/p=idLicitacion=' + match.group(groupNum) + '/327063124463/-/'
		#             arr_enlaces.append(enlace)


	def leer_enlaces_galicia(self):

		tabla = self.buscar_elemento("tabResultados", "id")
		body = self.buscar_elemento("tbody", "etiqueta", tabla)
		html = body.get_attribute('innerHTML')

		# html = driver.find_element_by_id('tabResultados').find_element_by_tag_name('tbody').get_attribute('innerHTML')

		#BUSCAR ENLACES
		regex = r"N=([0-9]{4,})"

		matches = re.finditer(regex, html)

		enlace_base = 'https://www.contratosdegalicia.gal/licitacion?OP=50&N='
		enlace_sufijo = '&lang=es'

		for matchNum, match in enumerate(matches):
			matchNum = matchNum + 1
			
			for groupNum in range( 0, len(match.groups()) ):

				groupNum = groupNum + 1
				
				if(groupNum == 1):

					enlace = enlace_base + match.group(groupNum) + enlace_sufijo

					self.url_concursos.append(enlace)

		mi_set = set(self.url_concursos)
		self.url_concursos = sorted(list(mi_set))
		# return mi_set

	
	def leer_enlaces_valladolid(self):

		# html = driver.find_element_by_id('row').find_element_by_tag_name('tbody')
		# links = html.find_elements_by_xpath('.//td[@style="width: 24%;"]/a')
		
		def devuelve_estado(estado):

			if re.match( 'Licitaci[^n]+n', estado ):

				return 2

			if re.match( 'Adjudicada', estado ):

				return 5

			if re.match( 'Formalizada', estado ):

				return 6
			
			return 1


		row = self.buscar_elemento("row", "id")
		tbody = self.buscar_elemento("tbody", "etiqueta", row)

		links = tbody.find_elements_by_xpath('.//td[@style="width: 24%;"]/a')

		estados = tbody.find_elements_by_xpath('.//td[@style="width: 8%;"]')
		
		assert len(links) == len(estados), 'Debería haber el mismo número de enlaces que de estados.'

		# print(links);
		for indice in range( len(links) ):
			
			concurso = {}

			concurso['href'] = links[indice].get_attribute('href')  
			concurso['objeto'] = links[indice].get_attribute('innerHTML')

			estado = devuelve_estado( estados[indice].get_attribute('innerHTML') );
			concurso['estado'] = estado

			self.url_concursos.append( concurso )
			# arr_enlaces.append( concurso )
		
		# return arr_enlaces


	def imprimir_anuncios(self):
		
		for anuncio in self.anuncios:

			print("\n Anuncio:")

			for attr in anuncio:

				print( "\t" + attr + ": " + str(anuncio[attr]) )


	def mover_hasta_elemento(self, elemento):

		print(elemento)

		try:

			self.actions.move_to_element(elemento).perform()

		except MoveTargetOutOfBoundsException:

			print("Error de movimiento: Elemento fuera de límites")

		except Exception as error:

			print("Error de movimiento: ", error)


	def pantalla_completa(self):

		self.driver.maximize_window()


	def recibir_zonas(self):

		datos = {
			'accion': 'recibir_zonas',
			'hash':   self.hash
		}
		
		url = "https://abogadosyarbitraje.com/plataforma/auto/4887_api_scracher.php"

		zonas = requests.post(url, datos).json()
		# zonas = requests.post(self.url, datos).json()

		if len(zonas) > 0:

			self.zonas = zonas

			return self.zonas

		return False



if __name__ == "__main__":



	scracher = Scracher()

	# print( scracher.devuelve_anuncio_base() )

	# scracher.escribir_log('Jajaja')

	# scracher.dormir(100)

	# scracher.abrir_conexion()

	# zonas = scrach.recibir_zonas()

	# assert len(zonas) > 0, 'Scracher debería recibir zonas.'

	# assert scrach.driver != False, 'Scracher debería driver válido'

	# assert isinstance(scrach.driver, webdriver.firefox.webdriver.WebDriver), 'Debería tener clase WebDriver de firefox'

	# url = "http://idealista.com/venta-viviendas/ciudad-real-provincia/"

	# scracher.establece_asociado("27");
	# scracher.establece_provincia("Ciudad Real");

	# scracher.conectar(url)

	# pagina = scracher.esperar_elemento('main-content')

	# scracher.leer_idealista()

	# prim = scracher.anuncios[0]

	# assert len( prim.get('propietario') ) > 0, 'Propietario debería tener contenido'


	# scrach.anuncios.append(anuncio_idealista)

	# scrach.enviar_resultados()



	# scracher.cerrar()
	# print anuncio



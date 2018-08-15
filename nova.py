#!usr/bin/python3
# -*- coding: utf-8 -*-

'''
Script diseñado para entrar en el curso de Python3 y cambiar de pagina entre las del primer
capítulo cada hora, hasta un total de 6
'''

import re
import time
import sys
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def eliminar_chat():

	global chat

	try:
		mi_chat = WebDriverWait( driver, 10 ).until( EC.presence_of_element_located((By.ID, 'chat-init')), 'Chat' )
		boton_x = mi_chat.find_element_by_id('chat-closed')
		boton_x.click()

		print( "chat cerrado" )
		chat = True

	except:
		print( "No hay ventana de chat" )


driver = webdriver.Firefox()

driver.get("https://campus.euroinnova.edu.es/")
retraso = 20

mi_login = WebDriverWait( driver, retraso ).until( EC.presence_of_element_located((By.ID, "login")) )
user = mi_login.find_element_by_id("username")
user.send_keys('AIZQUIERDO')

password = mi_login.find_element_by_id("password")
password.send_keys('33510211')

acceder = mi_login.find_element_by_id('loginbtn')
acceder.click()


try:
	chat = False
	
	# time.sleep(10)
	# enlace = driver.find_element_by_class_name('student').find_element_by_tag_name('a')
	# student = WebDriverWait( driver, retraso ).until( EC.element_to_be_clickable(enlace), 'Enlace al curso no es clickable' )
	student = WebDriverWait( driver, retraso ).until( EC.element_to_be_clickable((By.CLASS_NAME, 'student')), 'Enlace al curso no es clickable' )
	student.click()

	# mi_horario = WebDriverWait( driver, 5 ).until( EC.presence_of_element_located((By.CLASS_NAME, 'showSweetAlert')), 'Modal de horario no encontrado' )
	# loc_boton_no = mi_horario.find_element_by_class_name("cancel")
	boton_no = WebDriverWait( driver, retraso ).until( EC.element_to_be_clickable((By.CLASS_NAME,'cancel')), 'Enlace a NO no es clickable' )
	boton_no.click()


	try:
		print( "Buscando boton de confirmar..." )
		mi_confir = WebDriverWait( driver, 10 ).until( EC.presence_of_element_located((By.CLASS_NAME, 'sa-button-container')), 'Enlace a confirmar NO localizado' )

		boton_confirm = WebDriverWait( driver, retraso ).until( EC.element_to_be_clickable((By.CLASS_NAME,'confirm')), 'Enlace a Confirm no es clickable' )
		boton_confirm.click()

	except:
		print( "No hay boton de confirmar" )

	# Entrada al curso
	mi_unidad = WebDriverWait( driver, retraso ).until( EC.element_to_be_clickable((By.ID, 'section-1')), 'Buff' )
	titu = mi_unidad.find_element_by_class_name("activityinstance").find_element_by_tag_name("a")
	titu.click()

	contador = 0
	while True:

		contador += 1
		capitulos = WebDriverWait( driver, retraso ).until( EC.presence_of_all_elements_located((By.CLASS_NAME, 'title-sco')), 'No hay lista de capitulos' )

		if chat == False:
			eliminar_chat()
		
		print( "Pagina: ", contador )

		elemento = random.randrange( 1, 5 )
		# elemento = random.randrange( 0, len(capitulos) )
		print( 'elemento de azar: ', elemento )
		capitulos[elemento].click()

		extra = random.randrange( 0, 100 )
		cabezada = extra + 1650
		print( "Durmiendo 1 hora (3600 segundos) más el extra..." )
		time.sleep(cabezada)
		print( "...Llevas 30 min (1650 segundos)...")
		time.sleep(1350)
		print( "...Faltan 5 min (300 segundos)...")
		time.sleep(300)

		if contador == 6:
			break


	a = "Final del programa!!"

except WebDriverException as web_error:
	print( "Error web: ", type(web_error) )
	print( "Error web mensaje: ", web_error )

except TimeoutException as tiempo:
	print( "Tiempo: ", tiempo )


except Exception as error:
	print( "Cagada: ", error)
	e = sys.exc_info()[1]
	print( "sistema: ", e.args[0])

finally:
	if 'a' in vars(): 
		print( a )
		driver.close()
	





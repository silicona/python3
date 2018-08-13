#!usr/bin/python3
# -*- coding: utf-8 -*-

import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("https://campus.euroinnova.edu.es/")
retraso = 15

mi_login = WebDriverWait( driver, retraso ).until( EC.presence_of_element_located((By.ID, "login")) )
user = mi_login.find_element_by_id("username")
user.send_keys('AIZQUIERDO')

password = mi_login.find_element_by_id("password")
password.send_keys('33510211')

acceder = mi_login.find_element_by_id('loginbtn')
acceder.click()


mi_pagina = WebDriverWait( driver, retraso ).until( EC.presence_of_element_located((By.CLASS_NAME, 'student')) )
boton = mi_pagina.find_element_by_tag_name('a')
var = boton.location_once_scrolled_into_view
print( 'Var:', var)
if var != None:
	# driver.execute_script( "return arguments[0].scrollIntoView();", boton )
	boton.click()


mi_horario = WebDriverWait( driver, retraso ).until( EC.presence_of_element_located((By.CLASS_NAME, 'showSweetAlert')) )

boton_no = mi_horario.find_element_by_partial_link_text("NO")
boton_no.click()


mi_confir = WebDriverWait( driver, retraso ).until( EC.presence_of_element_located((By.CLASS_NAME, 'sa-confirm-button-container')) )
boton = mi_confir.find_element_by_xpath('.//button')
boton.click()

mi_unidad = WebDriverWait( driver, retraso ).until( EC.presence_of_element_located((By.ID, 'section-1')) )
titu = mi_unidad.find_element_by_class_name("activityinstance").find_element_by_tag_name("a")
titu.click()

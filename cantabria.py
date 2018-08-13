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


def leer_enlaces():

    lista_enlaces = []
    myElem = WebDriverWait(driver, delay).until( EC.presence_of_element_located((By.ID, 'expediente')) )
    tabla = myElem.get_attribute('innerHTML')
    print( "Página lista" )

    reg = re.compile(r"(perfilcontratante\/auth\/expedientes\/show\/[\d]+)")
    coincidencias = reg.finditer(tabla)

    for matchNum, match in enumerate(coincidencias):
        lista_enlaces.append( "/" + match.group(1) )
        # lista_enlaces.append( 'https://aplicacionesweb.cantabria.es/' + match.group(1) )

    return lista_enlaces

def devuelve_vocal(vocal_acentuada):

    if ord(vocal_acentuada) in range(225, 228):
        return 'a'
    if ord(vocal_acentuada) in range(233, 235):
        return 'e'
    if ord(vocal_acentuada) in range(236, 239):
        return 'i'
    if ord(vocal_acentuada) in range(242, 246):
        return 'o'
    if ord(vocal_acentuada) in range(249, 252):
        return 'u'
    if ord(vocal_acentuada) in range(192, 196):
        return 'A'
    if ord(vocal_acentuada) in range(200, 203):
        return 'E'
    if ord(vocal_acentuada) in range(225, 228):
        return 'I'
    if ord(vocal_acentuada) in range(210, 214):
        return 'O'
    if ord(vocal_acentuada) in range(217, 220):
        return 'U'


def devuelve_tipo_notificacion(id_o_nombre):

    notificaciones = {
        1: "anuncio",
        2: "licitacion",
        3: "adjudicacion provisional",
        4: "adjudicacion definitiva",
        5: "adjudicacion",
        6: "formalizacion",
        7: "pliego",
        8: "otros"
    }

    if type(id_o_nombre) == "int":
        return notificaciones.get( id_o_nombre, 'id inválido' )

    else:
        for clave, valor in notificaciones.items():
            if valor == id_o_nombre:
                return clave
    

def quitar_acentos(string):

    acentos = [
        'á', 'à', 'â', 'ã', 'ä',
        'Á', 'À', 'Â', 'Ã', 'Ä',
        'é', 'è', 'ê', 'ë',
        'É', 'È', 'Ê', 'Ë',
        'í', 'ì', 'î', 'ï',
        'Í', 'Ì', 'Î', 'Ï',
        'ó', 'ò', 'ô', 'õ', 'ö',
        'Ó', 'Ò', 'Ô', 'Õ', 'Ö',
        'ú', 'ù', 'û', 'ü',
        'Ú', 'Ù', 'Û', 'Ü'
    ]

    for acento in acentos:

        if acento in string:

            vocal = devuelve_vocal(acento)
            string = string.replace(acento, vocal)

    return string


def formatear_importe(importe):

    importe = importe.replace('.', '').replace(',', '.')
    return importe


def fecha_a_mysql(fecha):

    # Convierte lafecha de dd/mm/yyyy a yyyy-mm-dd
    list_fecha = fecha.split('/').reverse();
    return "".join(list_fecha)


def fecha_a_normal(fecha):

    # Convierte lafecha de yyyy-mm-dd a dd/mm/yyyy
    list_fecha = fecha.split('-').reverse();
    return list_fecha.join()




driver = webdriver.Firefox()


driver.get("https://aplicacionesweb.cantabria.es/perfilcontratante/portal/PORTALINSTITUCIONAL")
# driver.get("https://aplicacionesweb.cantabria.es/perfilcontratante/auth/expedientes/search")


# Pulsar el boton de busqueda
driver.find_element_by_id('idButtonBuscar').click()

#ESPERAR A QUE CARGUEN LOS RESULTADOS
delay = 10 # seconds

# tabla = WebDriverWait(driver, delay).until( EC.presence_of_element_located((By.ID, 'expediente')) )





lista_enlaces = leer_enlaces()
print( lista_enlaces )

# myElem = WebDriverWait(driver, delay).until( EC.presence_of_element_located((By.ID, 'expediente')) )

quitar_acentos("jaja")

lista_concursos = []
for indice, enlace in enumerate(lista_enlaces):

    try:
        # driver.find_element_by_id('idButtonBuscar').click()

        myElem = WebDriverWait(driver, delay).until( EC.presence_of_element_located((By.ID, 'expediente')) )
        # filas = myElem.find_elements_by_xpath(".//tr")

        boton = myElem.find_element_by_xpath(".//td[@style='accion-ancho']/a[@href='" + enlace + "']")
        boton.click()

        concurso = {}
        lateral = WebDriverWait( driver, delay ).until( EC.presence_of_element_located((By.CLASS_NAME, 'nav-stacked')) )
        # lateral = anuncio.find_element_by_class_name("nav-stacked")        
        li_activo = lateral.find_element_by_class_name("active")
        concurso['id_tipo_notificacion'] = devuelve_tipo_notificacion( quitar_acentos(li_activo.text).lower() )

        lis = lateral.find_elements_by_xpath(".//li")
        concurso['expediente'] = lis[2].text

        anuncio = WebDriverWait( driver, delay ).until( EC.presence_of_element_located((By.ID, 'anuncio')) )

        lis_estado = lateral.find_elements_by_class_name("boton-barra-lateral")

        # Pestaña Anuncio
        lis_estado[0].click()

        # datos_anuncio = WebDriverWait(driver, 2).until( EC.presence_of_element_located((By.ID, 'descripcion')) )
        # concurso['titulo'] = datos_anuncio.text.lower().capitalize()
        descripcion = anuncio.find_element_by_id("descripcion")
        concurso['titulo'] = descripcion.text.lower().capitalize()

        cajas_anuncio = anuncio.find_elements_by_class_name("col-md-4")
        dict_datos = {}
        list_fechas_pub = []
        for caja in cajas_anuncio:

            eti = caja.find_element_by_tag_name("label").text
            eti = quitar_acentos(eti).lower()

            val = caja.find_element_by_tag_name("input").get_attribute("value")

            dict_datos[eti] = val
        

        for etiqueta, valor in dict_datos.items():

            if etiqueta == "organismo":
            # if etiqueta == "organo de contratacion":
                concurso['organismo_contratacion'] = valor
        
            if etiqueta == "tipo de contrato":
                concurso['tipo_contrato'] = valor

            if etiqueta == "procedimiento":
                concurso['procedimiento'] = valor

            if etiqueta == "presupuesto licitacion":

                regexp = r"([\d\,\.]+)"
                list_valores = re.finditer(regexp, valor)

                concurso['importe'] = formatear_importe( list_valores.group[1] )

            if( etiqueta == "fecha b.o.c." or etiqueta == "fecha b.o.e." or
                etiqueta == "fecha d.o.u.e" or etiqueta == "fecha publicacion" ): # B. O. de Cantabria

                list_fechas_pub.append( fecha_a_mysql(valor) )
                # concurso['f_publicacion'] = fecha_a_mysql( valor )

            # if etiqueta == "fecha publicacion":
            #     list_fechas_pub.append( fecha_a_mysql(valor) )

            if etiqueta == "fecha limite proposiciones":
                concurso['f_recepcion_ofertas'] = fecha_a_mysql( valor )

        

         # Pestaña Licitación
        lis_estado[1].click()


        lista_concursos.append(concurso)

        break

        driver.back()

    except Exception as e:
        print( "Excepcion: ", str(e) )


print( lista_concursos )

# boton_sgte = driver.find_element_by_partial_link_text('Siguiente')

driver.close()


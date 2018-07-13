print( "\n2 - Creacion de módulos en Python\n" )

import modulo_1
import modulo_2

modulo_1.metodo_modulo_1()
modulo_2.metodo_modulo_2()

print( "Usando alias para los módulos" )
import modulo_1 as m1
import modulo_2 as m2

m1.metodo_modulo_1()
m2.metodo_modulo_2()

print( "Creando variables con Path de Python.\n" )
print( "El modulo importado debe estar en alguna referencia del Path.\n" )

import sys
print ( "Path: " )
print( sys.path )

print( "\nUsado paquetes de Python\n")

print( "El paquete va en una carpeta con los módulos necesarios y el archivo __init__.py, que en principio va vacio.\n" )
print( "En la carpeta '__pycache__' se crean los archivos python compilados de los módulos, tanto en el main como en la carpeta del paquete.\n")

from paquete import modulo_paquete_A as mod_paqA
from paquete import modulo_paquete_B as mod_paqB

mod_paqA.metodo_A()
mod_paqB.metodo_B()


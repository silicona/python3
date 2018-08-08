#!usr/bin/python3
# -*- coding: UTF-8 -*-

import pymysql as sql

print( "3 - Mysql en Python" )

print( "Creada BBDD en local: curso_python3" )

print( 'Instalado pymysql desde consola con: "pip3 install pymysql"')

print( "\nScript Crear tabla en BBDD local")

conexion = sql.connect( host='localhost', user='usuario', password='pass', database='curso_python3' )

cursor = conexion.cursor()
cursor.execute( 'CREATE TABLE IF NOT EXISTS demo (id INT, datos VARCHAR(255));')

cursor.execute( 'SELECT VERSION();' )

version = cursor.fetchone()
print( "Version de la BBDD local: %s " % version)

cursor.close()
conexion.close()

print( "\nScript insertar en BBDD local" )

conexion = sql.connect( host='localhost', user='usuario', password='pass', database='curso_python3' )

cursor = conexion.cursor()
res = cursor.execute( "INSERT INTO demo (id, datos) VALUES ('5', 'curso');")

print( 'Res: ' + str(res) )

conexion.commit()

conexion.close()

print( "\nScript Seleccionar tabla en BBDD local")

conexion = sql.connect( host='localhost', user='usuario', password='pass', database='curso_python3' )

cursor = conexion.cursor()
valor = 5
cursor.execute( 'SELECT * FROM demo WHERE id = %d;' %  valor )
filas = cursor.fetchall()

for fila in filas:

	print( fila )
	print( "\n" )

cursor.close()
conexion.close()

print( "\nScript Borrar de tabla en BBDD local")

conexion = sql.connect( host='localhost', user='usuario', password='pass', database='curso_python3' )

cursor = conexion.cursor()
valor = 5
cursor.execute( 'DELETE FROM demo WHERE id = %d;' %  valor )

conexion.commit()

cursor.close()
conexion.close()


print( "\nScript con Sqlite3 comentados por falta de instalacion en navegador local")

# import sqlite3

# conexion = sqlite3.connect( 'curso_python3' )
# query = "insert into 'datos ('id', 'datos') values ('1', '30')"

# conexion.execute( query )
# conexion.commit()
# conexion.close()


# Script de Seleccion
# conexion = sqlite3.connect( 'curso_python3' )

# for fila in conexion.execute( "SELECT * FROM 'datos';" )
	
# 	print( fila )

# conexion.close()


# Script de Borrado
# conexion = sqlite3.connect( 'curso_python3' )
# query = "DELETE FROM 'datos' WHERE id='1';"

# conexion.execute( query )
# conexion.commit()
# conexion.close()
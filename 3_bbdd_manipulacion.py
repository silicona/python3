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

print( "\nPostgreSql" )

print( "Instalar con pip psycopg2" )

print( "Comentado a falta de una base de datos PostGre" )

# import psycopg2, psycopg2.extras

# conn = psycopg2.connect( database = 'postgre', user = 'postgre', password = 'postgre', host = 'localhost' )

# cursor = conn.cursor()
# cursor.execute( "SELECT * FROM public.prueba" )
# filas = cursor.fetchall()

# print( filas )


print( "\nLDAP" )

print( "Lightweight Directory Access Protocol")

print( "Instalar con pip-3.2 install ldap3" )

print( "Comentado a falta de servidor LDAP" )

print( "Especificar antes: auto_bind = AUTO_BIND_TLS_BEFORE_BIND" )

# from ldap3 import Server, Connection, All, Tls
# from ldap3.core.exceptions import LDAPExceptionError, LDAPBindError, LDAPInvalidCredentialsResult, LDAPSizeLimitExceededResult

# s = Server( 'ldap.dominio.com', port = 389, get_info = ALL )
# c = Connection( s, user = 'cn=admni,dc=dominio,dc=com', password = 'S3cr3t0', auto_bind = True )

# c.strat_tls()
# c.bind()
# c.search( 'dc=dominio,dc=com', '(uid=*)', attributes = ['sn', 'cn', 'homeDirectory'], size_limit = 0 )

# for entrada in c.response:

# 	print( entrada['dn'] )

# Sign up for free

print( "\tGestión de datos con LDAP - comentado" )

# try: 
# 	resul_id = l.search( base, scope, filter, retrieve_attributes )

# 	while 1:
# 		result_type, result_data = l.result( result_id, timeout )

# 		if result_data == []:
# 			break

# 		else:
# 			if result_type == ldap.RES_SEARCH_ENTRY:
# 				result_set.append( result_data )
# except:
# 	print( "\tCazada")

# # INSERCIÖN Modo Sincronico
# import ldap
# import ldap.modlist as modlist

# conn = ldap.initialize( "ldaps://localhost.localdomain:636/" )

# conn.simple_bind_s( "cn=manager,dc=example,dc=com", "secret" )

# dn = "cn=replica,dc=example,dc=com"

# cuerpo = {}
# cuerpo['objectclass'] = ['top', 'organizationalRole', 'simpleSecurityObject']
# cuerpo['cn'] = 'replica'
# cuerpo['userPassword'] = 'aDifferentSecret'
# cuerpo['description'] = 'Objeto de usuario para la replicación usando slurpd'

# conndif = modlist.addModlist( cuerpo )

# conn.add_s( dn, conndif )

# conn.unbind_s()

# # INSERCIÖN Modo Asincrono
# import ldap

# try:
# 	conn = ldap.open( "127.0.0.1" )
# 	conn.protocol_version = ldap.VERSION3

# except ldap.LDAPError, e:
# 	print e

# baseDN = "ou=Customers,ou=Sales,o=dominio.com"
# searchScope = ldap.SCOPE_SUBTREE
# retrieveAttributes = None
# searchFilter = "cn=*jack"

# try:
# 	ldap_result_id = conn.search( baseDN, SearScope, searchFilter, retrieveAttributes )
# 	result_set = []

# 	while 1:
# 		result_type, result_data = conn.result( ldap_result_id, 0 )

# 		if result_data == []:
# 			break

# 		else:
# 			if result_type == ldap.RES_SEARCH_ENTRY:
# 				result_set.append( result_data )
# 	print( result_set )

# except ldap.LDAPError, e:
# 	print(e)

print( "\nConexiones SSL" )

# import socket
# import ssl

# mi_socket_ssl = ssl.wrap_socket(
# 	sock,
# 	keyfile = None,
# 	certfile = None,
# 	server_side = False,
# 	cert_reqs = CERT_NONE,
# 	ssl_version = {ver docs},
# 	ca_certs = None,
# 	do_handshake_on_connect = True,
# 	suppress_ragged_eofs = True,
# 	ciphers = None )

# # Ejemplo de Socket SSL
# ejemplo_ssl = ssl.wrap_socket(
# 	mi_socket,
# 	server_side = True,
# 	keyfile = 'mi_keyfile.pem',
# 	certfile = "mi_certfile.pem",
# 	ssl_version = ssl.PROTOCOL_SSLv23 )
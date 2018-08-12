#!usr/bin/python3
# -*- coding:utf-8 -*-

print( "\nServidor" )

import socket

def Main():

	host = "127.0.0.1"
	port = 5000

	miSocket = socket.socket()
	miSocket.bind( (host, port) )

	miSocket.listen(1)

	conexion, direccion = miSocket.accept()

	print( "Conexion desde: ", str(direccion) )

	while True:
		datos = conexion.recv(1024).decode()

		if not datos:
			break

		print( "desde el usuario conectado: ", datos )

		datos = str(datos).upper()
		print( "enviando: " + str(datos) )
		conexion.send( datos.encode() )

	conexion.close()

if __name__ == "__main__":

	Main()
	
#!usr/bin/python3
# -*- coding:utf-8

import socket

def Main():

	host = "127.0.0.1"
	port = 5000

	miSocket = socket.socket()
	miSocket.connect( (host, port) )

	mensaje = input( " -> ")

	while mensaje != 'q':

		miSocket.send( mensaje.encode() )
		datos = miSocket.recv(1024).decode()

		print( "Recibido del servidor: ", datos )

		mensaje = input(" -> ")

	miSocket.close()


if __name__ == '__main__':

	Main()


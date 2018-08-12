#!usr7bin/python3
# -*- coding:utf-8 -*-

print( "THREADS" )

import os
import multiprocessing
import threading
import time
import _thread

def solo_dormir():

	print( "PID: %s, Nombre del Proceso: %s, nombre del Thread: %s" % (
		os.getpid(),
		multiprocessing.current_process().name,
		threading.current_thread().name
		)
	)

	time.sleep(1)

solo_dormir()

def print_time( nombreThread, retraso ):

	contador = 0

	while contador < 5:

		time.sleep(retraso)
		contador += 1
		print( "%s %s" % ( nombreThread, time.ctime(time.time()) ) )


# Creamos dos hilos
try:
	_thread.start_new_thread( print_time, ("hilo 1", 2, ) )
	_thread.start_new_thread( print_time, ("hilo 2", 4, ) )
	
except:
	print( "Error: no se puede iniciar el hilo" )

# while 1:
# 	pass

time.sleep(10)

print( "GESTION DE UN PROCESO" )

from multiprocessing import Pool

def funcion_un_proceso(x):

	return x * x

print( "GESTION DE VARIOS PROCESOS" )

from multiprocessing import Process

def print_func( continente = 'Asia' ):
	print( "El nombre del continente es: ", continente )


print( "\nDAEMON" )

print( "Instalar con apt-get python-daemon python-lockfile")

import logging

logging.basicConfig( level = "INFO" )

ok = True
cont = 0
while ok:
	logging.info( "He despertado, humano!!" )
	time.sleep(2)
	cont += 1

	if cont == 4:
		break


print( "\nASINCRONIA")

import asyncio

async def saludar():

	print( "Temblad, humanos!!" )
	await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete( saludar() )
loop.close()



if __name__ == '__main__':

# Un proceso
	p = Pool(5)
	print( "\tMapeo: ", p.map( funcion_un_proceso, [1, 2, 3] ) )

# Varios procesos
	nombres = ['América', 'Europa', 'África']
	procesos = []
	proceso = Process( target = print_func ) # Instanciamos sin argumento para Asia

	procesos.append( proceso )
	proceso.start()

	#instanciamos procesos con nombre
	for nombre in nombres:

		proceso = Process( target = print_func, args = (nombre,))
		procesos.append( proceso )

		proceso.start()

	# Completamos los procesos
	for proceso in procesos:

		proceso.join()

